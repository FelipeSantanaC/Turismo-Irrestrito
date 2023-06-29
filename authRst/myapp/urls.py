from django.urls import path
from myapp import views

urlpatterns = [
    path('api/myapp/', views.tutorial_list),
    #path('api/myapp/<int:pk>/', views.myapp_detail),
    #path('api/myapp/published/', views.myapp_list_published)
]
