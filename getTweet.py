import tweepy 
import json

# Twitter API credentials
consumerKey = "Put your consumer key here"
consumerSecret = "Put your consumer secret key here"
tokenKey = "Put your token key here"
tokenSecret = "Put your token secret key here"

# Twitter only allows access to a users most recent 3240 tweets with this method
def get_tweets(screen_name):

    # authorize twitter and initialize tweepy
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(tokenKey, tokenSecret)
    api = tweepy.API(auth)

    # initialize a list to hold all the Tweets
    allTweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count), getting 100 most recent tweets
    newTweets = api.user_timeline(screen_name=screen_name, count=100)

    # save most recent tweets
    allTweets.extend(newTweets)

    # save the id of the oldest tweet by one less
    previousTweet = allTweets[-1].id - 1

    # keep grabbing tweets until limit is reached from initial request
    while len(newTweets) > 0:
        # all subsequent requests use the max_id param to prevent duplicates
        newTweets = api.user_timeline(screen_name=screen_name, count=100, max_id=previousTweet)

        # save most recent tweets
        allTweets.extend(newTweets)

        # update the id of the oldest tweet by one less
        oldest = allTweets[-1].id - 1

    # write tweet objects to JSON file
    file = open('tweet.json', 'wb')
    for status in allTweets:
        json.dump(status._json, file, sort_keys=True, indent=4)

    # close the file"
    file.close()

    # # Get the User object for twitter...
    # user = api.get_user('readDonaldTrump')
    #
    # print user.screen_name
    # print user.followers_count


if __name__ == '__main__':
    # passing in the username of the account we want to grab tweets from
    get_tweets("@realDonaldTrump")