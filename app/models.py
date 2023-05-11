from django.db import models

from accounts.models import Customer

from picklefield.fields import PickledObjectField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    price2 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    # matn
    description = models.TextField(max_length=300, null=True)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    # review = PickledObjectField(null=True, blank=True)
    review = ''
    images = models.FileField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str_(self):
        return self.name


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    products = []


