from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        'email', 'username', 'first_name',
        'last_name', 'is_staff', 'is_active',
    )
    list_filter = (
        'email', 'username', 'first_name',
        'last_name', 'is_staff', 'is_active',
    )
    fieldsets = (
        (
            None, {
                'fields': (
                    'email', 'password',
                    'username', 'first_name', 'last_name',
                ),
            },
        ),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'email', 'username', 'first_name', 'last_name',
                    'password1', 'password2', 'is_staff', 'is_active',
                ),
            },
        ),
    )
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
