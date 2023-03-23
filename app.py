from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
from src.client import get_authorization_token

headers = get_authorization_token(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)

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