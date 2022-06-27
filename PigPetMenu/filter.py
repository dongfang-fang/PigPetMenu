from django_filters.rest_framework import DjangoFilterBackend


class BaseFilterBackend(DjangoFilterBackend):
    def get_schema_fields(self, view):
        # Customize according to your need here.
        if view.action not in ["list", "retrieve"]:
            return []
        return super().get_schema_fields(view)
