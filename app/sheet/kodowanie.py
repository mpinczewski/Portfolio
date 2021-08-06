# from codecs import encode
# from logging import debug
# import poplib
# import mailparser


# pop3server = poplib.POP3_SSL("", "995")
# pop3server.user("")
# pop3server.pass_("")
# pop3info = pop3server.stat()
# mailcount = pop3info[0]

# email_subjects = []
# email_senders = []
# email_receivers = []
# email_bodies = []

# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog

# interface = Tk()

# def openfile():
#     return filedialog.askopenfilename()

# button = ttk.Button(interface, text="Dodaj pracowników z pliku", command=openfile)  # <------
# button.grid(column=1, row=1)

# button = ttk.Button(interface, text="Dodaj oddział z pliku", command=openfile)  # <------
# button.grid(column=2, row=1)

# interface.mainloop()
# """""" """"""

# from tkinter import Tk     # from tkinter import Tk for Python 3.x
# from tkinter.filedialog import askopenfilename

# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print(filename)

# """""" """""" ""

# import random


# print(random.randint(99999, 999999))

# for i in range(mailcount):
#     raw_email = b"\n".join(pop3server.retr(i + 1)[1])
#     mail = mailparser.parse_from_bytes(raw_email)
#     # Temat
#     email_subject = mail.subject
#     email_subjects.append(email_subject)
#     # Nadawca
#     email_sender = mail.from_  # lista tupli
#     email_sender = email_sender[0]  # tupla
#     email_sender = email_sender[1]
#     email_senders.append(email_sender)
#     # Odbiorca
#     email_receiver = mail.delivered_to
#     email_receiver = email_receiver[0]
#     email_receiver = email_receiver[1]
#     email_receivers.append(email_receiver)
#     # Treść
#     email_body = mail.text_plain
#     email_body = email_body[0]
#     email_bodies.append(email_body)
#     # print(email_body)

# print(email_subjects)
# print(email_senders)
# print(email_receivers)
# var = (email_bodies[14])

# s = var.decode('utf8').encode('latin1').decode('utf8')
# print(s)

# var = 'Å¼Ã³Åw, crianÃ§a'

# var.decode("iso-8859-1").encode("utf-8")

# var1 = var.encode("ISO-8859-1")
# print(f'encode: {var1}')
# var2 = var1.decode("UTF-8", errors='ignore')
# print(f'encode: {var2}')

# # initializing string
# str = 'A â Ä a â Ä C â Ä c â Ä E â Ä e â Ä L â Å l â Å N â Å n â Å O â Ã o â Ã³ S â Å s â Å Z â Å¹ z â Å¼ Z â Å» z â Å¼'
# print(str.find('Ä'))
# # encoding string
# str_enc = str.encode(encoding="ISO-8859-1")

# # printing the encoded string
# # print ("The encoded string in base64 format is : ",)
# # print (str_enc )

# # printing the original decoded string
# print ("The decoded string is : ",)
# print (str_enc.decode('utf8', errors='ignore'))

# # print(var1)
# # print(var2)
# 'crianÃ§a'.encode('utf8')#.decode('utf-8')

# ascii_code_letter = 179
# ascii_letter = chr(ascii_code_letter)
# letter = ascii_letter.encode('ISO 8859-2')

# print(letter)

# my_letter = 'ł'

# if ascii_letter == 'ł':
#     print('Well done!')
# else:
#     print("What's wrong with me?")


# print(var)
# print(f"NOWY: {email_bodies[0]}")
# print(f"NOWY: {email_bodies[1]}")
# print(f"NOWY: {email_bodies[2]}")


# list = poplib.POP3_SSL.uidl(pop3server)
# list = list[1]
# list1 = list[0]
# # print(type(list1))


# list1 = list1.decode("utf-8")
# print(list1)


# """""" """Wysyłka emaili""" """"""

# from django.core.mail import send_mail

# send_mail(
#     "Subject here",
#     "Here is the message.",
#     "from@example.com",
#     ["to@example.com"],
#     fail_silently=False,
# )


