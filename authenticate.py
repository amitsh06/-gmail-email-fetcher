from google_auth_oauthlib.flow import InstalledAppFlow
import os

# Define the required Gmail API scope (read-only access)
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    """Authenticate user and save access token."""
    creds = None

    # Authenticate user
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

    # Save the token for future use
    with open('token.json', 'w') as token:
        token.write(creds.to_json())
    print("✅ Authentication successful! Token saved as token.json.")

if __name__ == "__main__":
    authenticate_gmail()
