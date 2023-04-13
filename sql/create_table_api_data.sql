CREATE TABLE api_data (
ID serial PRIMARY KEY,
track_id VARCHAR,
track_name VARCHAR,
artist VARCHAR,
release_date VARCHAR,
Popularity INT,
duration_ms BIGINT,
valence FLOAT,
energy FLOAT,
key INT,
lyric_word_yeah INT,
lyric_sentiment_score FLOAT,
prediction INT,
outcome VARCHAR
);