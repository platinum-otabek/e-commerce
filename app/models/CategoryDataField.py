from django.db import models

from app.models.Category import Category
from app.models.DataField import DataField


class CategoryDataField(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    datafield = models.ForeignKey(DataField, on_delete=models.CASCADE)

