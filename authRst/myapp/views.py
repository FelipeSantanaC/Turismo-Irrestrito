from django.shortcuts import render, redirect

from django.http.response import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status,filters
from django.core.exceptions import ObjectDoesNotExist

from myapp.models import MyUser, Local
from myapp.serializers import UserSerializer, LocalSerializer
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .admin import UserCreationForm
from django.contrib.auth import views as auth_views


def index(request):
    form = UserCreationForm()
    
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
                return redirect('home') 
            else:
                return HttpResponse('Invalid credentials')
    
    # Render the initial page with the form
    context = {'form': form}
    return render(request, 'home.html', context=context)

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
    if request.method == 'GET':
        search_query = request.GET.get('search','')
        try:
            locals = Local.objects.filter(nome__icontains=search_query)
            local_serializer = LocalSerializer(locals, many=True)
            if len(local_serializer.data) == 0:
                context = {'mensagem': 'Nenhuma correspondência encontrada.'}
            else:
                context = {'data': local_serializer.data}
            return render(request, 'results.html', context)
        except ObjectDoesNotExist:
            context = {'mensagem': 'Nenhuma correspondência encontrada.'}
            return render(request, 'results.html', context)
    else:
        return render(request, 'results.html')