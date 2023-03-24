class Track:
    columns = ['track_id', 'track_name', 'artist', 'release_date', 'Popularity', 'duration_ms', 'valence', 'energy', 'key', 'lyric_word_yeah', 'lyric_sentiment_score']
    def __init__(self, values):
        key = values[0]
        value = values[1]
        if key not in self.columns:
            raise ValueError(f'{key} not in columns') 
        setattr(self, key, value)