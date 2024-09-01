import requests
import base64

CLIENT_ID = 'ebe367b1678e48bb963a2687b9217128'
CLIENT_SECRET = 'aa5383ade714409b83c94776f5134bf2'
REFRESH_TOKEN = 'your_refresh_token'  # Replace with your refresh token

def refresh_access_token():
    token_url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': REFRESH_TOKEN
    }

    response = requests.post(token_url, headers=headers, data=data)
    response_data = response.json()

    if response.status_code == 200:
        new_access_token = response_data['access_token']
        print(f"New Access Token: {new_access_token}")
    else:
        print(f"Error {response.status_code}: {response.text}")