from django.urls import path
from . import views


urlpatterns = [
    path('', views.recipes_list),
    path('<pk>/', views.recipes_detail),
]