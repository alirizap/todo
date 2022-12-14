from django.test import TestCase
from user.models import User 


class UserTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.normal_user = User.objects.create(
            username="normaluser",
            email="normal@user.com",
            password="normaluserpassword"
        )

        cls.staff_user = User(
            username="staffuser",
            email="staff@user.com",
            password="staffuserpassword"
        )

        cls.staff_user.is_staff = True 
        cls.staff_user.save()

    def test_user_model(self):
        self.assertEqual(self.normal_user.username, "normaluser")
        self.assertEqual(self.normal_user.email, "normal@user.com")
        self.assertTrue(self.normal_user.is_active)
        self.assertFalse(self.normal_user.is_staff)
        self.assertFalse(self.normal_user.is_superuser)

        self.assertEqual(self.staff_user.username, "staffuser")
        self.assertEqual(self.staff_user.email, "staff@user.com")
        self.assertTrue(self.staff_user.is_active)
        self.assertTrue(self.staff_user.is_staff)
        self.assertFalse(self.staff_user.is_superuser)


