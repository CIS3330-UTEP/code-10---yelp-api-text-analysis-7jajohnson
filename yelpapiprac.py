from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
import pandasprac as pd
import json
from yelpapi import YelpAPI
api_key = 'pdy7AtRZpar8WynlDxaXhy1eF2qgLxdQJ3QGKGJpcuRPcwAvKevxeun4BkZe2UUYrSisl4M5xU7n9zYSURy8x5gdBwtN_GGySNqSB0HzzJEgbDDjqAeWUo2LGUZMZXYx'
yelp_api = YelpAPI(api_key)
s_term = 'Food'
loc = 'El Paso, TX'

# result = yelp_api.search_query(
#     term=s_term,
#     location=loc,
#     sort_by='rating',
#     limit=50
# )
# df = pd.DataFrame.from_dict(result['businesses'])
# print(df)

# df.to_csv('result_api.csv',index=False)

