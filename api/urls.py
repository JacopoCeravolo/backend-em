from django.urls import path
from .views import StartupCreate, StartupDelete
from . import views

urlpatterns = [
    path('startup/', StartupCreate.as_view(), name='startup-list-create'),
    path('startup/delete/<int:pk>/', StartupDelete.as_view(), name='startup-retrieve-update-destroy'),
    path('', views.getRoutes),
    path('startup/', StartupCreate.as_view(), name='startup-list-create'),
    path('startup/delete/<int:pk>/', StartupDelete.as_view(), name='startup-retrieve-update-destroy'),
    path('investor/', StartupCreate.as_view(), name='startup-list-create'),
    path('investor/delete/<int:pk>/', StartupDelete.as_view(), name='startup-retrieve-update-destroy'),
]