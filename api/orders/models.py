from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from api.common.models import TimeStampedModel

class Order(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='delivery_crew', null=True)
    status = models.BooleanField(default=0, db_index=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order with {self.id}"
    
    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"order_id": self.id})
    
