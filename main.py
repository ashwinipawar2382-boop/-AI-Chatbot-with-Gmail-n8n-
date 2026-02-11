pip install openai google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2 python-dotenv
import os
import base64
from email.mime.text import MIMEText
from dotenv import load_dotenv
from openai import OpenAI
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Gmail API scope
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def get_unread_messages(service):
    results = service.users().messages().list(
        userId='me', labelIds=['UNREAD'], maxResults=5).execute()
    messages = results.get('messages', [])
    return messages

def get_message_content(service, msg_id):
    message = service.users().messages().get(
        userId='me', id=msg_id, format='full').execute()

    payload = message['payload']
    headers = payload['headers']

    subject = ""
    sender = ""

    for header in headers:
        if header['name'] == 'Subject':
            subject = header['value']
        if header['name'] == 'From':
            sender = header['value']

    parts = payload.get('parts')
    body = ""

    if parts:
        for part in parts:
            if part['mimeType'] == 'text/plain':
                data = part['body']['data']
                body = base64.urlsafe_b64decode(data).decode()
    else:
        data = payload['body']['data']
        body = base64.urlsafe_b64decode(data).decode()

    return subject, sender, body

def generate_ai_reply(email_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional email assistant."},
            {"role": "user", "content": f"Reply professionally to this email:\n{email_text}"}
        ]
    )
    return response.choices[0].message.content

def send_reply(service, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['subject'] = f"Re: {subject}"

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    body = {'raw': raw}

    service.users().messages().send(userId='me', body=body).execute()

def mark_as_read(service, msg_id):
    service.users().messages().modify(
        userId='me',
        id=msg_id,
        body={'removeLabelIds': ['UNREAD']}
    ).execute()

def main():
    service = authenticate_gmail()
    messages = get_unread_messages(service)

    if not messages:
        print("No unread messages found.")
        return

    for msg in messages:
        msg_id = msg['id']
        subject, sender, body = get_message_content(service, msg_id)

        print("Processing email:", subject)

        ai_reply = generate_ai_reply(body)
        send_reply(service, sender, subject, ai_reply)
        mark_as_read(service, msg_id)

        print("Replied successfully!\n")

if __name__ == '__main__':
    main()
