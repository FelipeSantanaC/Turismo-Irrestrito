from django.urls import path, re_path, include
from myapp import views
from django.contrib import admin

urlpatterns = [
    path('results/', views.results, name='results'),
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('home/', views.home, name='home'),
    path('logout', views.logout_view, name='logout'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_register/', views.user_register, name='user_register'),
    path('popup/', views.open_pop_up, name='open_pop_up'),
    path('nextWizard/', views.next_step, name='next_step'),
    path('comp/', views.complementar_register, name='complementar_register'),
    path('user_display/', views.user_display, name='user_display'),
    path('about/', views.about, name='about'),
    path('local/<int:local_id>', views.local_detail, name="local_detail"),
]   

