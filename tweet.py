import twitter

consumer_key = 'gvei0oIX1e7llzjYnsYuq6mO6'
consumer_secret = 'Wa3LuvRmRkIpRWUvhAUpSZI9IwB3mFZo8HjjU6LvfH31lNOulD'
access_token = '1004266754846097408-KJgMLiyONMTYvTF91uxZiv7tTKwu7S'
access_secret = 'Oo0NPQgucIQvcb3JqTktWoq0rT9EGb93DNeKwSCunqPsd'

api = twitter.Api(consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token_key=access_token,
                    access_token_secret=access_secret)

def getLatestTweets():
    list = []
    i=0
    while i < 10:
        for line in api.GetStreamSample(stall_warnings=True):
             tweet={'created_at':line['created_at'],
                    'text':line['text']}
             list.append(tweet)
             i = i+1
             if i >= 100:
                 break
    return list
