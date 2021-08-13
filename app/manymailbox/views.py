import imaplib
import poplib
from poplib import error_proto
from socket import gaierror

from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail

from imap_tools import MailBox

from .forms import MailboxForm
from .email_reader import parse_pop_mail, parse_imap_mail_object
from .models import (
    DestinationInbox,
    Mailbox,
    RecievedMail,
)


def add_mailbox(request):
    if request.method == "POST":
        form = MailboxForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("/manymailbox/all-emails/")
    else:
        form = MailboxForm()

    return render(request, "add-mailbox.html", {"form": form})


def all_mailboxes(request):
    mailbox = Mailbox.objects.all()
    return render(request, "all-mailboxes.html", {"test": mailbox})


def edit_mailbox(request, id):
    instance = get_object_or_404(Mailbox, id=id)
    form = MailboxForm(data=request.POST or None, instance=instance)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/manymailbox/all-mailboxes/")

    return render(request, "add-mailbox.html", {"form": form})


def delete_mailbox(request, id):
    instance = get_object_or_404(Mailbox, id=id)
    form = MailboxForm(data=request.POST or None, instance=instance)

    if request.method == "POST":
        instance.delete()
        return redirect("/manymailbox/all-mailboxes/")

    return render(request, "delete-mailbox.html", {"form": form})


def all_emails(request):
    emails = RecievedMail.objects.all().order_by("send_date")
    return render(request, "all-emails.html", {"test": emails})


def login_errors(request, user):
    print(user)
    obj = Mailbox.objects.get(email_user=user)
    id = obj.id
    return render(request, "errors.html", {"user": user, "id": id})


def connect_imap_server(request, mailbox, mailbox_counter):
    server = mailbox.server
    port = mailbox.port
    user = mailbox.email_user
    password = mailbox.email_password
    try:
        mailbox = MailBox(server, port).login(user, password)
        parse_imap_mail_object(mailbox, mailbox_counter)
    except imaplib.IMAP4.error:
        print("imaplib.IMAP4.error")
        return redirect("access-denied.html", {"user": user})
    except gaierror:
        print("gaierror")
        return render(request, "errors.html", {"user": user})
    except TimeoutError:
        print("TimeoutError")
        return render(request, "errors.html", {"user": user})


def connect_pop_server(request, mailbox, mailbox_counter):
    server = mailbox.server
    port = mailbox.port
    user = mailbox.email_user
    password = mailbox.email_password
    try:
        pop3server = poplib.POP3_SSL(server, port)
        pop3server.user(user)
        pop3server.pass_(password)
        pop3info = pop3server.stat()
        mailcount = pop3info[0]
        bytes_emails_uidl = poplib.POP3_SSL.uidl(
            pop3server
        )  # Find Unique ID Listing
        emails_uidl = bytes_emails_uidl[1]  # tuple of list -> list
        parse_pop_mail(mailcount, pop3server, emails_uidl, mailbox_counter)
    except TimeoutError:
        print("TimeoutError")
        return render(request, "errors.html", {"user": user})
    except error_proto:
        print("error_proto")
        return login_errors(request, user)


def check_mailboxes(request):
    mailbox_counter = -1
    mailboxes = Mailbox.objects.all()
    for mailbox in mailboxes:
        port = mailbox.port
        user = mailbox.email_user
        password = mailbox.email_password
        if port == "993":  # imap server
            mailbox_counter += 1
            connect_imap_server(request, mailbox, mailbox_counter)
        elif port == "995":
            mailbox_counter += 1
            connect_pop_server(request, mailbox, mailbox_counter)
        else:
            mailbox_counter += 1
            return render(request, "errors.html", {"user": user})

    return render(request, "check-emails.html", {"user": user})


# def check_mailboxes(request):
#     mailbox_counter = -1
#     mailboxes = Mailbox.objects.all()
#     for mailbox in mailboxes:
        
#         server = mailbox.server
#         port = mailbox.port
#         user = mailbox.email_user
#         password = mailbox.email_password
#         if port == "993":  # imap server
#             mailbox_counter += 1
#             try:
#                 mailbox = MailBox(server, port).login(user, password)
#                 parse_imap_mail_object(mailbox, mailbox_counter)
#             except imaplib.IMAP4.error:
#                 return render(request, "access-denied.html", {"user": user})
#             except gaierror:
#                 return render(request, "errors.html", {"user": user})
#             except TimeoutError:
#                 return render(request, "errors.html", {"user": user})
#         elif port == "995":
#             mailbox_counter += 1
#             try:
#                 pop3server = poplib.POP3_SSL(server, port)
#                 pop3server.user(user)
#                 pop3server.pass_(password)
#                 pop3info = pop3server.stat()
#                 mailcount = pop3info[0]
#                 bytes_emails_uidl = poplib.POP3_SSL.uidl(
#                     pop3server
#                 )  # Find Unique ID Listing
#                 emails_uidl = bytes_emails_uidl[1]  # tuple of list -> list
#                 parse_pop_mail(mailcount, pop3server, emails_uidl, mailbox_counter)
#             except TimeoutError:
#                 return render(request, "errors.html", {"user": user})
#             except error_proto:
#                 print(user)
#                 return login_errors(request, user)
#                 # return render(request, "errors.html", {"user": user})
#             except ConnectionRefusedError:
#                 return render(request, "errors.html", {"user": user})
#         else:
#             mailbox_counter += 1
#             return render(request, "errors.html", {"user": user})

#     return render(request, "check-emails.html", {"user": user})


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


def access_denied(request):
    return render(request, "access-denied.html")
