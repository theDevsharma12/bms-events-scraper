import os
import smtplib
from email.mime.text import MIMEText
from scrape_events import scrape_events

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["EMAIL_PASSWORD"]
TO_EMAIL = os.environ["TO_EMAIL"]

events = scrape_events()

if not events:
    raise Exception("No events scraped. Email not sent.")

body = ""
for e in events:
    body += (
        f"Event: {e['Event Name']}\n"
        f"Date: {e['Date']}\n"
        f"Venue: {e['Venue']}\n"
        f"Link: {e['Link']}\n"
        "-----------------------------\n"
    )

msg = MIMEText(body)
msg["Subject"] = "Daily Jaipur Events – BookMyShow"
msg["From"] = EMAIL
msg["To"] = TO_EMAIL

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.send_message(msg)

print("✅ Email sent successfully")
