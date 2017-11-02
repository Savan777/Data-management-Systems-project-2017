CREATE TABLE Tweet
(
Text_ID int NOT NULL PRIMARY KEY,
User_ID int NOT NULL,
Message varchar(255) NOT NULL,
DateCreated DATETIME NOT NULL,
ST varchar(32) NOT NULL,
LT varchar(32) NOT NULL,
FOREIGN KEY(User_ID) REFERENCES Users(User_ID)
);