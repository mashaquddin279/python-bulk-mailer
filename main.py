
import os
import re
import ssl
import smtplib
import time
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
# HTML EMAIL CONTENT
# ==========================================

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>India Automation & Robotics Expo 2026</title>
</head>

<body style="
    margin:0;
    padding:20px;
    background-color:#f2f4f7;
    font-family:Arial, Helvetica, sans-serif;
">

<table width="100%" cellpadding="0" cellspacing="0">
<tr>
<td align="center">

<table width="650" cellpadding="0" cellspacing="0"
       style="
       background-color:#ffffff;
       border-radius:8px;
       overflow:hidden;
       ">

    <!-- HEADER -->
    <tr>
        <td style="
            background-color:#0b2c4d;
            color:#ffffff;
            padding:22px 30px;
        ">

            <h2 style="margin:0;">
                India Automation & Robotics Expo 2026
            </h2>

            <p style="margin:6px 0 0;">
                New Year Special Exhibitor Offer
            </p>

        </td>
    </tr>


    <!-- CONTENT -->
    <tr>
        <td style="
            padding:30px;
            color:#333333;
            font-size:15px;
            line-height:1.6;
        ">

            <p>Dear Sir/Madam,</p>

            <p>
                Greetings from
                <strong>India Automation & Robotics Expo 2026</strong>.
            </p>

            <p>
                We are pleased to announce a
                <strong>limited-time New Year discount on stall bookings</strong>
                for companies planning to exhibit at IAR Expo 2026.
            </p>

            <p>
                The exhibition will take place from
                <strong>06–08 April 2026</strong> at
                <strong>Bangalore International Exhibition Centre (BIEC)</strong>.
            </p>


            <!-- OFFER -->
            <div style="
                background-color:#fff3cd;
                border:1px solid #ffeeba;
                padding:14px;
                margin:20px 0;
                border-radius:4px;
            ">

                <strong>Important Notice</strong>

                <br>

                This special offer is valid until
                <strong>15 January</strong>.

                Stall allocation will be handled on a
                <strong>first-come, first-served basis</strong>.

            </div>


            <h3 style="color:#0b2c4d;">
                Why Exhibit?
            </h3>

            <ul>
                <li>
                    Platform for Automation, Robotics, AI and Industry 4.0
                </li>

                <li>
                    Connect with plant heads, CXOs and procurement professionals
                </li>

                <li>
                    Reach manufacturing and technology companies
                </li>

                <li>
                    Build brand visibility and generate business opportunities
                </li>
            </ul>


            <h3 style="color:#0b2c4d;">
                Stall Options
            </h3>

            <ul>
                <li>Shell Space – Ready-to-use exhibition package</li>
                <li>Bare Space – Custom booth design flexibility</li>
                <li>Multiple stall sizes and locations available</li>
            </ul>


            <p>
                Companies confirming participation early can benefit from
                special pricing and secure preferred stall locations.
            </p>


            <p>
                Warm regards,<br>
                <strong>Media Day Marketing</strong>
            </p>


            <p style="
                font-size:13px;
                color:#555555;
            ">

                No:16-2-741/D/24, 2nd Floor,<br>
                Fazilat Manzil, Beside TV Tower,<br>
                Malakpet, Hyderabad – 500036, Telangana

            </p>

        </td>
    </tr>

</table>

</td>
</tr>
</table>

</body>
</html>
"""


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
