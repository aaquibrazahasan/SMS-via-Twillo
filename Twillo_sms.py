import csv
from twilio.rest import Client

# Twilio Account SID and Auth Token
account_sid = 'Account SID'
auth_token = 'Auth Token'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Function to send SMS invitation and return status
def send_invitation(to, body, messaging_service_sid):
    try:
        message = client.messages.create(
            messaging_service_sid=messaging_service_sid,
            body=body,
            to=to
        )
        return 'Success', message.sid
    except Exception as e:
        return 'Error', str(e)

# Path to CSV file containing phone numbers
csv_file_path = '/Users/aaquibhasan/Desktop/contacts.csv'

# List to store status of sent messages
report = []

# Read phone numbers from CSV file and send invitations
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row if exists
    for row in reader:
        phone_number = row[1]
      # Enter your message here within the quotes and enter the Messaging SID which you will find in the Twillo Webapp under Category SMS Service.
        status, message_id = send_invitation(phone_number, "Enter Your Message here", 'Enter Messaging SID here')
        report.append([phone_number, status, message_id])

# Write report to CSV file
report_file_path = '/Users/aaquibhasan/Desktop/invitation_report.csv'
with open(report_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Phone Number', 'Status', 'Message ID'])
    writer.writerows(report)

print(f"Invitations sent and report generated: {report_file_path}")
