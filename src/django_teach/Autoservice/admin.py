from django.contrib import admin
from Autoservice import models


@admin.register(models.CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.CarModel._meta.fields]
    list_filter = [field.name for field in models.CarModel._meta.fields]
    search_fields = [field.name for field in models.CarModel._meta.fields]
    fields = [field.name for field in models.CarModel._meta.fields]
    readonly_fields = ('id', 'is_active', 'created_at', 'updated_at')
    ordering = [field.name for field in models.CarModel._meta.fields]
    pass


class PreferredParametersModelAdmin(admin.StackedInline):
    model = models.PreferredCarParametersModel


@admin.register(models.AutoserviceModel)
class AutoserviceModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.AutoserviceModel._meta.fields]
    list_filter = [field.name for field in models.AutoserviceModel._meta.fields]
    search_fields = [field.name for field in models.AutoserviceModel._meta.fields]
    fields = [field.name for field in models.AutoserviceModel._meta.fields]
    readonly_fields = ('id', 'is_active', 'created_at', 'updated_at')
    ordering = [field.name for field in models.AutoserviceModel._meta.fields]

    inlines = [PreferredParametersModelAdmin]


@admin.register(models.PreferredCarParametersModel)
class AutoserviceModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.PreferredCarParametersModel._meta.fields]
    list_filter = [field.name for field in models.PreferredCarParametersModel._meta.fields]
    search_fields = [field.name for field in models.PreferredCarParametersModel._meta.fields]
    fields = [field.name for field in models.PreferredCarParametersModel._meta.fields]
    readonly_fields = ('id',)
    ordering = [field.name for field in models.PreferredCarParametersModel._meta.fields]




