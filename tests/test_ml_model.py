import pickle
import pandas as pd

track_details = {'track_id': '6ubzgznl4lqaCYV2kd7ewv', 'track_name': 'Tasty x Tasty', 'artist': 'Loco and GRAY', 'release_date': '2022-10-14', 'Popularity': 40, 'duration_ms': 169718, 'valence': 0.912, 'energy': 0.815, 'key': 0, 'lyric_word_yeah': 1, 'lyric_sentiment_score': 0.2833215384615384}

track_features = pd.DataFrame([track_details])[['Popularity', 'duration_ms', 'valence',  'energy', 'key', 
            'lyric_word_yeah', 'lyric_sentiment_score']]

def test_ml_model_run():
    ss = pickle.load(open(f"src/standardscaler.pkl", 'rb'))
    model = pickle.load(open(f"src/svm.pkl", 'rb'))
    X_test_scaled = ss.fit_transform(track_features)
    prediction = model.predict(X_test_scaled)
    assert prediction[0] in [0, 1, 2]