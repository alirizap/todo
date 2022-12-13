from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.forms import UserCreationForm, UserChangeForm
from user.models import User


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ["username", "email", "is_staff", "is_active"]
    list_filter = ["username", "email", "is_staff", "is_active"]
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )

    search_fields = ["username", "email"]
    ordering = ["username", "email"]


admin.site.register(User, UserAdmin)
