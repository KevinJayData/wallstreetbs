import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(config):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = config.sender_email
    message["To"] = config.receiver_email
    message["Subject"] = config.subject
    message["Bcc"] = config.receiver_email  # Recommended for mass emails
    message.attach(MIMEText(config.body, "plain"))
    filename = "todays_bullshit.csv"

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

    port = 465  # For SSL
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(config.sender_email, config.email_password)
        server.sendmail(config.sender_email, config.receiver_email, text)

    print('Email sent to the knuckle draggers')