from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import (
    DestinationInbox,
    Mailbox,
    RecievedMail,
)


@admin.register(DestinationInbox)
class DestinationInboxesAdmin(admin.ModelAdmin):
    list_display = ["id", "company", "email"]
    list_filter = ["company", "email"]
    search_fields = ["company", "email"]


@admin.register(Mailbox)
class MailboxAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "server", "email_user"]
    list_filter = ["name", "server", "email_user"]
    search_fields = ["name", "server", "email_user"]


@admin.register(RecievedMail)
class RecievedMailAdmin(admin.ModelAdmin):
    list_display = [
        "email_sender",
        "email_receiver",
        "send_date",
        "subject",
        "save_to_db_date",
        "email_body",
        "email_uidl",
        "is_forwarded",
    ]
    list_filter = ["email_sender", "email_receiver", "is_forwarded"]
    search_fields = [
        "email_sender",
        "email_receiver",
        "subject",
        "email_body",
        "email_uidl",
    ]
