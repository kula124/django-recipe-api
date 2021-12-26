from django.test import TestCase
from django.contrib.auth import get_user, get_user_model

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
  
  def test_new_user_invalid_email(self):
    """Test creating user with no email raises error"""
    with self.assertRaises(ValueError):
      get_user_model().objects.create_user(None, 'aa')
  
  def test_create_new_superuser(self):
    """Create superuser"""
    user = get_user_model().objects.create_superuser(
      "user@super.com",
      "strongPassword"
    )

    self.assertTrue(user.is_staff)
    self.assertTrue(user.is_superuser)