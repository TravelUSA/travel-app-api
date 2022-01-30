from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email = 'test@travelusa.com', password='testpass'):
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_create_user_with_email_succesful(self):
        email = 'abc@test.com'
        password = 'pass123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        "Test the email for a new user is normalized"
        email = 'abc@TEST.COM'
        user = get_user_model().objects.create_user(email,'test1232')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        "Test the user enters VALID email"
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        "Test creating a super uswer"
        user = get_user_model().objects.create_superuser(
            'super@test.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user =sample_user(),
            name = 'Vegan'
        )
        self.assertEqual(str(tag), tag.name)