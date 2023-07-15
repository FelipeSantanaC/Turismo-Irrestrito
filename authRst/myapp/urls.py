from django.urls import path
from myapp import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('results/', views.results, name ='results'),
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('api/myapp/user/', views.users_list, name='user_list'),
    path('api/myapp/results/', views.results, name='results'),
    path('home/', views.home, name='home'),
    path('logout', views.logout_view, name='logout'),
    #Reset Password
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]   
    
