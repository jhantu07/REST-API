# populate_contacts.py
import os
import django

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phonebook_api.settings')
django.setup()

from contacts.models import Contact

# List all contacts
contacts = Contact.objects.all()
for contact in contacts:
    print(f"Contact Name: {contact.contact_name}, Phone Number: {contact.phone_number}, Is Spam: {contact.is_spam}")
