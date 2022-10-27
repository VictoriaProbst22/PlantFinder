from django.urls import path
from . import views


urlpatterns = [
    path('', views.recipes_list),
    path('<int:pk>/', views.recipes_detail),
]