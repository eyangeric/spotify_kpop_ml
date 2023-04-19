import requests
from settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_USERNAME, SPOTIFY_PASSWORD

class Client:
    TOKEN_URL = 'https://accounts.spotify.com/api/token'
    TRACK_ROOT_URL = 'https://api.spotify.com/v1/tracks/'
    AUDIO_FEATURES_ROOT_URL = 'https://api.spotify.com/v1/audio-features/'

    def get_auth_token_params(self):
        response = requests.post(self.TOKEN_URL, data = {'grant_type' : 'client_credentials'}, auth = (SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)) 
        token_json = response.json()
        access_token = token_json['access_token']
        token_type = token_json['token_type']
        return {'Authorization': f"{token_type} {access_token}"}

    def extract_track_id_from_url(self, track_url):
        str_with_track_id = track_url.split('?si=')[0]
        track_id = str_with_track_id.split('track/')[1]
        return track_id
    
    def request_track_details(self, token, track_id):
        url = self.TRACK_ROOT_URL + track_id
        response = requests.get(url, headers = token)
        track_details = response.json()
        return track_details
    
    def request_audio_features(self, token, track_id):
        url = self.AUDIO_FEATURES_ROOT_URL + track_id
        response = requests.get(url, headers = token)
        audio_details = response.json()
        return audio_details
