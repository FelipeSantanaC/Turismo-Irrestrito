from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('api/myapp/', views.users_list, name='users_list'),
]
    
