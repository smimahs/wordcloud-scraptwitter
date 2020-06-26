#!pip install twitter_scraper
#!pip install wordcloud
from twitter_scraper import get_tweets

file = open('output.txt','w')
t=[]
for tweet in get_tweets('username'):
    t.append(tweet['text'])
    file.write(tweet['text'])

file.close()

