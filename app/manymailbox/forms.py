from django.forms import ModelForm

from .models import Mailbox


class MailboxForm(ModelForm):
    class Meta:
        model = Mailbox
        fields = [
            "name",
            "server",
            "port",
            "email_user",
            "email_password",
        ]
        labels = {
            "name": "Nazwa Skrzynki",
            "server": "Serwer pocztowy",
            "port": "Port",
            "email_user": "Adres email",
            "email_password": "hasło do skrzynki",
        }
