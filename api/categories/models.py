from curses import savetty
from django.urls import reverse
from django.db import models
from api.common.models import TimeStampedModel
from django.utils.text import slugify


class Category(TimeStampedModel):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"id": self.id})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    