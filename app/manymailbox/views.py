import imaplib
import poplib
import email
from imap_tools import MailBox

from django.shortcuts import render
from django.core.mail import send_mail

from .email_reader import parse_pop_mail_object, parse_imap_mail_object
from .models import (
    DestinationInbox,
    Mailbox,
    RecievedMail,
)


def all_emails(request):
    emails = RecievedMail.objects.all().order_by("send_date")
    return render(request, "all-emails.html", {"test": emails})


def check_mailboxes(request):
    mailbox_counter = -1
    mailboxes = Mailbox.objects.all()
    for mailbox in mailboxes:
        mailbox_counter += 1
        server = mailbox.server
        port = mailbox.port
        user = mailbox.email_user
        password = mailbox.email_password
        if port == "993":  # imap server
            mailbox = MailBox(server, port).login(user, password)
            parse_imap_mail_object(mailbox, mailbox_counter)

        else:
            pop3server = poplib.POP3_SSL(server, port)
            pop3server.user(user)
            pop3server.pass_(password)
            pop3info = pop3server.stat()
            mailcount = pop3info[0]
            bytes_emails_uidl = poplib.POP3_SSL.uidl(
                pop3server
            )  # # Find Unique ID Listing
            emails_uidl = bytes_emails_uidl[1]  # tuple of list -> list
            parse_pop_mail_object(mailcount, pop3server, emails_uidl, mailbox_counter)

    return render(request, "check-emails.html")


def send_emails(request):
    new_emails = RecievedMail.objects.filter(is_forwarded=False)
    query_set_len = len(new_emails)
    email_counter = -1

    for _ in range(query_set_len):  # number of emails-object
        email_counter += 1
        new_email = new_emails[email_counter]
        parsed_email_reciever = new_email.email_receiver
        specific_mailbox = DestinationInbox.objects.filter(
            mailbox__email_user=parsed_email_reciever
        )

        mail_to_sent_list = []
        for mail in specific_mailbox:
            mail_to_sent_list.append(mail.email)

        send_mail(
            new_email.subject,
            new_email.email_body,
            new_email.email_sender,
            mail_to_sent_list,
            fail_silently=False,
        )
        update_email_object = RecievedMail.objects.get(id=new_email.id)
        update_email_object.is_forwarded = True
        update_email_object.send_to = mail_to_sent_list
        update_email_object.save()

    return render(request, "send-emails.html")
