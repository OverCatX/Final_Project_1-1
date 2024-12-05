import csv
import os.path
from .player import Player

database_file = 'db/players.csv'


class PlayerDB:
    def __init__(self, db_file=database_file):
        self.players_db = db_file
        if not os.path.exists(self.players_db):
            with open(self.players_db, mode='w') as file:
                writer = csv.writer(file)
                writer.writerow(['Username', 'HighScore', 'ReleaseScore'])

    def player_exists(self, username) -> bool:
        with open(self.players_db, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Username'] == username:
                    return True

    def player_login(self, username):
        if not self.player_exists(username):
            with open(self.players_db, mode='a') as file:
                writer = csv.writer(file)
                writer.writerow([username, 0, 0])
            print(f'{username} was added to Database')
            return Player(username, 0, 0)
        else:
            with open(self.players_db, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Username'] == username:
                        return Player(row['Username'], row['HighScore'], row['ReleaseScore'])
