# import pandas as pd
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn import metrics
# from sklearn.model_selection import cross_val_predict
# dataset = pd.reader_csv('data.csv')
# dataset.count()

# tweets = dataset ['text'].values
# classes = dataset['Classificacao'].values
# vectorizer = CountVectorizer(analyzer='word')
# freq_tweets = vectorizer.fit_transform(tweets)
# modelo = MultinomialNB()
# modelo.fit(freq_tweets, classes)
# testes = ['Esse governo está no início, vamos ver o que vai dar',
#          'Estou muito feliz com o governo de Minas esse ano',
#          'O estado de Minas Gerais decretou calamidade financeira!!!',
#          'A segurança desse país está deixando a desejar',
#          'O governador de Minas é do PT']
# freq_testes = vectorizer.transform(testes)
# modelo.predict(freq_testes)
# resultado = cross_val_predict(modelo, freq_tweets, classes, cv=10)

import csv
import os
import sys
from TwitterSearch import *
try:

    ts = TwitterSearch(
        consumer_key='zcQ8yEGrCpUL7AiJC7XSjP0ib',
        consumer_secret='LicwyVCoenr4ITeUuF1Y55NpXoaeIJXqA4fN23LKSBIOj4cDVC',
        access_token='117869496-Biraq1HNZhVpTrPtCA0MgvXUw3YxFzkEjeEyyKlK',
        access_token_secret='2mM4lUXbhgRvG4lgkdzWYqcRxStYPZpmloTHoOlRoUKZ5'
    )

    tso = TwitterSearchOrder()
    tso.set_keywords(['#galo'])
    tso.set_language('pt')
    for tweet in ts.search_tweets_iterable(tso):
             print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
             #c = csv.writer(open("data.csv", "wb"))
             #c.writerow('@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text']))

except TwitterSearchException as e:
    print(e)