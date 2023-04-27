#!/usr/bin/python3 

# Challenge 03
# Dylan Dempsey
# 04/27/23
# E-Mail Automation

# Main

import socket
import smtplib
import ssl
from email.message import EmailMessage
from time import sleep, strftime

# Function to check if the host is up or down
def check_host_status(host, port):
    try:
        socket.create_connection((host, port), timeout=3)
        return "up"
    except socket.error:
        return "down"

# Function to send an email using the provided credentials and message details
def send_email(sender_email, password, recipient_email, host, prev_status, current_status, timestamp):
    message = EmailMessage()
    message.set_content(f"Host: {host}\nStatus changed from {prev_status} to {current_status}\nTimestamp: {timestamp}")

    message["Subject"] = f"Uptime Sensor: Host {host} status changed"
    message["From"] = sender_email
    message["To"] = recipient_email

    context = ssl.create_default_context()

    # Connect to the Gmail SMTP server and send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.send_message(message)

def main():
    # Request user inputs for email credentials and recipient email address
    sender_email = input("Please enter your email address: ")
    password = input("Please enter your email password: ")
    recipient_email = input("Please enter the recipient's email address: ")
    
    # Set the host and port to monitor
    host = "example.com"
    port = 80
    # Time interval (in seconds) between host status checks
    check_interval = 60
    # Check the initial status of the host
    prev_status = check_host_status(host, port)

    # Monitor the host status indefinitely
    while True:
        sleep(check_interval)
        current_status = check_host_status(host, port)

        # If the host status has changed, send a notification email
        if current_status != prev_status:
            timestamp = strftime("%Y-%m-%d %H:%M:%S")
            send_email(sender_email, password, recipient_email, host, prev_status, current_status, timestamp)
            prev_status = current_status

if __name__ == "__main__":
    main()

# End 

# ChatGPT was refenced for this code

# Replace host variable with the domain name or IP address you want to monitor.
# This script uses Gmail's SMTP server, so make sure to use a Gmail email address for the sender_email variable. 
# The recipient_email variable should be the email address of the administrator who will receive notifications.
