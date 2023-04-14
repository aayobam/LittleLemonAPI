from django.db import models

from api.common.models import TimeStampedModel
from api.orders.models import Order
from api.menuitems.models import MenuItem



class OrderItem(TimeStampedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('order', 'menuitem')

