# phonebook_api/contacts/views.py

from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework import status
from .models import User, Contact
from .sers import UserSerializer, RegisterSerializer, ContactSerializer


# Register View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Login View
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid Credentials'}, status=400)

# Profile View
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

# Search View
class SearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get('query')
        if query.isdigit():
            users = User.objects.filter(phone_number__icontains=query)
        else:
            users = User.objects.filter(name__icontains=query)

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
class ReportSpamView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        phone_number = request.data.get('phone_number')
        Contact.objects.filter(phone_number=phone_number).update(is_spam=True)
        return Response({'status': 'marked as spam'})
class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

# User List View
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]