import smtplib
from email.mime.text import MIMEText
from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Load email credentials from environment variables
gmail_user = os.getenv('GMAIL_USER')
gmail_password = os.getenv('GMAIL_PASSWORD')

def send_email(subject, body, recipient_email):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = gmail_user
    msg['To'] = recipient_email

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, recipient_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

if __name__ == '__main__':
    # Send a single email when the script is run
    subject = "Automated Email"
    body = "This is a test email sent when the script starts."
    recipient_email = "kherikisia@gmail.com"
    
    if send_email(subject, body, recipient_email):
        print("Email sent successfully!")
    else:
        print("Failed to send email.")
    
    # Start the Flask app
    app.run(host='0.0.0.0', port=5000)
