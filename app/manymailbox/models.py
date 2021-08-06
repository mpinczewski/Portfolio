from django.db import models


class Mailbox(models.Model):
    name = models.CharField(max_length=32)
    server = models.CharField(max_length=128)
    port = models.CharField(max_length=6, null=True, blank=True)
    email_user = models.CharField(max_length=128)
    email_password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"


class DestinationInbox(models.Model):
    email = models.CharField(max_length=128)
    company = models.CharField(max_length=64, null=True, blank=True)
    mailbox = models.ManyToManyField(Mailbox, blank=True)

    def __str__(self):
        return f"{self.email}"


class RecievedMail(models.Model):
    email_uidl = models.CharField(max_length=128)
    send_date = models.DateTimeField(blank=True, null=True)
    email_sender = models.CharField(max_length=128)
    email_receiver = models.CharField(blank=True, null=True, max_length=128)
    subject = models.CharField(max_length=128)
    email_body = models.TextField(max_length=10000, null=True, blank=True)
    is_forwarded = models.BooleanField(default=False)
    send_to = models.CharField(max_length=256, blank=True, null=True)
    save_to_db_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject}"
