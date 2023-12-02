from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
import yelpapi
client_id = 'pT6LvQcfOarpa_4EsCvGQ'
api_key = 'pdy7AtRZpar8WynlDxaXhy1eF2qgLxdQJ3QGKGJpcuRPcwAvKevxeun4BkZe2UUYrSisl4M5xU7n9zYSURy8x5gdBwtN_GGySNqSB0HzzJEgbDDjqAeWUo2LGUZMZXYx'

analyzer = SentimentIntensityAnalyzer()
data = open('tacos_reviews.txt')

for review in data:
    # print(review)
    sen_score = analyzer.polarity_scores(review)
    print(review)
    print(sen_score)

