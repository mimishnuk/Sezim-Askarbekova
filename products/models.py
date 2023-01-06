from django.db import models
from django.contrib.auth.models import User

class Categori(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    discription = models.TextField()
    rate = models.FloatField()
    image = models.ImageField(blank=True, null=True)
    created_date = models.DateField(auto_now_add =True)
    modified_date = models.DateField(auto_now=True)
    categori = models.ForeignKey(Categori, on_delete=models.CASCADE, null=True)
    commentable = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='review')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
