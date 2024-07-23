from django.db import models

# Create your models here.
class Rest_list(models.Model):
  restaurant_name = models.CharField(max_length=255)
  type = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  def __str__(self):
      return f"{self.restaurant_name} {self.type} {self.address}"
class rest_users(models.Model):
    model = Rest_list
    fields = ['username', 'email', 'password1', 'password2']
