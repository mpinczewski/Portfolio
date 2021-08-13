from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail

from .forms import MailboxForm
from .models import DestinationInbox, Mailbox, RecievedMail
from .email_reader import connect_pop_server, connect_imap_server


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
    obj = Mailbox.objects.get(email_user=user)
    id = obj.id
    return render(request, "errors.html", {"user": user, "id": id})


def check_mailboxes(request):
    mailbox_counter = -1
    mailboxes = Mailbox.objects.all()
    for mailbox in mailboxes:
        port = mailbox.port
        user = mailbox.email_user
        if port == "993":  # imap server
            mailbox_counter += 1
            check_errors = connect_imap_server(mailbox, mailbox_counter)
            if check_errors == True:
                return login_errors(request, user)
        elif port == "995":  # pop server
            mailbox_counter += 1
            check_errors = connect_pop_server(mailbox, mailbox_counter)
            if check_errors == True:
                return login_errors(request, user)
        else:  # incorrect port
            mailbox_counter += 1
            return login_errors(request, user)

    return render(request, "check-emails.html", {"user": user})


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
