from django.db import models

# Create your models here.
class User(models.Model):
  email = models.EmailField()
  username = models.CharField(max_length=60)
  dateBirth = models.DateField()
  password = models.CharField(max_length=40)