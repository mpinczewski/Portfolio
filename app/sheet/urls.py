from django.urls import path
from .views import (
    add_sales_manager,
    all_traders,
    delete_sales_manager,
    edit_sales_manager,
    specific_trader,
    find_trader,
    find_trader_dok,
    upload_sales_branch_view,
    upload_sales_manager_view,
)

app_name = "sheet"

urlpatterns = [
    path("csv/", upload_sales_manager_view, name="upload_view"),
    path("csv-branches/", upload_sales_branch_view, name="upload_sales_branch_view"),
    path("all-traders/", all_traders, name="all_traders"),
    path("submit/", find_trader, name="submit"),
    path("submit/<int:pk>/", specific_trader, name="specific_trader"),
    path("submit-dok/", find_trader_dok, name="submit_dok"),
    path("add-sales-manager/", add_sales_manager, name="add_sales_manager"),
    path(
        "add-sales-manager/<int:id_number>/",
        edit_sales_manager,
        name="edit_sales_manager",
    ),
    path(
        "delete-sales-manager/<int:id_number>/",
        delete_sales_manager,
        name="delete_sales_manager",
    ),
]
