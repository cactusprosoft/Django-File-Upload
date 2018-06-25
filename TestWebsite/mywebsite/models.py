from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    us_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    dp = models.ImageField(upload_to='mywebsite/images/',
                           default='mywebsite/images/no-image.jpg')

    def __str__(self):
        return self.us_id
