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
    model = models.AutoserviceRegularCustomersModel


class PreferredParametersModelInline(admin.StackedInline):
    model = models.PreferredCarParametersModel


class AutoserviceCarCatalogModelInline(admin.StackedInline):
    model = models.AutoserviceCarCatalogModel


class AutoserviceSaleHistoryInline(admin.StackedInline):
    model = models.AutoserviceSaleHistoryModel


@admin.register(models.AutoserviceRegularCustomersModel)
class AutoserviceRegularCustomersAdmin(admin.ModelAdmin):
    all_fields = [field.name for field in models.AutoserviceRegularCustomersModel._meta.fields]
    list_display = all_fields
    list_filter = all_fields
    search_fields = all_fields
    fields = all_fields
    readonly_fields = ('id', 'is_active', 'created_at', 'updated_at')
    ordering = all_fields


@admin.register(models.AutoserviceModel)
class AutoserviceModelAdmin(admin.ModelAdmin):
    all_fields = [field.name for field in models.AutoserviceModel._meta.fields]
    list_display = all_fields
    list_filter = all_fields
    search_fields = all_fields
    fields = all_fields
    readonly_fields = ('id', 'is_active', 'created_at', 'updated_at')
    ordering = all_fields

    inlines = [
        PreferredParametersModelInline,
        AutoserviceRegularCustomersInline,
        AutoserviceCarCatalogModelInline,
        AutoserviceSaleHistoryInline,
    ]


@admin.register(models.PreferredCarParametersModel)
class PreferredCarParametersModelAdmin(admin.ModelAdmin):
    all_fields = [field.name for field in models.PreferredCarParametersModel._meta.fields]
    list_display = all_fields
    list_filter = all_fields
    search_fields = all_fields
    fields = all_fields
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = all_fields


@admin.register(models.AutoserviceCarCatalogModel)
class AutoserviceCarCatalogAdmin(admin.ModelAdmin):
    all_fields = [field.name for field in models.AutoserviceCarCatalogModel._meta.fields]
    list_display = all_fields
    list_filter = all_fields
    search_fields = all_fields
    fields = all_fields
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = all_fields


@admin.register(models.AutoserviceSaleHistoryModel)
class AutoserviceSaleHistoryAdmin(admin.ModelAdmin):
    all_fields = [field.name for field in models.AutoserviceSaleHistoryModel._meta.fields]
    list_display = all_fields
    list_filter = all_fields
    search_fields = all_fields
    fields = all_fields
    readonly_fields = ('id', 'date_of_sale')
    ordering = all_fields
