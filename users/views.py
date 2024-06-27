from .models import CustomUser
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer
from .utils import Util

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated


# Create your views here.

#Login User
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#Register User
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        # Call the superclass method to create the user
        response = super().create(request, *args, **kwargs)
        
        # Get the user data from the request
        user_data = request.data
        user = CustomUser.objects.get(email=user_data['email'])

        # Generate the email body and subject
        email_body = f"Hi {user.first_name},\n\nThank you for registering. Please verify your email by clicking the link below:\n\n<verification_link>\n\nBest regards,\nYour Company"
        email_subject = 'Verify your email'

        # Prepare the email data
        data = {
            'email_body': email_body,
            'to_email': user.email,
            'email_subject': email_subject
        }

        # Send the email
        Util.send_email(data=data)

        return response

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/users/token/',
        '/users/register/',
        '/users/token/refresh/',
    ]
    return Response(routes)