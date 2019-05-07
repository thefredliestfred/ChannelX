from django.test import TestCase
from django.contrib.auth.models import User
from coolname import generate_slug

# Create your tests here.
class AliasTest(TestCase):
    
    def test_unique_alias(self):
        alias_1 = generate_slug(3)
        alias_2 = generate_slug(3)

        self.assertNotEquals(alias_1, alias_2)