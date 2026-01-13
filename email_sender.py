import smtplib
from email.mime.text import MIMEText

# Use Gmail SMTP server
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Replace with your new Gmail and App Password
sender_email = "phishingproject231@gmail.com"
sender_password = "kjyq wmon tkwm cpid"

def send_phishing_email(target_email, phishing_link):
    print("Starting email sending process...")  # Debugging message

    subject = "Urgent: Security Update Required"
    body = f"Dear User,\n\nPlease update your credentials immediately to avoid account suspension.\nClick here: {phishing_link}"

    msg = MIMEText(body)
    msg['From'] = sender_email
    msg['To'] = target_email
    msg['Subject'] = subject

    try:
        print("Connecting to SMTP server...")  # Debugging message
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            print("Logging into Gmail...")  # Debugging message
            server.login(sender_email, sender_password)
            print("Sending email...")  # Debugging message
            server.sendmail(sender_email, target_email, msg.as_string())

        print(f"✅ Phishing email sent to {target_email}")
    
    except Exception as e:
        print("❌ Error sending email:", e)

# Test sending an email
send_phishing_email("victim@example.com", "http://example.com/phish")
