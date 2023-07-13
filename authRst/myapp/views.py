from django.shortcuts import render, redirect

from django.http.response import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from myapp.models import MyUser
from myapp.serializers import UserSerializer
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .admin import UserCreationForm

def index(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        if 'register_form' in request.POST:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                return HttpResponse('Invalid form data')
        
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
    return render(request, 'index.html', context=context)

@login_required(login_url='login')
def home(request):
    user = request.user 

    context = {'user': user}
    return render(request, 'home.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('index')       

def register_user (requests):
    pass
            
def _login (requests):
    pass

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
    