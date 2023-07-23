from django.shortcuts import render, redirect

from django.http.response import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status,filters
from django.core.exceptions import ObjectDoesNotExist

from django.db.models import Max
from myapp.models import MyUser, Local, UserProfile, ListaRecursos, ListaDispositivos, TiposLocais
from myapp.serializers import UserSerializer, LocalSerializer
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .admin import UserCreationForm
from django.db.models import Q
from .forms import UserProfileForm

def index(request):
    search_query = request.GET.get('search', '')
    locals = Local.objects.filter(nome__icontains=search_query).order_by('-nota')[:10]
    local_serializer = LocalSerializer(locals, many=True)
    return render(request,'home.html',{'data': local_serializer.data})

def user_login(request):   
    if request.method == "POST":
        
        if 'register_form' in request.POST:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                # Display form errors
                errors = form.errors.as_data()
                error_messages = []
                for field, error_list in errors.items():
                    error_messages.append(f"{field}: {', '.join(error.message for error in error_list)}")
                return HttpResponse(f"Invalid form data: {', '.join(error_messages)}")
                # return HttpResponse('Invalid form data')
        
        elif 'login_form' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password1')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index') 
            else:
                return HttpResponse('Invalid credentials')


@login_required
def complementar_register(request):
    user_profile_exists = UserProfile.objects.filter(user=request.user).exists()
    if user_profile_exists:
        return HttpResponse('Você já preencheu este formulário')
    tipos_locais = TiposLocais.objects.all()
    tipos_recursos = ListaRecursos.objects.all()
    tipos_dispositivos = ListaDispositivos.objects.all()
    if request.method == 'POST':
        additional_form = UserProfileForm(request.POST)
       
        if additional_form.is_valid():
            user_profile = additional_form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('index')
    else:
        additional_form = UserProfileForm()

    return render(request, 'comp.html', context={'additional_form': additional_form, 
                                                'tipos_locais' : tipos_locais,
                                                'tipos_recursos' : tipos_recursos,
                                                'tipos_dispositivos' : tipos_dispositivos})

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

    search_query = request.GET.get('search', '')
    selected_types = request.GET.getlist('tipo')

    locals = Local.objects.all()

    if search_query:
        locals = locals.filter(Q(nome__icontains=search_query))

    for type in selected_types:
        locals = locals.filter(tipo=type)

    local_serializer = LocalSerializer(locals, many=True)
    unique_types = Local.objects.values_list('tipo', flat=True).distinct()

    context = {
        'data': local_serializer.data,
        'types': unique_types,
        'selected_types': selected_types,
        'search_query': search_query,
    }
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
