from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import Textarea

from .models import Brand, User, Year


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = (
        'email',
        'user_name',
        'first_name',
    )
    list_filter = (
        'email',
        'user_name',
        'first_name',
        'is_active',
        'is_staff',
        'cpf',
        'phone',
    )
    ordering = ('-start_date',)
    list_display = (
        'id',
        'email',
        'user_name',
        'first_name',
        'is_active',
        'is_staff',
        'cpf',
        'phone',
    )
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'email',
                    'user_name',
                    'first_name',
                )
            },
        ),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'user_name',
                    'first_name',
                    'password1',
                    'password2',
                    'is_active',
                    'is_staff',
                    'cpf',
                    'phone',
                ),
            },
        ),
    )


admin.site.register(User, UserAdminConfig)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ('year',)
