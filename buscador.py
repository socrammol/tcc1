import sys
import tweepy
#import TwitterSearch
import csv
import os

from TwitterSearch import *
try:

    ts = TwitterSearch(
        consumer_key = '',
        consumer_secret = '',
        access_token = '',
        access_token_secret = ''
     )

    tso = TwitterSearchOrder()
    tso.set_keywords([''])
    tso.set_language('pt')

    for tweet in ts.search_tweets_iterable(tso):
        c = csv.writer(open("data.csv", "wb"))

        c.writerow( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e:
    print(e)
"""""
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
"""

"""""
#coletando twwets
class CustomStreamListener(tweepy.StreamListener):

    def on_status(self, tweet):
        #ler o arquivo csv no disco
        fin = open ('data.csv', 'r')
        fout = open ('data.csv', 'w')
        reader = csv.DictReader(fin, delimiter=',')
        writer = csv.DictWriter(fout, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL,fieldnames=reader.fieldnames)
        writer.writeheader()
        #Quando receber algum status, esta função pode manipular o objeto tweet. Exemplos:
        #print tweet.author.screen_name
        #print tweet.text.encode('utf-8')
        api.create_favorite(tweet.id)
        #inserir em um arquivo csv
        with open(, 'w') as csvfile:

''''''

        #erro com o codigo:", status_code
        return  True
        #nao mata o coletor
    def on_timeout(self):
        print('TEMPO ESGOTADO!')

        return True
        #nao mata o coletor
"""