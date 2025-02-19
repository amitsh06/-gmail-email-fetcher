import base64
import csv
import os
import pandas as pd
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from bs4 import BeautifulSoup

# 🔹 Load Credentials
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
creds = Credentials.from_authorized_user_file('token.json', SCOPES)
service = build('gmail', 'v1', credentials=creds)

def get_emails():
    results = service.users().messages().list(userId='me', maxResults=10).execute()
    messages = results.get('messages', [])

    email_data = []
    for msg in messages:
        msg_id = msg['id']
        msg_detail = service.users().messages().get(userId='me', id=msg_id).execute()

        headers = msg_detail['payload']['headers']
        subject = sender = date = ''
        
        for header in headers:
            if header['name'] == 'Subject':
                subject = header['value']
            elif header['name'] == 'From':
                sender = header['value']
            elif header['name'] == 'Date':
                date = header['value']

        # 🔹 Extract email body safely
        body = ''
        payload = msg_detail['payload']
        
        try:
            if 'parts' in payload:
                for part in payload['parts']:
                    if part['mimeType'] == 'text/plain' and 'data' in part['body']:
                        body = base64.urlsafe_b64decode(part['body']['data']).decode()
                        break
            elif 'body' in payload and 'data' in payload['body']:
                body = base64.urlsafe_b64decode(payload['body']['data']).decode()

        except Exception as e:
            print(f"⚠ Error decoding email {msg_id}: {e}")

        # 🔹 Clean email body
        body = BeautifulSoup(body, 'html.parser').get_text()

        email_data.append([date, sender, subject, body])

    return email_data

# 🔹 Save Emails to CSV
def save_to_csv(email_data, filename='emails.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Sender", "Subject", "Body"])
        writer.writerows(email_data)
    print(f"✅ Emails saved to {filename}")

# 🔹 Save Emails to Excel
def save_to_excel(email_data, filename='emails.xlsx'):
    df = pd.DataFrame(email_data, columns=["Date", "Sender", "Subject", "Body"])
    df.to_excel(filename, index=False)
    print(f"✅ Emails saved to {filename}")

if __name__ == "__main__":
    emails = get_emails()
    print("Fetched Emails:", emails)  # 🔹 Debugging ke liye print
    if emails:
        save_to_csv(emails)
        save_to_excel(emails)
    else:
        print("⚠ No Emails Found!")
