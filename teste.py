import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
dataset = pd.reader_csv('data.csv')
dataset.count()
tweets = dataset ['text'].values
classes = dataset['Classificacao'].values
vectorizer = CountVectorizer(analyzer='word')
freq_tweets = vectorizer.fit_transform(tweets)
modelo = MultinomialNB()
modelo.fit(freq_tweets, classes)
testes = ['Esse governo está no início, vamos ver o que vai dar',
          'Estou muito feliz com o governo de Minas esse ano',
          'O estado de Minas Gerais decretou calamidade financeira!!!',
          'A segurança desse país está deixando a desejar',
          'O governador de Minas é do PT']
freq_testes = vectorizer.transform(testes)
modelo.predict(freq_testes)
resultado = cross_val_predict(modelo, freq_tweets, classes, cv=10)

import csv
import os
import sys