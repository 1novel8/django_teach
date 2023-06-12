from django.contrib import admin

from Autoservice import models


@admin.register(models.CarModel)
class CarModelAdmin(admin.ModelAdmin):
    all_fields = [field.name for field in models.CarModel._meta.fields]
    list_display = all_fields
    list_filter = all_fields
    search_fields = all_fields
    fields = all_fields
    readonly_fields = ('id', 'is_active', 'created_at', 'updated_at')
    ordering = all_fields


class AutoserviceRegularCustomersInline(admin.StackedInline):
    model = models.AutoserviceRegularCustomers


@admin.register(models.AutoserviceRegularCustomers)
class AutoserviceRegularCustomersAdmin(admin.ModelAdmin):
    all_fields = [field.name for field in models.AutoserviceRegularCustomers._meta.fields]
    list_display = all_fields
    list_filter = all_fields
    search_fields = all_fields
    fields = all_fields
    readonly_fields = ('id', 'is_active', 'created_at', 'updated_at')
    ordering = all_fields


class PreferredParametersModelInline(admin.StackedInline):
    model = models.PreferredCarParametersModel


@admin.register(models.AutoserviceModel)
class AutoserviceModelAdmin(admin.ModelAdmin):
    all_fields = [field.name for field in models.AutoserviceModel._meta.fields]
    list_display = all_fields
    list_filter = all_fields
    search_fields = all_fields
    fields = all_fields
    readonly_fields = ('id', 'is_active', 'created_at', 'updated_at')
    ordering = all_fields

    inlines = [PreferredParametersModelInline, AutoserviceRegularCustomersInline]


@admin.register(models.PreferredCarParametersModel)
class PreferredCarParametersModelAdmin(admin.ModelAdmin):
    all_fields = [field.name for field in models.PreferredCarParametersModel._meta.fields]
    list_display = all_fields
    list_filter = all_fields
    search_fields = all_fields
    fields = all_fields
    readonly_fields = ('id',)
    ordering = all_fields




