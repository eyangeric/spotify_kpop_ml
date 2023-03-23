from src.client import get_authorization_token
from src.audiofeatures import extract_track_id, extract_artists_of_song, extract_track_details, extract_audio_features
from settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

headers = get_authorization_token(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
song_url = 'https://open.spotify.com/track/7fjAIwn4DpKwTEqO08zN9H?si=09cde79b65ee4305'

def test_extract_track_id():
    track_id = extract_track_id(song_url)
    assert track_id == '7fjAIwn4DpKwTEqO08zN9H', 'Not Track ID'

def test_extract_artists_of_song():
    artists_for_song1 = ['Gray', 'Loco']
    artists_for_song2 = ['Paul Kim']
    artists_for_song3 = ['Wendy', 'IU', 'Mamamoo']
    artists_for_song4 = ['Gray', 'Hyolyn', 'Mamamoo', 'Red Velvet']
    assert extract_artists_of_song(artists_for_song1) == 'Gray and Loco'
    assert extract_artists_of_song(artists_for_song2) == 'Paul Kim'
    assert extract_artists_of_song(artists_for_song3) == 'Wendy, IU, and Mamamoo'
    assert extract_artists_of_song(artists_for_song4) == 'Gray, Hyolyn, Mamamoo, and Red Velvet'

def test_extract_track_details():
    track_details = extract_track_details('7fjAIwn4DpKwTEqO08zN9H?', headers)
    assert type(track_details) == dict, 'Not a dictionary'
    assert track_details == {'track': 'BAD BAD (Feat. Tabber, Jay Park)', 'artist': 'CODE KUNST, Tabber, and Jay Park', 'release_date': '2023-03-08', 'Popularity': 51}, 'Failed'

def test_extract_audio_features():
    audio_features = extract_audio_features('7fjAIwn4DpKwTEqO08zN9H', headers)
    assert type(audio_features) == dict, 'Not a dictionary'
    assert audio_features == {'duration_ms': 214507, 'valence': 0.679, 'energy': 0.66, 'key': 4}