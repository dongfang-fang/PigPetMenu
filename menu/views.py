
from rest_framework import viewsets, filters

from PigPetMenu.filter import BaseFilterBackend
from PigPetMenu.pagination import BasePagination
from menu.models import Menu
from menu.serializers import MenuSerializer


class MenuView(viewsets.ModelViewSet):
    pagination_class = BasePagination
    filter_backends = (BaseFilterBackend, filters.OrderingFilter)
    ordering_fields = ["id"]
    serializer_class = MenuSerializer
    queryset = Menu.objects.filter(delete_flat=False)