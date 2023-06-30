from django.urls import path
from myapp import views

urlpatterns = [
    path('api/myapp/', views.users_list),
]
