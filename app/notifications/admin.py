from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Msg

# Register your models here.


@admin.register(Msg)
class GroupAdmin(ModelAdmin):
    pass
