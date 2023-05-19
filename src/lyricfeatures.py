from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def scrape_lyrics(URL, USERNAME, PASSWORD):
    options = Options()
    # options.add_argument("--window-size=1920x1080")
    # options.add_argument("--verbose")
    options.add_argument('headless')
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)
    
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()
    
    uname = driver.find_element("id", "login-username") 
    uname.send_keys(USERNAME)

    pword = driver.find_element("id", "login-password") 
    pword.send_keys(PASSWORD)
    
    driver.find_element("id", "login-button").click()
    
    time.sleep(5)
    lyrics = driver.find_element(By.CLASS_NAME, "Q3OKWaFrTVTIRZyG05Gh").text
    return lyrics

def extract_translated_lyrics(LYRICS, LANGUAGE_FROM_GOOGLE_SERVICE_URL = 'translate.google.co.kr', LANGUAGE_TO = 'en'):
    translator = Translator(service_urls = [LANGUAGE_FROM_GOOGLE_SERVICE_URL])
    translated_lyric_lines = []
    lyric_lines = LYRICS.split('\n')
    for lyric_line in lyric_lines:
        try:
            translation = translator.translate(lyric_line, dest = LANGUAGE_TO)
            translated_lyric = translation.text
            translated_lyric_lines.append(translated_lyric)
        except:
            pass
    return translated_lyric_lines

def extract_count_for_word(LYRIC_LINES, WORD = 'yeah'):
    count = 0
    lyric_lines_lowercase = [lyric_line.lower() for lyric_line in LYRIC_LINES]
    for lyric in lyric_lines_lowercase:
        words = lyric.split(' ')
        for word in words:
            if word == WORD.lower():
                count += 1
    return count

def extract_lyric_sentiment(LYRIC_LINE):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_stats = sid_obj.polarity_scores(LYRIC_LINE)
    sentiment_score = sentiment_stats['compound']
    return sentiment_score

def extract_song_lyrics_sentiment(LYRIC_LINES, LANGUAGE_FROM_GOOGLE_SERVICE_URL = 'translate.google.co.kr'):
    # translator = Translator(service_urls = [LANGUAGE_FROM_GOOGLE_SERVICE_URL])
    lyric_lines_lowercase = [lyric_line.lower() for lyric_line in LYRIC_LINES]

    try:
        lyric_lines_lowercase.remove('lyrics')
    except:
        pass

    sentiment_scores = []
    for lyric_line in lyric_lines_lowercase:
        sentiment_scores.append(extract_lyric_sentiment(lyric_line))

        # #Would be ideal to check if lyric line is English, but there's a limit to how much Google API will let you make a request
        # try:
        #     lang_detect_output = str(translator.detect(lyric_line))
        #     index_start = lang_detect_output.find('lang=') + len('lang=')
        #     detected_language = lang_detect_output[index_start:(index_start + 2)]
        #     if detected_language == 'en':
        #         sentiment_scores.append(extract_lyric_sentiment(lyric_line))
        # except:
        #     pass
    return sum(sentiment_scores)/len(sentiment_scores)

            

