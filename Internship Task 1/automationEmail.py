import smtplib
sender_email = "adeelrizwan1234@gmail.com"
password = "kizn vpmb nvqy kkmd"

receivers = [
    "adeelatlaptop@gmail.com",
    "adeelrizwan1234@gmail.com",
    "mhasnabbas3@gmail.com",
    "fatimaazeem0425@gmail.com",
    "email5@gmail.com",
    "email6@gmail.com",
    "email7@gmail.com",
    "email8@gmail.com",
    "email9@gmail.com",
    "email10@gmail.com",
    "email11@gmail.com",
    "email12@gmail.com",
    "email13@gmail.com",
    "email14@gmail.com",
    "email15@gmail.com",
    "email16@gmail.com",
    "email17@gmail.com",
    "email18@gmail.com",
    "email19@gmail.com",
    "email20@gmail.com"
]

subject = "Email Automation System"
message = """
Hello, This is Adeel 
and I'm js testing email sent using Email Automation System.

Regards
Muhammad Adeel
"""

email_text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender_email, password)

for email in receivers:
    server.sendmail(sender_email, email, email_text)
    print(f"Email sent to {email}")

server.quit()

print("All emails sent successfully!")