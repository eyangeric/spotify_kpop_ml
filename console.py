from backend.api.src.adapters.client import Client
from backend.api.src.models.track import Track
from datetime import datetime

track_url = 'https://open.spotify.com/track/6ubzgznl4lqaCYV2kd7ewv?si=deafa76eb6dd482b'
client = Client()
token = client.get_auth_token_params()
track_id = client.extract_track_id_from_url(track_url)
track_details = client.request_track_details(token, track_id)
audio_features = client.request_audio_features(token, track_id)

track = Track(track_details)
# release_date = track.release_date
