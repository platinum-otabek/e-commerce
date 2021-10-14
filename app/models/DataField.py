from django.db import models


class DataField(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name
