from settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_USERNAME, SPOTIFY_PASSWORD
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from src.lyricfeatures import scrape_lyrics, extract_translated_lyrics, extract_count_for_word, extract_song_lyrics_sentiment
from src.client import get_authorization_token
from src.audiofeatures import extract_track_id, extract_track_details, extract_audio_features

track_url = 'https://open.spotify.com/track/6ubzgznl4lqaCYV2kd7ewv?si=deafa76eb6dd482b'

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

lyrics = ''
while lyrics == '':
    try:
        lyrics = scrape_lyrics(track_url, SPOTIFY_USERNAME, SPOTIFY_PASSWORD)
        translated_lyrics = extract_translated_lyrics(lyrics)
        yeah_word_count = extract_count_for_word(translated_lyrics, 'yeah')
        sentiment_score = extract_song_lyrics_sentiment(translated_lyrics)
    except:
        print('This song does not have lyrics in Spotify yet.')
        break

print(lyrics)


# token = get_authorization_token(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
# track_id = extract_track_id(track_url)
# track_details = extract_track_details(track_id, token)

track_details = extract_track_details(track_id, token)
audio_features = extract_audio_features(track_id, token, keys = ['duration_ms', 'valence', 'energy', 'key'])
