from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    discription = models.TextField()
    rate = models.FloatField()
    image = models.ImageField(blank=True, null=True)
    created_date = models.DateField(auto_now=True)
    modified_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
