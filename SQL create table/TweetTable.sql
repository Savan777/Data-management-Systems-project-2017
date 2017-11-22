CREATE TABLE Tweet
(
Text_ID int NOT NULL PRIMARY KEY,
User_ID int NULL,
Message varchar(255) NOT NULL,
DateCreated DATETIME NOT NULL,
ST varchar(32) NOT NULL, -- Source of text
LT varchar(32) NOT NULL, --Location of text
FOREIGN KEY(User_ID) REFERENCES Users(User_ID)
);