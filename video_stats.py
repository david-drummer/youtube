import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

#API_KEY = 'AIzaSyBNHUiSjnOoI6GwPxHiye_dKLLOctB-uXw'

CHANNEL_HANDLE = 'VivaLaDirtLeague'

url = f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}'

def get_playlistId():
    try:
        response = requests.get(url)

        response.raise_for_status()
        print(response)

        data = response.json()

        json.dumps(data, indent=4)

        channel_items = data['items'][0]

        channel_playlistId = channel_items['contentDetails']['relatedPlaylists']['uploads']

        print(channel_playlistId)

        return channel_playlistId
    except requests.exceptions.RequestException as e:
        raise e
    
if __name__ == "__main__":
    get_playlistId()

