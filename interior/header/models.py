from django.db import models

# Create your models here.
class Partners(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField()

class Services(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField()
    description = models.CharField(max_length=100)

class Employees(models.Model):
    name = models.CharField(max_length=100)
    foto = models.ImageField()
    position = models.TextField()

class News(models.Model):
    title = models.CharField(max_length=100)
    foto = models.ImageField()
    author = models.ForeignKey(Partners, on_delete=models.CASCADE)
    created_by = models.DateTimeField(auto_now_add=True)














