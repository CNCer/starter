
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from concurrency.admin import ConcurrencyListEditableMixin, ConcurrencyActionMixin, ConcurrentModelAdmin

admin.site.unregister(Group)

# Register your models here.


@admin.register(User)
class UserAdmin(  BaseUserAdmin, ModelAdmin, ConcurrentModelAdmin, TabbedTranslationAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    fieldsets = (
            (None, {"fields": ("username", "password", "user_version")}),
            ("Personal info", {"fields": ("first_name", "last_name", "email")}),
            (
                "Permissions",
                {
                    "fields": (
                        "is_active",
                        "is_staff",
                        "is_superuser",
                        "groups",
                        "user_permissions",
                    ),
                },
            ),
            ("Important dates", {"fields": ("last_login", "date_joined")}),
        )


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin, ConcurrencyListEditableMixin, ConcurrencyActionMixin):
    pass

@admin.register(Profile)
class ProfileAdmin( ConcurrencyListEditableMixin, ConcurrencyActionMixin, ModelAdmin):
    pass
