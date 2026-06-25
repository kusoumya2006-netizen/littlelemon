from django.test import TestCase
from .models import Menu

class MenuTest(TestCase):

    def test_create_menu(self):
        item = Menu.objects.create(
            title="Pizza",
            price=10.99,
            inventory=5
        )
        self.assertEqual(item.title, "Pizza")