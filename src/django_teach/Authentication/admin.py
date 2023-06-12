from django.contrib import admin

from . import models


@admin.register(models.UserModel)
class CarModelAdmin(admin.ModelAdmin):
    all_fields = [field.name for field in models.UserModel._meta.fields]
    list_display = all_fields
    list_filter = all_fields
    search_fields = all_fields
    fields = all_fields
    readonly_fields = ('id',)
    ordering = all_fields
