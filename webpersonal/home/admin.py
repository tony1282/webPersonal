from django.contrib import admin  # type: ignore
from .models import Proyect

@admin.register(Proyect)
class ProyectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")