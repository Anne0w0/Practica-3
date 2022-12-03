import smtplib
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '
# Define params
rrdpath = '/home/anapaty/PycharmProjects/Introduccion_SNMP/Practica-3/RRD/'
imgpath = '/home/anapaty/PycharmProjects/Introduccion_SNMP/Practica-3/IMG/'
fname = 'trend.rrd'

mailsender = "dummycuenta3@gmail.com"
mailreceip = "anapaty2000@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'dvduuffmlhspbmjj'

def send_alert_attached(subject,servicio):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    fp = open(imgpath+servicio, 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    s = smtplib.SMTP(mailserver)

    s.starttls()

    s.login(mailsender, password)

    time.sleep(10)

    s.sendmail(mailsender, mailreceip, msg.as_string())

    s.quit()