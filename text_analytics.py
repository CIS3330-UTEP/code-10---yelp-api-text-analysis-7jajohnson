import nltk
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import  SentimentIntensityAnalyzer
reviews = open('ice_cream_reviews.txt')
s_words = stopwords.words('english')
print(s_words)
for review in reviews:
    tokens = nltk.word_tokenize(review)
    # print(tokens)
    pos_tags = nltk.pos_tag(tokens)
    # print(pos_tags)
# JJ JJS JJR
    new_text = []
    for tag in pos_tags:
        # if tag[1] == "NN" or tag[1] == "NNP" or tag[1] == "NNS":
        #     # print(tag)
        #     pass
        if tag[0] not in  s_words:
            new_text.append(tag[0])
    print(review)
    print(" ".join(new_text))
