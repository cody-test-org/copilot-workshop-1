from django.db import models

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    age = models.IntegerField()
    
    class Meta:
        db_table = 'cats'
