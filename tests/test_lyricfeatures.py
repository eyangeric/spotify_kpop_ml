from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from settings import SPOTIFY_USERNAME, SPOTIFY_PASSWORD
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator
from src.lyricfeatures import scrape_lyrics, extract_translated_lyrics, extract_count_for_word, extract_lyric_sentiment, extract_song_lyrics_sentiment

language_from_google_service_url = 'translate.google.co.kr'
language_to = 'en'
song_url = 'https://open.spotify.com/track/6ubzgznl4lqaCYV2kd7ewv?si=deafa76eb6dd482b'
lyric = '서울숲 한강 또 어디든지 상쾌하고 재밌어'
lyrics = "Lyrics\n아무 계획 없이\n괜히 집을 나섰지\n고민해 뭘 먹을지\n맛있는 거 옆에는 역시\n애매한 건 싫어 전부 마시고 Having fun\n서울숲 한강 또 어디든지 상쾌하고 재밌어\n뭘 먹어도 Sprite 하나 더\n시원하면 눈 감아줘\n오늘이 Day day\n빨리 하얀색의 별들을 따다 줘\n맛있는 거, 맛있는 거\n맛있는 거 옆에 Sprite!\n맛있는 거 옆에, 맛있는 거\n맛있는 거 옆에\n맛있는 거, 맛있는 거\n맛있는 거 옆에 Sprite!\n맛있는 거 옆에, 맛있는 거\n맛있는 거 옆에\n안 놓쳐\n내가 하고 싶은 거, 내가 먹고 싶은 거\nYou got a thumbs-up\n들어와 너도 같이하게 될 거야\nSprite\nSprite\n동방에서부터 달랐지\n소음 아니고 음악이었지\nGood vibes only\n좋은 사람들 있기에 십 년을 달렸지\n필요 없어 각본, 드라마야 완전\nU just eatin' 팝콘\n편히 앉아 관전, 목마르면 한 잔\n들이키자 Havin' fun 재밌어\nReal recognize real yeah 멋있는 놈\n옆엔 붙어 다니지 또 멋있는 놈\n하얀 도화지에 초록색과 노란색으로 그린 그림\n끼리끼린 원래 과학이죠\n맛있는 거, 맛있는 거\n맛있는 거 옆에 Sprite!\n맛있는 거 옆에, 맛있는 거\n맛있는 거 옆에\n맛있는 거, 맛있는 거\n맛있는 거 옆에 Sprite!\n맛있는 거 옆에, 맛있는 거\n맛있는 거 옆에\n안 놓쳐\n내가 하고 싶은 거, 내가 먹고 싶은 거\nYou got a thumbs-up\n들어와 너도 같이하게 될 거야\nSprite\nSprite\n한 캔 따고 한 캔 더\nI found a love making me loco\n하늘이 깜깜해도\n다 마시고 같이 구름을 넘어\nEverybody snap your fingers, snap your fingers\n이 순간을 즐긴다면\n상쾌함에 빠져들어 날 물 들여\n함께해 All day and night\n안 놓쳐\n내가 하고 싶은 거, 내가 먹고 싶은 거\nYou got a thumbs-up\n들어와 너도 같이하게 될 거야\nSprite\nSprite\nSprite!"
translated_lyrics = ['Lyrics', 'Without any plan', 'I left home for nothing', 'What to eat', 'Next to the delicious thing', "I don't like it ambiguous, drink all, having fun", 'Seoul Forest Han River is refreshing and fun anywhere else', 'No matter what you eat, one more Sprite', 'If you cool it, close your eyes', 'Today is the day day', 'Get the white stars quickly', 'Delicious, delicious', 'Sprite next to the delicious thing!', 'Next to the delicious thing, the delicious thing', 'Next to the delicious', 'Delicious, delicious', 'Sprite next to the delicious thing!', 'Next to the delicious thing, the delicious thing', 'Next to the delicious', 'Not missed', 'What I want to do, what I want to eat', 'You got a thumbs-up', 'You will come in and you will be together', 'Sprite', 'Sprite', 'It was different from the East', 'It was music, not noise', 'Good vibes only', 'I have been running for 10 years because there are good people', "I don't need it, the script, the drama", "U Just Eatin 'Popcorn", 'Sit comfortably, watch, thirst, a drink', "Let's go in, havin 'fun is fun", 'Real Recognize Real Yeah cool guy', 'I stick to the side and the cool guy', 'Pictures drawn with green and yellow on white drawing paper', "It's the original science of each other", 'Delicious, delicious', 'Sprite next to the delicious thing!', 'Next to the delicious thing, the delicious thing', 'Next to the delicious', 'Delicious, delicious', 'Sprite next to the delicious thing!', 'Next to the delicious thing, the delicious thing', 'Next to the delicious', 'Not missed', 'What I want to do, what I want to eat', 'You got a thumbs-up', 'You will come in and you will be together', 'Sprite', 'Sprite', 'One more can', 'I found a love making me loco', 'Even if the sky is dark', 'Drink everything and go beyond the clouds', 'Everybody snap your fingers, snap your fingers', 'If you enjoy this moment', 'I fall into freshness and water', 'All Day and Night together', 'Not missed', 'What I want to do, what I want to eat', 'You got a thumbs-up', 'You will come in and you will be together', 'Sprite', 'Sprite', 'Sprite!']

def test_scrape_lyrics_gets_string():
    lyrics = scrape_lyrics(song_url, SPOTIFY_USERNAME, SPOTIFY_PASSWORD)
    assert type(lyrics) == str

def test_extract_translated_lyrics():
    translated_lyrics = extract_translated_lyrics(lyrics)
    breakpoint()
    assert type(translated_lyrics) == str

def test_extract_count_for_word():
    word_count = extract_count_for_word(translated_lyrics, 'yeah')
    assert word_count == 1

def test_extract_lyric_sentiment():
    lyric = 'Seoul Forest Han River is refreshing and fun anywhere else'
    sentiment = extract_lyric_sentiment(lyric)
    assert type(sentiment) == float
    assert sentiment == 0.5106

def test_extract_song_lyrics_sentiment():
    breakpoint()
    sentiment_score = extract_song_lyrics_sentiment(translated_lyrics)
    breakpoint()
    assert type(sentiment_score) == float