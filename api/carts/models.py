from decimal import Decimal
from django.db import models
from api.menuitems.models import MenuItem
from django.contrib.auth.models import User
from api.common.models import TimeStampedModel


class Cart(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ['user', 'menuitem']

    def __str__(self) -> str:
        return self.menuitem.title
    
    def save(self, *args, **kwargs):
        self.unit_price = self.menuitem.price
        price = self.unit_price * self.quantity
        self.price = Decimal(price)
        return super().save(*args, **kwargs)
