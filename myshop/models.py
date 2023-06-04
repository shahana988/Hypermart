from django.db import models

# Create your models here.
class admindb(models.Model):
    name = models.CharField(max_length=50, null=True , blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=50,null=True, blank=True)
    username = models.CharField(max_length=50, null=True , blank=True)
    password = models.CharField(max_length=10, null=True, blank=True)
    image = models.ImageField(upload_to="profile", null=True, blank=True)

class catdb(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=160, null=True, blank=True)
    image = models.ImageField(upload_to="profile", null=True, blank=True)


class prodb(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.CharField(max_length=50,null=True,blank=True)
    quantity = models.IntegerField()
    description = models.TextField(max_length=160, null=True, blank=True)
    category = models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField(upload_to="profile", null=True, blank=True)

class logdb(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=10,null=True,blank=True)