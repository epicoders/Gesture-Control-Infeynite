import requests

ACCESS_TOKEN = 'your_access_token'  # Replace with your access token
BASE_URL = 'https://api.spotify.com/v1/me/player/'

def make_request(endpoint, method='GET', data=None):
    url = BASE_URL + endpoint
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    try:
        response = requests.request(method, url, headers=headers, json=data)
        print(f"Raw Response: {response.text}")  # Print raw response for debugging
        response.raise_for_status()  # Raises HTTPError for bad responses
        try:
            json_response = response.json()
            print(f"Success: {json_response}")
        except requests.exceptions.JSONDecodeError as json_err:
            print(f"JSON Decode Error: {json_err}")
            print(f"Response Content: {response.text}")
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"OOps: Something Else: {err}")

def play_pause():
    make_request('play', method='PUT')

def next_track():
    make_request('next', method='POST')

def previous_track():
    make_request('previous', method='POST')

def set_volume(volume_percent):
    url = BASE_URL + 'volume'
    params = {'volume_percent': volume_percent}
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.put(url, headers=headers, params=params)
    if response.status_code == 204:
        print("Volume set successfully")
    else:
        print(f"Error {response.status_code}: {response.text}")

# Example usage
# play_pause()
# next_track()
# previous_track()
# set_volume(50)
