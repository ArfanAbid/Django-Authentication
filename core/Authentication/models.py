from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Authentication_user(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL ,blank=True, null=True)
