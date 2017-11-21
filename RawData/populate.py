import pandas
import requests
from sqlalchemy import create_engine
from urls import urls


class Populate:
    def __init__(self):
        # localhost:5432/XXX' where XXX is the name of the databases
        self.engine = create_engine('postgresql://root:root@localhost:5432/backupTwitter')

    def populate(self):
        # gets players and writes to sql, replacing if table exists
        players = get_dataframe_from_response(urls[0])

        # name of SQL table, db connection, ~if table exists, drop it, recreate it and insert data~,
        # , write DataFrame index as a column true/false
        players.to_sql('players', con=self.engine, if_exists='replace', index=False)
        # gets teams and writes to sql, replace if table exists (if you want to append to the table,
        # use if_exists='append')

        # Call function below
        teams = get_dataframe_from_response(urls[1])

        # I only want to store certain columns
        # .loc[] is a label-location based indexer for selection by label
        # A list or array of labels is given as parameters
        teams = teams.loc[:, ['TEAM_ID', 'TEAM_NAME']]
        teams.to_sql('teams', con=self.engine, if_exists='replace', index=False)

def get_dataframe_from_response(url):
    # sends a request to the url, requests key : value payload
    # reponse is a decoded text response from the server
    # custom header is used, given less precedence.
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    # any response other than 200 is an error
    while response.status_code != 200:
        response = requests.get(url)
    # if youre dealing with json data then use .json() to decode it
    headers = response.json()['resultSets'][0]['headers']
    data = response.json()['resultSets'][0]['rowSet']
    # data can contain series, array, constants or list-like objects
    # columns are column labels to use for resulting frame
    frame = pandas.DataFrame(data, columns=headers)

    return frame


# Initialize populate object
populate = Populate()
# Call populate function on populate object
populate.populate()
