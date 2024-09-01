import requests
import base64

CLIENT_ID = 'ebe367b1678e48bb963a2687b9217128'  # Replace with your actual Client ID
CLIENT_SECRET = 'aa5383ade714409b83c94776f5134bf2'  # Replace with your actual Client Secret
REDIRECT_URI = 'http://localhost:9000/callback'  # Ensure this matches your registered Redirect URI
AUTHORIZATION_CODE = 'your_authorization_code'  # Replace with your actual authorization code

def get_access_token():
    token_url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'authorization_code',
        'code': AUTHORIZATION_CODE,
        'redirect_uri': REDIRECT_URI
    }
   
    response = requests.post(token_url, headers=headers, data=data)
    response_data = response.json()
   
    if response.status_code == 200:
        access_token = response_data['access_token']
        refresh_token = response_data.get('refresh_token')
        print(f"Access Token: {access_token}")
        print(f"Refresh Token: {refresh_token}")
    else:
        print(f"Error {response.status_code}: {response.text}")

# Example usage
get_access_token()
