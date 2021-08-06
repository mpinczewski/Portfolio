from django.test import TestCase

from ..models import DestinationInbox, Mailbox, RecievedMail


class MailboxTests(TestCase):
    def setUp(self):
        self.name = "Skrzynka Testowa"
        self.server = "test.home.pl"
        self.port = "995"
        self.email_user = "test@home.pl"
        self.email_password = "haslo123"

    def test_mailbox_create(self):
        new_mailbox = Mailbox.objects.create(
            name="Skrzynka Testowa",
            server="test.home.pl",
            port="995",
            email_user="test@home.pl",
            email_password="haslo123",
        )
        len_list = Mailbox.objects.all()

        self.assertEqual(new_mailbox.name, self.name)
        self.assertEqual(new_mailbox.server, self.server)
        self.assertEqual(new_mailbox.port, self.port)
        self.assertEqual(new_mailbox.email_user, self.email_user)
        self.assertEqual(new_mailbox.email_password, self.email_password)
        self.assertEqual(len(len_list), 1)


class RecievedMailTests(TestCase):
    def setUp(self):
        self.email_uidl = "Test - b'7 0000000760acedc7'"
        self.send_date = "2021-07-22 10:14:37+00:00"
        self.email_sender = "emailod@test.pl"
        self.email_receiver = "emaildo@test.pl"
        self.subject = "temat"
        self.email_body = "tresć maila"
        self.is_forwarded = False
        self.send_to = "przekazanydo@test.pl"

    def test_recieved_mail_creation(self):
        new_recieved_mail = RecievedMail.objects.create(
            email_uidl="Test - b'7 0000000760acedc7'",
            send_date="2021-07-22 10:14:37+00:00",
            email_sender="emailod@test.pl",
            email_receiver="emaildo@test.pl",
            subject="temat",
            email_body="tresć maila",
            is_forwarded=False,
            send_to="przekazanydo@test.pl",
        )
        self.assertEqual(new_recieved_mail.email_uidl, self.email_uidl)
        self.assertEqual(new_recieved_mail.send_date, self.send_date)
        self.assertEqual(new_recieved_mail.email_sender, self.email_sender)
        self.assertEqual(new_recieved_mail.email_receiver, self.email_receiver)
        self.assertEqual(new_recieved_mail.subject, self.subject)
        self.assertEqual(new_recieved_mail.email_body, self.email_body)
        self.assertEqual(new_recieved_mail.is_forwarded, self.is_forwarded)
        self.assertEqual(new_recieved_mail.send_to, self.send_to)


class DestinationInboxTests(TestCase):
    def setUp(self):
        self.email = "test@home.pl"
        self.company = "Testowa Firma"

    def test_mailbox_create(self):
        new_destination_inboxes = DestinationInbox.objects.create(
            email="test@home.pl",
            company="Testowa Firma",
        )
        self.assertEqual(new_destination_inboxes.email, self.email)
        self.assertEqual(new_destination_inboxes.company, self.company)
