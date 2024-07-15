import tkinter as tk
import random
import smtplib
from email.mime.text import MIMEText

# Function to send OTP via email
def send_otp_email(to_email, otp):
    msg = MIMEText(f"Your OTP is: {otp}")
    msg['Subject'] = "OTP Verification"
    msg['From'] = "your_email@example.com"
    msg['To'] = to_email

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your_email@example.com", "your_password")
    server.sendmail("your_email@example.com", to_email, msg.as_string())
    server.quit()

# Function to verify OTP
def verify_otp():
    user_otp = otp_entry.get()
    if user_otp == otp:
        print("OTP verified successfully!")
        # You can add additional logic here, such as logging in the user
    else:
        print("Invalid OTP. Please try again.")

# Create GUI
root = tk.Tk()
root.title("OTP Verification")

# Email entry field
email_label = tk.Label(root, text="Enter your email:")
email_label.pack()
email_entry = tk.Entry(root, width=30)
email_entry.pack()

# Send OTP button
def send_otp():
    global otp
    otp = str(random.randint(100000, 999999))
    send_otp_email(email_entry.get(), otp)
    otp_label.pack()
    otp_entry.pack()
    verify_button.pack()

send_otp_button = tk.Button(root, text="Send OTP", command=send_otp)
send_otp_button.pack()

# OTP entry field
otp_label = tk.Label(root, text="Enter OTP:")
otp_entry = tk.Entry(root, width=30)

# Verify OTP button
verify_button = tk.Button(root, text="Verify OTP", command=verify_otp)

root.mainloop()