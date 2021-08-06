import mailparser
 
# import six
# import simplejson

from django.shortcuts import render


from .models import Mailbox, RecievedMail


def encoding_error_debugger(email_body):
    iso_8859_1_characters = ["Ä", "Å", "Ã", "Å"]
    for incorrect_letter in iso_8859_1_characters:  # check coding type in text
        if incorrect_letter in email_body:  # if 8859-1 coding errors:
            email_body = email_body.encode(encoding="ISO-8859-1", errors="ignore")
            email_body = email_body.decode("utf8", errors="ignore")
    return email_body


def create_email_objects(*args):
    RecievedMail.objects.create(
        email_uidl=args[0],
        send_date=args[1],
        email_sender=args[3],
        email_receiver=args[4],
        subject=args[2],
        email_body=args[5],
    )


def check_email_uidl(mailbox_counter, email_uidl):
    all_mailboxes = Mailbox.objects.all()  # take all mailboxes
    mailbox_name = all_mailboxes[mailbox_counter]
    mailbox_name = mailbox_name.name.lower()  # Business vs DB issue :)
    email_uidl = f"{mailbox_name} - {email_uidl}"  # merge mailbox name with email uidl
    return email_uidl


def parse_mail_object(mailcount, pop3server, emails_uidl, mailbox_counter):
    for i in range(mailcount):  # parse every email in box
        raw_email = b"\n".join(pop3server.retr(i + 1)[1])
        mail = mailparser.parse_from_bytes(raw_email)  # parse email data
        send_date = mail.date  # email sending date
        email_subject = mail.subject  # subject
        email_sender = mail.from_  # list of tuples
        email_sender = email_sender[0]  # tuple
        email_sender = email_sender[1]  # sender
        email_receiver = mail.to  # list of tuples
        if len(email_receiver) != 0:  # chceck email parsing
            email_receiver = email_receiver[0]  # tuple
            email_receiver = email_receiver[1]  # receiver
        email_body = mail.text_plain[0]  # body of email
        email_body = encoding_error_debugger(email_body)

        email_uidl = emails_uidl[0]  # get uidl
        email_uidl = check_email_uidl(mailbox_counter, email_uidl)

        check_uidl_in_db = RecievedMail.objects.filter(email_uidl=email_uidl)
        if len(check_uidl_in_db) == 0:
            create_email_objects(
                email_uidl,
                send_date,
                email_subject,
                email_sender,
                email_receiver,
                email_body,
            )
        else:
            pass
        emails_uidl.pop(0)  # remove checked uidl
