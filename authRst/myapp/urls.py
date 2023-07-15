from django.urls import path
from myapp import views
from django.contrib import admin

urlpatterns = [
    path('results/', views.results, name ='results'),
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('api/myapp/user/', views.users_list, name='user_list'),
    path('home/', views.home, name='home'),
    path('logout', views.logout_view, name='logout'),
    path('user_login', views.user_login, name='user_login'),
]   

