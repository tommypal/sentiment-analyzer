import matplotlib.pyplot as plt
import pandas as pd
from textblob import TextBlob
from newspaper import Article
import ssl
import nltk
# WARNING: The following line disables SSL certificate verification.
# It is used here to bypass SSL certificate issues during development.
ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt_tab')
def analyze_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return article.summary
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return None
#print(text)
def get_sentiment(text):
    if text is None:
        return None
    blob = TextBlob(text)
    return  blob.sentiment.polarity
urls = [
    'https://www.cnn.com/2024/08/26/sport/michigan-allegations-ncaa-sign-stealing-investigation-spt/index.html',
    'https://www.cnn.com/2024/01/08/sport/2024-cfp-national-championship-michigan-wolverines-washington-huskies-spt-intl/index.html'
]
dates = [
    '2024-08-26',
    '2024-01-09'
]
sentiments = [
    
]
for url in urls:
    summary = analyze_article(url)
    if summary is None:
        sentiments.append(None)
    else:
        sentiment = get_sentiment(summary)
        sentiments.append(sentiment)

valid_dates = [date for date, sentiment in zip(dates, sentiments) if sentiment is not None]
valid_sentiments = [sentiment for sentiment in sentiments if sentiment is not None]
#creates data from without the None values
df = pd.DataFrame({
    'Date': pd.to_datetime(dates),
    'Sentiment': sentiments
})
df = df.sort_values('Date')

#plot sentiment over time
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Sentiment'], marker='o')
plt.title('Sentiment Analysis Over Time')
plt.xlabel('Date')
plt.ylabel('Sentiment Polarity')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

