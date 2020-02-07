import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#we are going to use the email package to add attachments to our emails
from email import encoders
from email.mime.base import MIMEBase
import ssl

my_email = "cartmanusbg233@gmail.com"
my_password = ""
sender_email = "cartmanbg233@abv.bg"
gmail = 'smtp.gmail.com'

#MIMEMultipart("alternative") instance combines our html and plain-text versions into a single message
msg = MIMEMultipart('alternative')
msg['Subject'] = input("Enter subject: ")
msg['From'] = my_email
msg['To'] = sender_email

html = '<html><body><p><a href="https://www.google.com">Hi, this is a succesfull hyperlink message!</a></p></body></html>'

#MIMEText contains our html and plain-text versions of our message
#plain text can be also parsed with MIMEText, by specifying the first
#parameter to be our variable containing the plain text and the second
#parameter to be 'plain'
body = MIMEText(html, 'html')

#attach body of the message to the msg variable
msg.attach(body)

attachmentName = input("Specify attachment name: ")
#open file in binary mode
attachment = open("", "rb")

# Add file as application/octet-stream
# Email client can usually download this automatically as attachment
part = MIMEBase("application", "octet-stream")
part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {attachmentName}",
)

# Add attachment to message and convert message to string
msg.attach(part)

#Log in to server using secure context and send email
context = ssl.create_default_context()

server = smtplib.SMTP_SSL(gmail, 465, context=context)
server.login(my_email, my_password)
server.sendmail(my_email, sender_email, msg.as_string())
server.quit()