
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
from textblob import TextBlob
import pandas as pd
import json
from yelpapi import YelpAPI
api_key = 'pdy7AtRZpar8WynlDxaXhy1eF2qgLxdQJ3QGKGJpcuRPcwAvKevxeun4BkZe2UUYrSisl4M5xU7n9zYSURy8x5gdBwtN_GGySNqSB0HzzJEgbDDjqAeWUo2LGUZMZXYx'
yelp_api = YelpAPI(api_key)

df = pd.DataFrame()
alias = []
revtext = []


s_term = 'Pasta'
loc = 'El Paso, TX'
data =yelp_api.search_query(s_term=s_term,
                   location=loc,
                   limit=20)
for item in data['businesses']:
    review_response = yelp_api.reviews_query(id=item.get('alias'))
    for review in review_response['reviews']:
        alias.append(item.get('alias'))
        revtext.append(review.get('text'))
data = {"Alias":alias,'Review':revtext}
df = pd.DataFrame(pd.DataFrame.from_dict(data))
score = 0
count = 0
for review in df['Review']:
    blob = TextBlob(review)
    print(review)
    print(blob.sentiment.polarity)
    print('\n\n\n')
    score += blob.sentiment.polarity
    count += 1
print(f"Average Polarity Score: {round(score / count,4)}")



from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('stopwords')


all_reviews = ' '.join(df['Review'])
stop_words = set(stopwords.words('english'))

all_words = [word.lower() for word in word_tokenize(all_reviews) if word.isalpha() and word.lower() not in stop_words]

word_counts = Counter(all_words)

most_common_words = word_counts.most_common(10)
print("Top 10 Most Common Words:")
for word, count in most_common_words:
    print(f"{word}: {count}")
