from api.menuitems.models import MenuItem
from django_filters.rest_framework import FilterSet


class MenuItemFilter(FilterSet):
    class Meta:
        model = MenuItem
        fields = {"category__title": ["iexact"], "price": ["gt", "lt"]}