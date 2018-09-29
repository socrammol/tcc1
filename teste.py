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
    #import pdb; pdb.set_trace()
        for tweet in ts.search_tweets_iterable(tso):
            # c = csv.writer(open("data.csv", "wb"))
             #c.writerow('@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text']))
             print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

#except TwitterSearchException as e:
#    print(e)