from fastapi import FastAPI
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from scripts.schemas.response_models import Email

app = FastAPI()

class Email_handler:
    def send_email(self, email: Email):
        # Set up the email details
        sender_email = "nisanthpraveen02@gmail.com"
        sender_password = "prkqjrsdhtdjpkmb"
        receiver_email = email.rec_email

        # Create a multipart message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = email.subject

        # Add the body to the email
        message.attach(MIMEText(email.body, "plain"))

        try:
            # Create a secure connection to the SMTP server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            # Login to the sender's email account
            server.login(sender_email, sender_password)

            # Send the email
            server.send_message(message)

            # Close the connection
            server.quit()

            return {"message": "Email sent successfully"}
        except Exception as e:
            return {"message": str(e)}
