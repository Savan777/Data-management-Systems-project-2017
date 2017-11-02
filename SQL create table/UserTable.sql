CREATE TABLE Users
(
User_ID int NOT NULL PRIMARY KEY,
DisplayName varchar(32) NOT NULL,
Summary varchar(255) NULL,
Followers_Count int NULL,
Friends_Count int NULL,
ProfileAddress varchar(255) NOT NULL
);