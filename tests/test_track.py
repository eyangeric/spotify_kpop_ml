from src.track import Track

def test_initialize_track():
    track = Track(('track_id', '6ubzgznl4lqaCYV2kd7ewv'))
    assert track.__dict__ == {'track_id': '6ubzgznl4lqaCYV2kd7ewv'}

def test_add_in_kwargs():
    track = Track(('track_id', '6ubzgznl4lqaCYV2kd7ewv'))
    for audio_feature, value in {'track_name': 'Tasty x Tasty', 'artist': 'Loco and GRAY', 'release_date': '2022-10-14', 'Popularity': 40, 'duration_ms': 169718, 'valence': 0.912, 'energy': 0.815, 'key': 0, 'lyric_word_yeah': 1, 'lyric_sentiment_score': 0.2833215384615384}.items():
        setattr(track, audio_feature, value)
    assert track.__dict__ == {'track_id': '6ubzgznl4lqaCYV2kd7ewv', 'track_name': 'Tasty x Tasty', 'artist': 'Loco and GRAY', 'release_date': '2022-10-14', 'Popularity': 40, 'duration_ms': 169718, 'valence': 0.912, 'energy': 0.815, 'key': 0, 'lyric_word_yeah': 1, 'lyric_sentiment_score': 0.2833215384615384}
