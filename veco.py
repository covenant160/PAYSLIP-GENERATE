import yagmail

# Your Gmail credentials
sender_email = "covenantlambert@gmail.com"
app_password = "sjkuawkltmmzjzng"  

# Setup yagmail client
yag = yagmail.SMTP(sender_email, app_password)

# Send email
recipient_email = "recipient_email@gmail.com"
subject = "Subject"
body = "This is the email body."

try:
    yag.send(recipient_email, subject, body)
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
