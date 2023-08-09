from django.shortcuts import render, redirect

from django.http.response import JsonResponse, HttpResponse
from django.urls import reverse
from rest_framework.parsers import JSONParser 
from rest_framework import status,filters
from django.core.exceptions import ObjectDoesNotExist

from django.db.models import Max
from myapp.models import MyUser, Local, UserProfile, TiposRecursos, TiposDispositivos, TiposLocais, PreferenciaLocais, PreferenciaDispositivos, PreferenciaRecursos
from myapp.serializers import UserSerializer, LocalSerializer
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .admin import UserCreationForm
from django.db.models import Q
from .forms import UserProfileForm


error_translation = {
    'This field is required.': 'Este campo é obrigatório.',
    'Enter a valid email address.': 'Insira um endereço de e-mail válido.',
    'A user with that username already exists.': 'Já existe um usuário com esse nome de usuário.',
    'This password is too short. It must contain at least 8 characters.': 'A senha é muito curta. Deve conter pelo menos 8 caracteres.',
    'This password is too common.': 'Esta senha é muito comum.',
    'This password is entirely numeric.': 'A senha é totalmente numérica.',
    'This password is too similar to the username.': 'A senha é muito semelhante ao nome de usuário.',
    'The two password fields didn’t match.': 'As duas senhas não correspondem.',
    # Add more translations for other error messages if needed
}


def index(request):
    print('index being load')
    search_query = request.GET.get('search', '')
    locals = Local.objects.filter(nome__icontains=search_query).order_by('-nota')[:10]
    local_serializer = LocalSerializer(locals, many=True)
    return render(request,'home.html',{'data': local_serializer.data})


def user_register(request):
     if request.method == "POST":
        form = UserCreationForm(request.GET)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'redirect_url': reverse('results')})
        else:
            # Display form errors
            errors = form.errors.as_data()
            error_messages = []
            for field, error_list in errors.items():
                for error in error_list:
                    for message in error:
                        translated_message = error_translation.get(str(message), str(message))
                        error_messages.append(f"{field}:{translated_message}")
            return JsonResponse({'success': False, 'message':error_messages})

def user_login(request):   
    if request.method == "GET":
        email = request.GET.get('email')
        password = request.GET.get('password')
        print(f"email:{email}\npassword:{password}")
        user = authenticate(request, email=email, password=password)
        print(f"request:{user}")
        if user != None:
            print("Redirect")
            login(request, user)
            return JsonResponse({'success': True, 'redirect_url': reverse('index')}) 
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'})


@login_required
def complementar_register(request):
    usuario = request.user
    user_profile_exists = UserProfile.objects.filter(user=usuario).exists()
    if user_profile_exists:
        return redirect(user_display) 
    
    if request.method == 'POST':
        additional_form = UserProfileForm(request.POST)
        if additional_form.is_valid():
            current_user = additional_form.save(commit=False) #Cria uma instancia de UserProfile
            current_user.user = request.user #Associa o UserProfile ao usuário logado (MyUser)
            current_user.save()
            """ 
                As proximas linhas repetem para locais, recursos e dispositivos:
                Armazena os id dos elementos selecionados no form pelo usuário
                Para cada id armazenado:
                Usa o id para instanciar um tipo de elemento
                Instancia Preferencias com  o usuario logado e o tipo de elemento
                Salva o id usuario e o id elemento na tabela"""
            preferencia_locais_ids = additional_form.cleaned_data['preferencia_locais'].values_list('id', flat=True)
            for tipo_local_id in preferencia_locais_ids:
                tipo_local_instance = TiposLocais(tipo_local_id)
                preferencia_locais_instance = PreferenciaLocais(user=current_user.user, local=tipo_local_instance)
                preferencia_locais_instance.save()
            preferencia_recursos_ids = additional_form.cleaned_data['preferencia_recursos'].values_list('id', flat=True)
            for tipo_recurso_id in preferencia_recursos_ids:
                tipo_recurso_instance = TiposRecursos(tipo_recurso_id)
                preferencia_recursos_instance = PreferenciaRecursos(user=current_user.user, recurso=tipo_recurso_instance)
                preferencia_recursos_instance.save()
            dispositivo_aux_marcha_ids = additional_form.cleaned_data['preferencia_dam'].values_list('id', flat=True)
            for tipo_dam_id in dispositivo_aux_marcha_ids:
                tipo_dispositivo_instance = TiposDispositivos(tipo_dam_id)
                preferencia_dispositivos_instance = PreferenciaDispositivos(user=current_user.user, dispositivo=tipo_dispositivo_instance)
                preferencia_dispositivos_instance.save()
            
            return redirect('index') # Redirecionar para a tela de perfil quando criar
    else:
        additional_form = UserProfileForm()

    return render(request, 'comp.html', context={'additional_form': additional_form,})   

