from django.urls import path
from .views import all_emails, send_emails, check_mailboxes

app_name = "manymailbox"

urlpatterns = [
    path("check-emails/", check_mailboxes, name="check_emails"),
    path("all-emails/", all_emails, name="all_emails"),
    path("send-emails/", send_emails, name="send_emails"),
]
