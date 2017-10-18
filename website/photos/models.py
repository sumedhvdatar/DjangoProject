from django.db import models

# # Create your models here.
#
class AppUsers(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    permission = models.PositiveSmallIntegerField(max_length=10)

class Photos(models.Model):
    photo_url = models.CharField(max_length=500)

