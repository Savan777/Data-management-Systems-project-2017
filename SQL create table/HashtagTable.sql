CREATE TABLE Hashtag
(
Text_ID int NOT NULL,
HashTag_1 varchar(32) NULL,
HashTag_2 varchar(32) NULL,
HashTag_3 varchar(32) NULL,
HashTag_4 varchar(32) NULL,
HashTag_5 varchar(32) NULL,
FOREIGN KEY(Text_ID) REFERENCES Tweet(Text_ID)
);