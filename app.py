"""
This is currently the main app file 
"""
import os
from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URL = 'https://127.0.0.1:5000'

session = OAuth2Session(client_id=CLIENT_ID, redirect_uri=REDIRECT_URL)

AUTH_BASE_URL = "https://www.strava.com/oauth/authorize"
session.scope = ["profile:read_all"]

auth_link = session.authorization_url(AUTH_BASE_URL)

print(f'Click Here: {auth_link[0]}')

redirect_response = input("Paste URL Here: ")

TOKEN_URL = "https://www.strava.com/api/v3/oauth/token"
session.fetch_token(
    token_url=TOKEN_URL,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    authorization_response=redirect_response,
    include_client_id=True
)

response = session.get("https://www.strava.com/api/v3/athlete")

print("\n\n\n")
print(f"Response Status: {response.status_code}")
print(f"Response Reason: {response.reason}")
print(f"Time Elaspsed: {response.elapsed}")
print(f"Response Text: \n{'-'*15}\n{response.text}")
