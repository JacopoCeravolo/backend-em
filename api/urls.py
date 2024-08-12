from django.urls import path
from .views import StartupCreate, StartupDelete, InvestorCreate, InvestorDelete
from . import views

urlpatterns = [
    path('startup/', StartupCreate.as_view(), name='startup-list-create'),
    path('startup/delete/<int:pk>/', StartupDelete.as_view(), name='startup-retrieve-update-destroy'),
    path('', views.getRoutes),
    path('startup/delete/<int:pk>/', StartupDelete.as_view(), name='startup-retrieve-update-destroy'),
    path('investor/', InvestorCreate.as_view(), name='startup-list-create'),
    path('investor/delete/<int:pk>/', InvestorDelete.as_view(), name='startup-retrieve-update-destroy'),
]