
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

admin.site.unregister(Group)

# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin, TabbedTranslationAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

@admin.register(Profile)
class CustomAdminClass( ModelAdmin):
    pass
