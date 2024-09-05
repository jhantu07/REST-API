# contacts/management/commands/populate_db.py

from django.core.management.base import BaseCommand
from contacts.models import User, Contact
from faker import Faker

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create sample users
        for _ in range(10):
            User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123',  # Use a secure password in production
                phone_number=fake.phone_number()
            )

        # Create sample contacts for each user
        users = User.objects.all()
        for user in users:
            for _ in range(5):
                Contact.objects.create(
                    user=user,
                    contact_name=fake.name(),
                    phone_number=fake.phone_number(),
                    is_spam=fake.boolean()
                )

        self.stdout.write(self.style.SUCCESS('Database populated successfully'))
