from django.db import models

from .CustomUser import CustomUser
from .Category import Category
from .DataField import DataField
from django.contrib.postgres.fields import ArrayField


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    datafield = models.ManyToManyField(DataField, related_name='product')
    price = models.IntegerField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    pics = ArrayField(models.CharField(max_length=127))
    destination = models.TextField(blank=True, null=True, )
    status = models.BooleanField(default=False,blank=True)
