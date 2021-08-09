from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sheet/", include("sheet.urls", namespace="sheet")),
    path("manymailbox/", include("manymailbox.urls", namespace="manmailbox")),
]
