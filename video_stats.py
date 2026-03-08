import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

CHANNEL_HANDLE = 'VivaLaDirtLeague'
maxResults = 50
url = f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}'

def get_playlistId():
    try:
        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        json.dumps(data, indent=4)

        channel_items = data['items'][0]

        channel_playlistId = channel_items['contentDetails']['relatedPlaylists']['uploads']


        return channel_playlistId
    except requests.exceptions.RequestException as e:
        raise e
    
def get_video_ids(playlistId):

    video_ids = []
    
    pageToken = None

    base_url = f'https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={maxResults}&playlistId={playlistId}&key={API_KEY}'

    try:
        while True:

            url = base_url

            if pageToken:
                url += f"&pageToken={pageToken}"

            response = requests.get(url)

            response.raise_for_status()

            data = response.json()

            for item in data.get('items', []):
                video_id = item['contentDetails']['videoId']
                video_ids.append(video_id)

            pageToken = data.get('nextPageToken')

            if not pageToken:
                break

        return video_ids
        
    except requests.exceptions.RequestException as e:
        raise e

if __name__ == "__main__":
    playlistId = get_playlistId()
    print(get_video_ids(playlistId))

