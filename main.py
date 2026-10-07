
import os
import re
import ssl
import smtplib
import time
from pathlib import Path
from email.message import EmailMessage


# ==========================================
# CONFIGURATION
# ==========================================

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

SUBJECT = "India Automation & Robotics Expo 2026 | New Year Offer"


# ==========================================
# LOAD HTML EMAIL TEMPLATE
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_FILE = BASE_DIR / "email_template.html"


def load_email_template():
    """Load the HTML email template from the project folder."""

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as file:
        return file.read()


HTML_CONTENT = load_email_template()


# ==========================================
# RECIPIENTS
# ==========================================

raw_recipients = [
    # Add approved/opt-in business recipients here.
    # "example@company.com",
]


# ==========================================
# EMAIL VALIDATION
# ==========================================

def is_valid_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, email) is not None


recipients = [
    email.strip()
    for email in raw_recipients
    if is_valid_email(email.strip())
]


# ==========================================
# SEND EMAILS
# ==========================================

def send_emails():

    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
        raise ValueError(
            "EMAIL_ADDRESS and EMAIL_PASSWORD environment variables are required."
        )

    print(f"Valid recipients: {len(recipients)}")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(
        SMTP_SERVER,
        SMTP_PORT,
        context=context
    ) as server:

        server.login(
            EMAIL_ADDRESS,
            EMAIL_PASSWORD
        )

        for recipient in recipients:

            try:

                message = EmailMessage()

                message["Subject"] = SUBJECT
                message["From"] = EMAIL_ADDRESS
                message["To"] = recipient

                message.set_content(
                    "Please view this email in HTML format."
                )

                message.add_alternative(
                    HTML_CONTENT,
                    subtype="html"
                )

                server.send_message(message)

                print(f"Sent successfully: {recipient}")

                # Small delay between messages
                time.sleep(2)

            except Exception as error:

                print(
                    f"Failed to send to {recipient}: {error}"
                )


# ==========================================
# PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":
    send_emails()
