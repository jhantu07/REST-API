# phonebook_api/contacts/management/commands/populate_test_data.py

from django.core.management.base import BaseCommand
from contacts.models import User, Contact
from django.contrib.auth.hashers import make_password
import random
from faker import Faker

class Command(BaseCommand):
    help = 'Populates the database with test data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create test users
        for _ in range(10):
            user = User(
                username=fake.user_name(),
                email=fake.email(),
                password=make_password('testpassword'),  # You can use a hashed password
                phone_number=fake.phone_number()
            )
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Created user: {user.username}'))

            # Create test contacts for each user
            for _ in range(5):
                contact = Contact(
                    user=user,
                    contact_name=fake.name(),
                    phone_number=fake.phone_number(),
                    is_spam=random.choice([True, False])
                )
                contact.save()
                self.stdout.write(self.style.SUCCESS(f'Created contact: {contact.contact_name}'))
