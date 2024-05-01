import csv
from twilio.rest import Client
import json

# Enter Twilio Account SID and Auth Token here
account_sid = 'Account SID'
auth_token = 'Auth Token'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Function to send WhatsApp message using template ID and media
def send_whatsapp_message(to, content_sid, content_variables):
    try:
        message = client.messages.create(
            messaging_service_sid='MG1U1U1U1U1U1U1U1U',  # Replace with your Messaging Service SID
            to=to,
            content_sid=content_sid,
            content_variables=content_variables
        )
        print(f"Message sent to {to}: {message.sid}")
    except Exception as e:
        print(f"Error sending message to {to}: {e}")

# Path to CSV file containing contacts (name, number)
csv_file_path = '/Users/Username/Desktop/contacts.csv'

# Read contacts from CSV file and send messages
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row if exists
    for row in reader:
        name, number = row[0], row[1]
        whatsapp_to = f"whatsapp:{number}"
      # Enter Template ID here
        send_whatsapp_message(whatsapp_to, 'Templete_ID',json.dumps({
                                  '1': 'Name'})
                                  )
