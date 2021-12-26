from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
  def test_create_user_with_email_successful(self):
    """Creating a new use with email is successful"""
    email = 'test@kula.com'
    password = "testpass123"
    user = get_user_model().objects.create_user(email=email,password=password)

    self.assertEqual(user.email, email)
    self.assertTrue(user.check_password(password))

  def test_new_user_email_normalized(self):
    """Test the email for a new user is normalized"""
    email = 'test@KuLa.CoM'
    user = get_user_model().objects.create_user(email, 'test123')
    
    self.assertEqual(user.email, 'test@kula.com')