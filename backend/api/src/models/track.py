from datetime import datetime

class Track:
    __table__ = 'tracks'
    columns = ['id', 'spotify_track_id', 'name', 'release_date', 'artists', 'popularity', 'duration_ms', 'valence', 'energy', 'key', 'lyric_word_yeah', 'lyric_sentiment_score']

    def __init__(self, dict):
        for key, value in dict.items():
            setattr(self, key, value)
        self._release_date = self.extract_release_date()
        self._artists = [artist['name'] for artist in dict['artists']]

    def extract_release_date(self):
        release_date = self['album']['release_date']
        return release_date

    @property
    def release_date(self):
        return self._release_date
    
    @release_date.setter
    def release_date(self, release_date):
        self._release_date = datetime.strptime(release_date, '%Y-%m-%d').date()

    @property
    def artists(self):
        return self._artists
    
    @artists.setter
    def artists(self, artists):
        artists_num = len(artists)
        if artists_num == 1:
            artist_names = artists[0]
        elif artists_num == 2:
            artist_names = ' and '.join(artists)
        else:
            last_artist = artists[-1:][0]
            artists_before_last = artists[:-1]
            artists_before_last_str = ', '.join(artists_before_last)
            artist_names = artists_before_last_str + ', and ' + last_artist
        self._artists = artist_names

