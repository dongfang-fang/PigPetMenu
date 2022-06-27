from django.urls import path, include


from rest_framework import routers

from menu.views import MenuView

router = routers.DefaultRouter()

router.register(r"menus", MenuView, basename="menus")

urlpatterns = [
    path("", include(router.urls)),
]
