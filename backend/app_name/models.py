from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # this user model already consists fields like username, email, password, first_name, last_name, and probably other fields
    # we will add additional fields to this model as per our requirements
    phone_number = models.CharField(max_length = 255)
    
    
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title