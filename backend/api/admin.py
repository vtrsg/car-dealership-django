from django.contrib import admin

from .models import Brand, Year


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ('year',)