# iso_8859_1_characters = ['Ä', 'Å', 'Ã', 'Å']

# iso_8859_1_text ="Å»Ã³pr, Å»Ã³Åw -- SOLID SECURITY Sp. z o.o. Z powaÅ¼aniem, *RafaÅ BaÅka* Specjalista ds. Mrketingu Internetowego *tel. kom.: 695 840 535*"

# import poplib

# import mailparser


# def encoding_error_debugger(email_body):
#     iso_8859_1_characters = ["Ä", "Å", "Ã", "Å"]
#     for incorrect_letter in iso_8859_1_characters:  # check coding for text
#         if incorrect_letter in email_body:  # if 8859-1 coding errors:
#             email_body = email_body.encode(encoding="ISO-8859-1", errors="ignore")
#             email_body = email_body.decode("utf8", errors="ignore")
#     return email_body


# pop3server = poplib.POP3_SSL("wordpress1677089.home.pl", "995")
# pop3server.user("marketing-lead@geminitech.pl")
# pop3server.pass_("1ea4zJoa")
# pop3info = pop3server.stat()
# mailcount = pop3info[0]


# bytes_emails_uidl = poplib.POP3_SSL.uidl(pop3server)  # # Find Unique ID Listing
# emails_uidl = bytes_emails_uidl[1]  # tuple of list -> list

# for i in range(mailcount):  # parse every email
#     raw_email = b"\n".join(pop3server.retr(i + 1)[1])
#     # print(type(raw_email))
#     mail = mailparser.parse_from_bytes(raw_email)  # parse email data
#     # print(raw_email)
#     send_date = mail.date  # email sending date
#     email_subject = mail.subject  # subject

#     email_sender = mail.from_  # list of tuples

#     email_sender = email_sender[0]  # tuple
#     email_sender = email_sender[1]  # sender

#     email_receiver = mail.to  # list of tuples
#     if len(email_receiver) != 0:  # chceck email parsing
#         email_receiver = email_receiver[0]  # tuple
#         email_receiver = email_receiver[1]  # receiver

#     else:
#         pass
#     # print(mail.text_plain)
#     if len(mail.text_plain) != 0:
#         # print("dupa")
#         email_body = mail.text_plain[0]  # body of email
#     email_body = encoding_error_debugger(email_body)
#     print(
#         f"emailsender: {email_sender} emailreciever: {mail.to} subjest: {email_subject} emailbody: {email_body} mailcount: {mailcount}"
#     )
#     # get and check uidl
#     email_uidl = emails_uidl[0]

# check_uidl_in_db = RecievedMail.objects.filter(email_uidl=email_uidl)
# if len(check_uidl_in_db) == 0:
#     pass
#     # create_email_objects(
#     #     email_uidl,
#     #     send_date,
#     #     email_subject,
#     #     email_sender,
#     #     email_receiver,
#     #     email_body,
#     # )
# else:
#     pass
# emails_uidl.pop(0)  # remove checked uidl

# import re

# just = "WAR-560233"
# price = re.findall("\d+", just)[0]

# print(price)


# short_str = "test@test.pl"
# string = "test2@test.pl;test@test.pl"
# x = short_str.split(";")
# print(type(x))
# print(x)


import mailparser
import imaplib
import base64
import os
import email


email_user = "dobrytyp@op.pl"
email_pass = "Onet2021"

mail = imaplib.IMAP4_SSL("imap.poczta.onet.pl", 993)
mail.login(email_user, email_pass)
mail.select('Inbox')

type, data = mail.search(None, 'ALL')
mail_ids = data[0]
id_list = mail_ids.split()
# print(id_list)

mail_list = []

for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)' )
    raw_email = data[0][1]


# converts byte literal to string removing b''
    raw_email_string = raw_email.decode('utf-8')
    rt = raw_email_string.encode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    mail_list.append(email_message)
    # print(rt)

for mail in mail_list:
    email_subject = mail.subject
    print(email_subject)
