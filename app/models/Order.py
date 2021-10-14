from django.db import models
from django.contrib.auth.models import User

from app.models.CustomUser import CustomUser
from app.models.Product import Product


class Order(models.Model):
    DELIVERED_SUCCESS = 'deliver'
    DELIVERED_UN_SUCCESS = 'un_deliver'
    DELIVERED_REJECT = 'reject_deliver'

    DELIVER_CHOICES = (
        (DELIVERED_SUCCESS, 'deliver'),
        (DELIVERED_UN_SUCCESS, 'un_deliver'),
        (DELIVERED_REJECT, 'reject_deliver')
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    deliver_status = models.CharField(max_length=50, choices=DELIVER_CHOICES)  # -> choices
    location = models.TextField  # {type:addrees,lat:2.12123,lang:32123} {type:text,text:"sergeli 3 dom korzinka yoni"}
    created_at = models.DateTimeField(auto_now_add=True)  # 17:00 10-october
    updated_at = models.DateTimeField(auto_now_add=True)  # 12:30  11-october
    deliverd_time = models.DateTimeField()  # when must deliver product
