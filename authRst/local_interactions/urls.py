from django.urls import path
from . import views

urlpatterns = [
    path('get_posts/<int:local_id>/', views.get_posts_by_local, name='get_posts_by_local'),
    path('local_rate/', views.local_rate, name='local_rate'),
]