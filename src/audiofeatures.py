import requests
from src.client import get_authorization_token

def extract_track_id(TRACK_URL):
    str_with_track_id = TRACK_URL.split('?si=')[0]
    track_id = str_with_track_id.split('track/')[1]
    return track_id

def extract_artists_of_song(ARTISTS):
    artists_num = len(ARTISTS)
    if artists_num == 1:
        artist_names = ARTISTS[0]
    elif artists_num == 2:
        artist_names = ' and '.join(ARTISTS)
    else:
        last_artist = ARTISTS[-1:][0]
        artists_before_last = ARTISTS[:-1]
        artists_before_last_str = ', '.join(artists_before_last)
        artist_names = artists_before_last_str + ', and ' + last_artist
    return artist_names

def extract_track_details(TRACK_ID, TOKEN):
    url = f"https://api.spotify.com/v1/tracks/{TRACK_ID}"
    response = requests.get(url, headers = TOKEN)
    track_details = response.json()
    track_name = track_details['name']
    release_date = track_details['album']['release_date']
    popularity = track_details['popularity']
    artists = [artist['name'] for artist in track_details['artists']]
    artist_names = extract_artists_of_song(artists)
    track_info = {'track_name': track_name, 'artist': artist_names, 'release_date': release_date, 'Popularity': popularity}
    return track_info

def extract_audio_features(TRACK_ID, TOKEN, keys = ['duration_ms', 'valence', 'energy', 'key']):
    url = f"https://api.spotify.com/v1/audio-features/{TRACK_ID}"
    response = requests.get(url, headers = TOKEN)
    song_details = response.json()
    return {key: song_details[key] for key in keys if key in song_details.keys()}