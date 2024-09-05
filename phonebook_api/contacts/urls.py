# phonebook_api/contacts/urls.py

from django.urls import path
from .views import RegisterView, LoginView, ProfileView, SearchView,ReportSpamView ,ContactListView,UserListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('search/', SearchView.as_view(), name='search'),
    path('report_spam/', ReportSpamView.as_view(), name='report_spam'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('contacts/', ContactListView.as_view(), name='contact-list'),

]
