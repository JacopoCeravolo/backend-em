from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from api.serializers import StartupSerializer, InvestorSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from matcher.utils import main_matching_algo_inv, main_matching_algo_stp

from .models import Startup, Investor


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/startup/create',
        'api/startup/delete/<int:pk>/',
    

    ]
    return Response(routes)

from rest_framework import generics
from .models import (
    Startup, 
    StartupDetails, 
    StartupOffering, 
    StartupFinancials, 
    StartupImpact, 
    StartupTeam, 
    StartupMarket, 
    StartupMatchingPreferences
)
from .serializers import (
    StartupSerializer, 
    StartupDetailsSerializer, 
    StartupOfferingSerializer, 
    StartupFinancialsSerializer, 
    StartupImpactSerializer, 
    StartupTeamSerializer, 
    StartupMarketSerializer, 
    StartupMatchingPreferencesSerializer
)

class StartupRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.startup

class StartupCreateView(generics.CreateAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        startup = serializer.save()  
        user.startup = startup  
        user.save()
    

class StartupDetailsView(generics.RetrieveUpdateAPIView):
    queryset = StartupDetails.objects.all()
    serializer_class = StartupDetailsSerializer

    def get_object(self):
        return self.request.user.startup.details

class StartupOfferingView(generics.RetrieveUpdateAPIView):
    queryset = StartupOffering.objects.all()
    serializer_class = StartupOfferingSerializer

    def get_object(self):
        return self.request.user.startup.offerings

class StartupFinancialsView(generics.RetrieveUpdateAPIView):
    queryset = StartupFinancials.objects.all()
    serializer_class = StartupFinancialsSerializer

    def get_object(self):
        return self.request.user.startup.financials

class StartupImpactView(generics.RetrieveUpdateAPIView):
    queryset = StartupImpact.objects.all()
    serializer_class = StartupImpactSerializer

    def get_object(self):
        return self.request.user.startup.impact

class StartupTeamView(generics.RetrieveUpdateAPIView):
    queryset = StartupTeam.objects.all()
    serializer_class = StartupTeamSerializer

    def get_object(self):
        return self.request.user.startup.team

class StartupMarketView(generics.RetrieveUpdateAPIView):
    queryset = StartupMarket.objects.all()
    serializer_class = StartupMarketSerializer

    def get_object(self):
        return self.request.user.startup.market

class StartupPreferencesView(generics.RetrieveUpdateAPIView):
    queryset = StartupMatchingPreferences.objects.all()
    serializer_class = StartupMatchingPreferencesSerializer

    def get_object(self):
        return self.request.user.startup.preferences


#api/startup/
""" class StartupCreate(generics.ListCreateAPIView):
    serializer_class = StartupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Startup.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        main_matching_algo_stp(startup=Startup.objects.filter(user=self.request.user)[0]) """

from .models import Investor, InvestorPreferences, InvestorPortfolio
from .serializers import InvestorSerializer, InvestorPreferencesSerializer, InvestorPortfolioSerializer

class InvestorRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.investor

class InvestorCreateView(generics.CreateAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        investor = serializer.save()  
        user.investor = investor  
        user.save()

class InvestorPreferencesView(generics.RetrieveUpdateAPIView):
    queryset = InvestorPreferences.objects.all()
    serializer_class = InvestorPreferencesSerializer

    def get_object(self):
        return self.request.user.investor.preferences

class InvestorPortfolioView(generics.RetrieveUpdateAPIView):
    queryset = InvestorPortfolio.objects.all()
    serializer_class = InvestorPortfolioSerializer

    def get_object(self):
        return self.request.user.investor.portfolio
    
from django.shortcuts import render

def profile(request):
    return render(request, 'profile.html')