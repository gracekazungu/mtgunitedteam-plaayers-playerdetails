from django.contrib import admin
from.models import Player

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display=("firstName","secondName","date_of_birth","image","id_number","gersey_number","field_number","phone_number","email","division","field")


admin.site.register(Player,PlayerAdmin)