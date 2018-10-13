from TwitterSearch import *
try:

    ts = TwitterSearch(
        consumer_key='zcQ8yEGrCpUL7AiJC7XSjP0ib',
        consumer_secret='LicwyVCoenr4ITeUuF1Y55NpXoaeIJXqA4fN23LKSBIOj4cDVC',
        access_token='117869496-Biraq1HNZhVpTrPtCA0MgvXUw3YxFzkEjeEyyKlK',
        access_token_secret='2mM4lUXbhgRvG4lgkdzWYqcRxStYPZpmloTHoOlRoUKZ5'
    )

    tso = TwitterSearchOrder()
    tso.set_keywords(['#america-mg'])
    tso.set_language('pt')
    for tweet in ts.search_tweets_iterable(tso):
             print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] + tweet['created_at'] ) )
             #with open("data.csv","a") as _file:
             #with open("teste.csv","a") as _file:
             #with open("bd/Atletico/AtleticoMG.csv","a") as _file:
             with open("bd/America/america.csv", "a") as _file:
             #with open("bd/cruzeiro/cruzeiro.csv","a") as _file:
                 _file.write( '@%s tweeted: %s' % ( tweet['user']['screen_name'] + ";", tweet['text'] + ";" + tweet['created_at']+ "\n"  ) )

except TwitterSearchException as e:
    print(e)