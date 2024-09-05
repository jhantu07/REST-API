# phonebook_api/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Phonebook API")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('contacts.urls')),  # Adjust based on your API urls
    path('', index),  # Root URL
]
