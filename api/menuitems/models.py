from django.db import models
from django.urls import reverse
from api.categories.models import Category
from api.common.models import TimeStampedModel


class MenuItem(TimeStampedModel):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("menuitem_detail", kwargs={"id": self.id})
    

