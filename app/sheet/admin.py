from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import SalesManager, SalesBranch, Csv


admin.site.register(Csv)


@admin.register(SalesManager)
class SalesManagerAdmin(admin.ModelAdmin):
    list_display = [
        "last_name",
        "first_name",
        "area",
        "id_number",
        "id",
    ]
    list_filter = ["is_active", "area", "position"]
    search_fields = ["last_name", "first_name", "area"]


@admin.register(SalesBranch)
class SalesBranchAdmin(admin.ModelAdmin):
    list_display = [
        "short_name",
        "full_name",
    ]
    list_filter = [
        "short_name",
        "full_name",
    ]
    search_fields = [
        "short_name",
        "full_name",
    ]
