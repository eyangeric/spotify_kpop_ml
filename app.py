from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_USERNAME, SPOTIFY_PASSWORD
from src.client import get_authorization_token
from src.audiofeatures import extract_track_id, extract_artists_of_song, extract_track_details, extract_audio_features
from src.lyricfeatures import scrape_lyrics, extract_translated_lyrics, extract_count_for_word, extract_lyric_sentiment, extract_song_lyrics_sentiment

track_url = 'https://open.spotify.com/track/6ubzgznl4lqaCYV2kd7ewv?si=deafa76eb6dd482b'

token = get_authorization_token(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
track_id = extract_track_id(track_url)

#spotify api data
track_details = extract_track_details(track_id, token)
audio_features = extract_audio_features(track_id, token, keys = ['duration_ms', 'valence', 'energy', 'key'])

#spotify lyric data scrape
lyrics = scrape_lyrics(track_url, SPOTIFY_USERNAME, SPOTIFY_PASSWORD)
translated_lyrics = extract_translated_lyrics(lyrics)
yeah_word_count = extract_count_for_word(translated_lyrics, 'yeah')
sentiment_score = extract_song_lyrics_sentiment(translated_lyrics)
lyric_data = {'lyric_word_yeah': yeah_word_count, 'lyric_sentiment_score': sentiment_score}

#all track info data
track_data = {'track_id': track_id}
track_data.update(track_details)
track_data.update(audio_features)
track_data.update(lyric_data)








# app = Flask(__name__, static_folder='static', template_folder = 'views')
# app.config['SECRET_KEY'] = 'd5qtfNZWXkU8VPCvswsCwER7Sh6UUGse'

# Bootstrap(app)

# class SpotifyUrlForm(FlaskForm):
#     name = StringField('Paste your Spotify song URL here.', validators=[DataRequired()])
#     submit = SubmitField('Submit')

# @app.route('/', methods = ['GET', 'POST'])
# def index():
#     form = SpotifyUrlForm()
#     message = ''
#     if request.method == 'POST':
#         spotify_song_url = request.form.get('name')
#         breakpoint()
#         return f"URL: {spotify_song_url}"
#     return render_template('index.html', form = form, message = message)

# app.run(debug = True)