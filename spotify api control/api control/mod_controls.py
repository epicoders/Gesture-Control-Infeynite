import serial
import time
import requests

ACCESS_TOKEN = 'your_access_token'  # Replace with your actual access token
BASE_URL = 'https://api.spotify.com/v1/me/player/'

# Initialize serial connection
# Replace 'COM_PORT' with the port your Arduino is connected to
ser = serial.Serial('COM_PORT', 9600)

# Initialize volume level (in percentage)
current_volume = 50  # Start with a default volume level of 50%

def make_request(endpoint, method='GET', data=None):
    url = BASE_URL + endpoint
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    try:
        response = requests.request(method, url, headers=headers, json=data)
        if response.status_code == 200:
            print(f"Success: {response.json()}")
        elif response.status_code == 204:
            print("Success: No Content")
        else:
            print(f"Error {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")

def set_volume(volume):
    # Ensure volume is between 0 and 100
    volume = max(0, min(100, volume))
    make_request(f'volume?volume_percent={volume}', method='PUT')
    print(f"Volume set to {volume}%")

def control_spotify(command):
    global current_volume

    if command == "NEXT_TRACK":
        make_request('next', method='POST')
    elif command == "PREV_TRACK":
        make_request('previous', method='POST')
    elif command == "VOL_UP":
        current_volume += 10
        set_volume(current_volume)
        if current_volume > 100:
            current_volume = 100
    elif command == "VOL_DOWN":
        current_volume -= 10
        set_volume(current_volume)
        if current_volume < 0:
            current_volume = 0
    elif command == "PLAY_PAUSE":
        make_request('play/pause', method='PUT')
    else:
        print(f"Unknown command: {command}")

def main():
    while True:
        if ser.in_waiting > 0:
            command = ser.readline().decode('utf-8').strip()
            print(f"Received command: {command}")
            control_spotify(command)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
