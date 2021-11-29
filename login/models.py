from django.db import models
class login(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    FEMALE='F'
    MALE='M'
    CHOICES_GENDER=[
        ('FEMALE',FEMALE),
        ('MALE',MALE)
    ]
    gender=models.CharField(max_length=20,choices=CHOICES_GENDER)
    def __str__(self):
        return self.username

# Create your models here.
