from django.db import models
from django.db.models.deletion import CASCADE
class books(models.Model):
    name=models.CharField(max_length=30)
    price=models.PositiveIntegerField()
    def __str__(self):
        return self.name
class author(models.Model):
    book=models.ForeignKey(books,on_delete=CASCADE)
    authorname=models.CharField(max_length=30)
    img=models.ImageField(upload_to='photo')
    def __str__(self):
        return self.authorname