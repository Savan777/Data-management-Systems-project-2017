import pandas as pd
import sqlalchemy
from sqlalchemy import sql
from sqlalchemy import create_engine, String, INTEGER, VARCHAR, BIGINT


class Populate:
    def __init__(self):
        self.engine = create_engine('postgresql://root:root@localhost:5432/Twitter') #connection to database

    def populate(self):
        #reads data from csv file
        dataframe = pd.read_csv('data.csv', usecols=['country', 'datecreated', 'displayname', 'favourites_count', 'followers_count', 'friends_count', 'hashtags','lt', 'profileaddress', 'retweet_count', 'st', 'summary', 'message', 'text_id', 'user_id'])

        #selecting required columns from dataframe
        userframe = dataframe.loc[:, ['user_id', 'displayname', 'summary', 'followers_count', 'friends_count', 'profileaddress']]
        tweetframe = dataframe.loc[:, ['text_id', 'user_id', 'message', 'datecreated', 'st', 'lt']]
        filterframe = dataframe.loc[:, ['text_id', 'country', 'favourites_count', 'retweet_count']]
        hashtagframe = dataframe.loc[:, ['text_id', 'hashtags']]

        #writing to database, dtype is datatype dont need it but just put it there cause it works
        filterframe.to_sql("filter", con=self.engine, if_exists='replace', index=False)
        hashtagframe.to_sql("hashtag", con=self.engine, if_exists='replace', index=False)
        tweetframe.to_sql("tweet", con=self.engine, if_exists='replace', index=False, dtype={'text_id': BIGINT, 'user_id': INTEGER, 'message': String, 'datecreated': VARCHAR, 'st': String, 'lt': String})
        userframe.to_sql("users", con=self.engine, if_exists='replace', index=False, dtype={'user_id': INTEGER, 'displayname': VARCHAR, 'summary': VARCHAR, 'followers_count': INTEGER, 'friends_count': INTEGER, 'profileaddress': VARCHAR})

populate = Populate()
populate.populate()