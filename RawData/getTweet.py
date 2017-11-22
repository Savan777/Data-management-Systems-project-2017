import tweepy
import json
import string
import pandas as pd
import  datetime

# Twitter API credentials
consumerKey = "CFzT0X0jaOJDXcBTzVtaviY9d"
consumerSecret = "TyZogohaB74ITobQMFTp5Z1BMwXIfFnoDWF2f7fkmUJ5BRluem"
tokenKey = "3137614402-qnvVpqY2cDoFjaQqKLvHgt18N6aEikoN3Qn532f"
tokenSecret = "sZbQNibpzn4PgpBvjcr53bhYnEpRjvA7cZgVK8EbgSEpX"

# Twitter only allows access to a users most recent 3240 tweets with this method
def get_tweets(screen_name):

    # authorize twitter and initialize tweepy
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(tokenKey, tokenSecret)
    api = tweepy.API(auth)

    # make initial request for most recent tweets (max 20)
    newTweets = api.user_timeline(screen_name=screen_name)

    tweetfile = open("tweets.txt","w")
#parsing tweet and printing it o txt file
    tweets_data = []
    for tweet in newTweets:
        tweet = get_data(tweet)

        #cleaning the json
        tweet['displayname'] = filter(lambda x: x in string.printable, tweet['displayname'] )
        tweet['message'] = filter(lambda x: x in string.printable, tweet['message'])
        tweet['text_id'] = filter(lambda x: x in string.printable, tweet['text_id'])
        tweet['st'] = filter(lambda x: x in string.printable, tweet['st'])
        tweet['lt'] = filter(lambda x: x in string.printable, tweet['lt'])
        tweet['summary'] = filter(lambda x: x in string.printable, tweet['summary'])
        tweet['country'] = filter(lambda x: x in string.printable, tweet['country'])
        tweet['datecreated'] = datetime.datetime.now().date()

        #adding the data to array
        tweets_data.append(tweet)

    #creating dataframe
    data = pd.DataFrame.from_records(tweets_data)
    data.to_csv('data.csv', index=False) #writing to csv
    tweetfile.close()

#extracts certain things from the tweet
def get_data(tweet):
    data = {}
    data['displayname'] = tweet.user.screen_name
    data['message'] = tweet.text
    data['datecreated'] = tweet.created_at #need to get the time from the time stamp to put in the times column in filter table
    data['user_id'] = tweet.user.id
    data['text_id'] = tweet.id_str
    data['st'] = tweet.source
    data['lt'] = tweet.user.location
    data['summary'] = tweet.user.description
    data['followers_count'] = tweet.user.followers_count
    data['friends_count'] = tweet.user.friends_count
    data['profileaddress'] = tweet.user.location
    data['country'] = tweet.user.time_zone
    data['favourites_count'] = tweet.favorite_count
    data['retweet_count'] = tweet.retweet_count

    for hashtag in tweet.entities["hashtags"]:  # iterate over the list
        data['hashtags'] = (hashtag["text"])

    return data

if __name__ == '__main__':
    # passing in the username of the account we want to grab tweets from
    get_tweets("@realDonaldTrump")