import smtplib, ssl, qrcode, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

port = 587
host = "smtp-mail.outlook.com"
sender_email = "prova@outlook.com"
password = "Prova"

receiver_email = input("Mail del destinatario: ")

msg = MIMEMultipart()
msg['From'] = 'Prova <' + sender_email + '>'
msg['To'] = receiver_email
msg['Subject'] = 'Prova'

filename = "temp.png"
img = qrcode.make("3")
img.save(filename)

with open('temp.png', 'rb') as fp:
    img = MIMEImage(fp.read())
    img.add_header('Content-Disposition', 'attachment', filename="temp.png")
    msg.attach(img)

os.remove("temp.png")

smtp_server = smtplib.SMTP(host, port=port)
context = ssl.create_default_context()

smtp_server.starttls(context=context)
smtp_server.login(sender_email, password)
smtp_server.sendmail(sender_email, receiver_email, msg.as_string())