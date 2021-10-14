from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, default=None, blank=True, null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
