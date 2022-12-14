from django.test import TestCase
from category.models import Category


class CategoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(
            name="Shopping"
        )

    def test_category_model(self):
        self.assertEqual(self.category.name, "Shopping")
        self.assertEqual(str(self.category), "Shopping")
