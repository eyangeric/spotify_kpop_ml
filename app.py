from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import pickle
import pandas as pd
from settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_USERNAME, SPOTIFY_PASSWORD, DATABASE
from src.client import get_authorization_token
from src.audiofeatures import extract_track_id, extract_artists_of_song, extract_track_details, extract_audio_features
from src.lyricfeatures import scrape_lyrics, extract_translated_lyrics, extract_count_for_word, extract_lyric_sentiment, extract_song_lyrics_sentiment
from src.track import Track
from src.outcome import Outcome
import psycopg2

track_url = 'https://open.spotify.com/track/6ubzgznl4lqaCYV2kd7ewv?si=deafa76eb6dd482b'

token = get_authorization_token(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
track_id = extract_track_id(track_url)
track = Track(('track_id', track_id))

#spotify api data
track_details = extract_track_details(track_id, token)
for track_info, value in track_details.items():
    setattr(track, track_info, value)

audio_features = extract_audio_features(track_id, token, keys = ['duration_ms', 'valence', 'energy', 'key'])
for audio_feature, value in audio_features.items():
    setattr(track, audio_feature, value)

#spotify lyric data scrape
lyrics = scrape_lyrics(track_url, SPOTIFY_USERNAME, SPOTIFY_PASSWORD)
translated_lyrics = extract_translated_lyrics(lyrics)
yeah_word_count = extract_count_for_word(translated_lyrics, 'yeah')
setattr(track, 'lyric_word_yeah', yeah_word_count)
sentiment_score = extract_song_lyrics_sentiment(translated_lyrics)
setattr(track, 'lyric_sentiment_score', sentiment_score)

# extract features and send through model
track_features = pd.DataFrame([track.__dict__])[['Popularity', 'duration_ms', 'valence',  'energy', 'key', 
            'lyric_word_yeah', 'lyric_sentiment_score']]
ss = pickle.load(open(f"src/standardscaler.pkl", 'rb'))
model = pickle.load(open(f"src/svm.pkl", 'rb'))
X_test_scaled = ss.fit_transform(track_features)
prediction = model.predict(X_test_scaled)[0]
outcome = Outcome(prediction)

all_track_info = {}
for track_dict in [track.__dict__.items(), outcome.__dict__.items()]:
    for key, value in track_dict:
        all_track_info[key] = value

final_output = pd.DataFrame([all_track_info])

app = Flask(__name__, static_folder='static', template_folder = 'views')
app.config['SECRET_KEY'] = 'd5qtfNZWXkU8VPCvswsCwER7Sh6UUGse'

app.config.from_mapping(
    DATABASE = DATABASE
)

Bootstrap(app)

class SpotifyUrlForm(FlaskForm):
    name = StringField('Paste your Spotify song URL here.', validators=[DataRequired()])
    actual_class = StringField('What kind of song is this? Enter 0 for Donald Feelz, 1 for Eric Feelz, and 2 for Eric/Donald Feelz.', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = SpotifyUrlForm()
    message = ''
    if request.method == 'POST':
        spotify_song_url = request.form.get('name')
        spotify_song_outcome_class = int(request.form.get('actual_class'))
    
    track_id = extract_track_id(spotify_song_url)



    conn = psycopg2.connect(database = app.config['DATABASE'])
    # cursor = conn.cursor()
    # insert_sql = 'INSERT INTO api_data (ID, track_id, track_name, artist, release_date, Popularity, duration_ms, valence, energy, key, lyric_word_yeah, lyric_sentiment_score) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
    # insert_data = tuple(value for value in all_track_info.values())
    # cursor.execute(insert_sql, insert_data)
    # conn.commit()

    # statement = f"{track.track_name} by {track.artist} is predicted to be a {outcome.outcome} type of song."
    return render_template('index.html', form = form, message = message)

app.run(debug = True)