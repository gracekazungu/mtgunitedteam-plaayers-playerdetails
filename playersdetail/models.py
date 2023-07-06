from django.db import models

# Create your models here.
class Player(models.Model):
    firstName=models.CharField(max_length=32)
    secondName=models.CharField(max_length=32)
    date_of_birth=models.DateField(max_length=16)
    image=models.ImageField()
    id_number=models.CharField(max_length=20)
    gersey_number=models.PositiveIntegerField()
    field_number=models.PositiveIntegerField()
    phone_number=models.CharField(max_length=20)
    email=models.EmailField()
    field=models.CharField(max_length=30)
    division=models.CharField(max_length=30)


    