CREATE TABLE Filter
(
Text_ID int NOT NULL,
Times varchar(32) NOT NULL,
Country varchar(32) NOT NULL,
Sentiment varchar(32) NOT NULL,
Favourites_Count int null,
Retweet_Count int null,
FOREIGN KEY (Text_ID) REFERENCES Tweet(Text_ID)
);

