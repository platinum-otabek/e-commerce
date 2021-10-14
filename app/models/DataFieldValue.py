from django.db import models
from .DataField import DataField
from .Product import Product


class DataFieldValue(models.Model):
    datafield = models.ForeignKey(DataField, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.CharField(max_length=63)
