from datetime import datetime
from settings import SPOTIFY_USERNAME, SPOTIFY_PASSWORD
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class Track:
    __table__ = 'tracks'
    columns = ['id', 'url', 'spotify_track_id', 'name', 'release_date', 'artists', 'popularity', 'duration_ms', 'valence', 'energy', 'key', 'lyric_word_yeah', 'lyric_sentiment_score']

    def __init__(self, dict):
        for key, value in dict.items():
            setattr(self, key, value)
        self.release_date = self.extract_release_date()
        self.artist_names = self.extract_artist_names()

    def extract_release_date(self):
        release_date = self.album['release_date']
        return release_date
    
    def extract_artist_names(self):
        artists_list = [artist['name'] for artist in self.artists]
        artists_num = len(artists_list)
        if artists_num == 1:
            artist_names_str = artists_list[0]
        elif artists_num == 2:
            artist_names_str = ' and '.join(artists_list)
        else:
            last_artist = artists_list[-1:][0]
            artists_before_last = artists_list[:-1]
            artists_before_last_str = ', '.join(artists_before_last)
            artist_names_str = artists_before_last_str + ', and ' + last_artist
        return artist_names_str

    @property
    def release_date(self):
        return self._release_date
    
    @release_date.setter
    def release_date(self, release_date):
        self._release_date = datetime.strptime(release_date, '%Y-%m-%d').date()

    def scrape_lyrics(self):
        options = Options()
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--verbose")
        # options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
        # driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        driver.get(self.url)
        
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        
        uname = driver.find_element("id", "login-username") 
        uname.send_keys(SPOTIFY_USERNAME)

        pword = driver.find_element("id", "login-password") 
        pword.send_keys(SPOTIFY_PASSWORD)
        
        driver.find_element("id", "login-button").click()
        
        time.sleep(5)
        lyrics = driver.find_element(By.CLASS_NAME, "Q3OKWaFrTVTIRZyG05Gh").text
        return lyrics


