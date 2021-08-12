from django.urls import path
from .views import access_denied, add_mailbox, all_mailboxes, delete_mailbox, edit_mailbox, all_emails, send_emails, check_mailboxes

app_name = "manymailbox"

urlpatterns = [
    path("check-emails/", check_mailboxes, name="check_emails"),
    path("all-emails/", all_emails, name="all_emails"),
    path("send-emails/", send_emails, name="send_emails"),
    path("access-denied/", access_denied, name="access_denied"),
    path("all-mailboxes/", all_mailboxes, name="all_mailboxes"),
    path("add-mailbox/", add_mailbox, name="add_mailbox"),
    path("add-mailbox/<int:id>/", edit_mailbox, name="edit_mailbox"),
    path("delete-mailbox/<int:id>/", delete_mailbox, name="delete_mailbox"),
]
