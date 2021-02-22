# coding=utf-8

# Date and Time library
import datetime

# E-mail libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP server library
import smtplib

# HTTP handler to get the External IP address
import urllib2


# Get current timestamp
CurrDate = datetime.date.today()


# SMTP server details
SMTP_addr = "smtp.gmail.com"
SMTP_port = 587


# E-mail account that will be used as sender
sender_email = ""
sender_password = ""


# List of recipients to use in the e-mail
# Each entry on this list must be separated by commas, and encased in quotes
# Example: ["email1@example.com", "email2@example.com", "email3@example.com"]
recipient_list = [""]


# Initialize a variable for the SMTP server connection and set-up some configurations
SMTP_conn = smtplib.SMTP(SMTP_addr, SMTP_port)
SMTP_conn.ehlo()
SMTP_conn.starttls()
SMTP_conn.login(sender_email, sender_password)


# Get the network's external IP address (IPv4)
EIPA = urllib2.urlopen("http://icanhazip.com").read()


# Initialize variables for the E-mail message
EM_Recipients_String = ", ".join(recipient_list)
EM_Message = MIMEMultipart("alternative")
EM_Message["Subject"] = "External IP address - " + CurrDate.strftime("%Y-%m-%d")
EM_Message["From"] = sender_email
EM_Message["To"] = EM_Recipients_String


# Create the text for the Message Body, both in plain text and HTML
EM_Message_Body_PlainText = "Your current external IP address is " + EIPA

EM_Message_Body_HTML = """
<html>
<head>
   <style>
      .Sig a {        
      color:rgb(0,192,192);
      }
      .Header {
      text-align: center;
      background: teal;
      color: white;
      padding: 1.4rem 2rem;
      font-size: 3rem;
      margin-bottom: 2rem;
      }
      .Footer {
      font-size: 1rem;
      padding: 1rem 0;
      background: grey;
      color: rgb(0,192,192) !important;
      margin-top: 10rem;
      display: flex;
      justify-content: space-around
      }
      .IPCont {
      display: flex;
      justify-content: center;
      }
      .IP {
      margin: 1rem;
      padding: 0.5rem;
      border: 3px solid rgb(0,192,192);
      border-radius: 7px;
      }
      @media (prefers-color-scheme: light) {
      .IP {
      border-color:rgb(0,192,192) !important;
      color:rgb(0,192,192) !important;
      }
      body {
      background: white !important;
      color: rgb(0,192,192) !important;
      }
      .Header {
      background: rgb(0,192,192) !important;
      color: white !important;
      }
      }
      @media (prefers-color-scheme: dark) {
      .IP {
      border-color:rgb(0,128,128) !important;
      color:rgb(0,128,128) !important;
      }
      body {
      background: black !important;
      color: rgb(0,128,128) !important;
      }
      .Header {
      background: rgb(0,128,128) !important;
      color: lightgrey !important;
      }
      }
      body {
      font-family: Arial, Helvetica, sans-serif !important;
      background: white;
      margin: 0;
      font-size: 1.4rem;
      }
   </style>
   </head>
   <body>
      <div class="Header">
         External IP address
      </div>
      <div style="text-align: center">
         Your address is:
      </div>
      <div class="IPCont" style="display: flex; justify-content: center">
         <div class="IP" onclick="var EIPA = '""" + EIPA + """'; EIPA.select(); EIPA.setSelectionRange(0, 99999); document.execCommand("copy");">
            """ + EIPA + """
         </div>
      </div>
      <div class="Footer" style="display: inline-flex; justify-content: space-between; width: 100%; padding: 1rem">
         <div class="execTS">
            Script execution started at <b>""" + CurrDate.strftime("%Y-%m-%d %H:%M:%S") + """</b>
         </div>
         <div class="Sig">
            <a style="text-decoration: none" href="https://github.com/rt-zen">rt-zen</a>
         </div>
      </div>
   </body>
</html>"""


# Create both MIME objects to attach to the E-Mail message
MIMEText_Plain = MIMEText(EM_Message_Body_PlainText, "plain")
MIMEText_HTML = MIMEText(EM_Message_Body_HTML, "html")


# Attach both MIME objects to the E-Mail message
EM_Message.attach(MIMEText_Plain)
EM_Message.attach(MIMEText_HTML)


# Send EMail message
SMTP_conn.sendmail(sender_email, EM_Recipients_String, EM_Message.as_string())


# Close SMTP instance
SMTP_conn.quit()
