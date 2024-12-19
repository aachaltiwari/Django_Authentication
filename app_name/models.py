from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # this user model already consists fields like username, email, password, first_name, last_name, and probably other fields
    # we will add additional fields to this model as per our requirements
    phone_number = models.CharField(max_length = 255)