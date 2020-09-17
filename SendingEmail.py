import smtplib
import os
import getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

'''If you are coming from a Unix/Linux background, you should know that you cannot directly
send emails using command like mailx -s ... in Python as Python isnt running on a server directly'''

os.chdir('C:/tech/python/Python/Python')

try:
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
#When using the 587 port, this means you are using TLS encryption, which you need to initiate by running the starttls() command.
#If you are using port 465, this means you are using SSL and you can skip this step.
    print(f"we are connected to gmail {smtp_obj.ehlo()}")
    smtp_obj.starttls()
    # use getpass to enter email and password securely
    # email = getpass.getpass("Enter your email: ")
    # password = getpass.getpass("Enter your password: ")

    # Unsecure email and password
    email1 = input("enter email: ")
    pass1 = input("enter password: ")
    smtp_obj.login(email1, pass1)

    # mail details below:
    from_address = email1
    to_address = email1
    subject = "hey guru"
    body = "how are you"

    # Construct multi-part for sending .txt,.pdf,.csv etc
    message = MIMEMultipart()
    message["From"] = from_address
    message["To"] = to_address
    message["Subject"] = subject
    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "py core.txt"

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    #msg = "Subject: " + subject + '\n' + message

    # Send email
    smtp_obj.sendmail(from_address, to_address, text)
    smtp_obj.quit()
except smtplib.SMTPException as e:
    print("there is something wrong,check this message {}".format(e))
