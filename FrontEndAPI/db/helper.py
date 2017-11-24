import psycopg2

class Connection:
    def __init__(self):
        con = psycopg2.connect(database='Twitter', user='root', host='localhost', password='root')
        self.cur = con.cursor()

    def get_user(self, user_id):
        self.cur.execute('select "user_id", "displayname" from users where "user_id" = %s')
        return self.cur.fetchall()

    def get_all(self):
        self.cur.execute('select * from filter as F INNER JOIN tweet as T ON F.text_id = T.text_id INNER JOIN users as U ON T.user_id = user_id')
        return  self.cur.fetchall()

    def get_Names(self):
        self.cur.execute('select DisplayName FROM Users WHERE User_ID = ANY (SELECT User_ID FROM Tweet WHERE User_ID > 100000) GROUP BY DisplayName')
        return self.cur.fetchall()

    def get_averageFavourite(self):
        self.cur.execute('select AVG(favourites_count) FROM filter, tweet WHERE filter.text_id = tweet.text_id')
        return self.cur.fetchall()

    def get_locationOfTweet(self):
        self.cur.execute('select st from tweet FULL OUTER JOIN users ON tweet.text_id = users.text_id')
        return self.cur.fetchall()

    def get_userid(self):
        self.cur.execute('select user_id FROM tweet UNION select user_id from users ORDER BY user_id')
        return self.cur.fetchall()

    def get_chinaTweet(self):
        self.cur.execute('select message FROM tweet WHERE message LIKE '%China%'')
        return self.cur.fetchall()

    def get_averageRetweet(self):
        self.cur.execute('select AVG(retweet_count) FROM filter,tweet WHERE filter.text_id = tweet.text_id')
        return self.cur.fetchall()

    def get_maxTweetInDay(self):
        self.cur.execute('select COUNT(DISTINCT text_id) FROM tweet GROUP BY datecreated')
        return self.cur.fetchall()

    def get_latestTweet(self):
        self.cur.execute('select * FROM tweet ORDER BY datecreated DESC LIMIT 1')
        return self.cur.fetchall()

    def get_totalTweets(self):
        self.cur.execute('select COUNT(text_id) FROM tweet')
        return self.cur.fetchall()

    def get_tweets(self,tweet_id):
        self.cur.execute('select * from tweet where "text_id" = %s',[tweet_id])
        return self.cur.fetchall()