@login_required(login_url='login')
def home(request):
    user = request.user 

    context = {'user': user}
    return render(request, 'home.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('index')       


@api_view(['GET', 'POST', 'DELETE'])
def users_list(request):
    if request.method == 'GET':
        users = MyUser.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            users = users.filter(title__icontains=title)
        
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        users_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': #Delete all instances
        count = MyUser.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

def results(request):
    search = False
    tags = False
    try: search_query = request.GET.get('searchQuery') 
    except: pass
    try: selected_types = request.GET.get('checkboxesData')
    except: pass

    locals = Local.objects.all()
    if selected_types == 'all' and search_query == 'all':
        tags = True
        # search = True
    else: 
        if selected_types and selected_types != 'undefined':
            selected_types = selected_types.split(',')
            locals = locals.filter(tipo__in=selected_types)
            tags = True

        if search_query and search_query != 'undefined':
            locals = locals.filter(Q(nome__icontains=search_query))
            search = True
        

    local_serializer = LocalSerializer(locals, many=True)
    unique_types = Local.objects.values_list('tipo', flat=True).distinct()

    context = {
        'data': local_serializer.data,
        'types': list(unique_types),
        'selected_types': selected_types,
        'search_query': search_query,
    }

    if search or tags:
        return JsonResponse(context)
    return render(request, 'results.html', context)

def open_pop_up(request):
    pop_up_model = request.GET.get('model') # Retrieve the data from the request
    print(pop_up_model)
    if pop_up_model == '0': # Register One
        return render(request, 'popup/register_popup.html')
    elif pop_up_model == '1': # Login One
        return render(request, 'popup/login_popup.html')
    elif pop_up_model == '4': # Complement
        return render(request, "popup/complementInfo_popup_pcd_start.html")
    # if request.method =='post':
    return #Just Placeholder

def next_step(request): 
    # pcd = 1 => Is PCD
    # pcd = 0 => Not PCD
    userType = request.GET.get('pcd')
    nextStep = request.GET.get('step')
    if nextStep == "2": # DAM
        return render(request, 'popup/complementInfo_dam_type.html')
    elif nextStep == "3":
        if userType == "1": # The condition type
            return render(request, 'popup/complementInfo_condition_type.html') 
        return render(request, 'popup/complementInfo_tag_preference.html') # TAGS if not pcd
    elif nextStep == "4" and userType == "1":
        return render(request, 'popup/complementInfo_tag_preference.html') # TAGS
    else:
        return HttpResponse("Realizar Cadastro")

@login_required
def user_display(request):
    usuario = request.user  # Obtém o usuário logado
    preferencias_locais = PreferenciaLocais.objects.filter(user=usuario)
    preferencias_recursos = PreferenciaRecursos.objects.filter(user=usuario)

    locais_unicos = set()
    locais_preferidos = []
    for preferencia in preferencias_locais:
        if preferencia.local not in locais_unicos:
            locais_unicos.add(preferencia.local)
            locais_preferidos.append(preferencia)

    recursos_unicos = set()
    recursos_preferidos = []
    for preferencia in preferencias_recursos:
        if preferencia.recurso not in recursos_unicos:
            recursos_unicos.add(preferencia.recurso)
            recursos_preferidos.append(preferencia)

    context = {
        'usuario': usuario,
        'preferencias_locais': locais_preferidos,
        'preferencias_recursos': recursos_preferidos,
    }

    return render(request, 'profile.html', context)

def about(request):
    return render(request, 'about.html')