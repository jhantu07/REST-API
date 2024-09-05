# contacts/tests/test_models.py

from django.test import TestCase
from models import User, Contact

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpassword')

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

class ContactModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.contact = Contact.objects.create(user=self.user, phone_number='1234567890')

    def test_contact_creation(self):
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.get().phone_number, '1234567890')
