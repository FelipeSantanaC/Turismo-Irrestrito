from django.urls import path
from myapp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('api/myapp/', views.users_list, name='users_list'),
    path('login', views.login, name='login'),
    path('register_user', views.register_user, name='register_user'),
    
]   
    
