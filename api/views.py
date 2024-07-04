from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from api.serializers import StartupSerializer, InvestorSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .models import Startup, Investor


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/startup/create',
        'api/startup/delete/<int:pk>/',
    

    ]
    return Response(routes)


#api/startup/
class StartupCreate(generics.ListCreateAPIView):
    serializer_class = StartupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Startup.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#api/startup/delete/<int:pk>  
class StartupDelete(generics.DestroyAPIView):
    serializer_class = StartupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Startup.objects.filter(user=user)
    
#api/investor/
class InvestorCreate(generics.ListCreateAPIView):
    serializer_class = InvestorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Investor.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#api/investor/delete/<int:pk>  
class InvestorDelete(generics.DestroyAPIView):
    serializer_class = InvestorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Investor.objects.filter(user=user)