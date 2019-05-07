from django.test import TestCase
from django.contrib.auth.models import User
from coolname import generate_slug

# Create your tests here.
class AliasTest(TestCase):
    
    def test_unique_alias(self):
        alias_1 = generate_slug(3)
        alias_2 = generate_slug(3)

        self.assertNotEquals(alias_1, alias_2)

class LoginTest(TestCase):

    def test_login(self):
        client_user = auth.get_user(self.client)
        self.assertEqual(client_user, user)