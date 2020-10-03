
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    cname=models.CharField(max_length=30)

    def __str__(s):
        return s.cname