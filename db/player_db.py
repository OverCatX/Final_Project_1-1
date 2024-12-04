import csv
import os.path

database_file = 'players.csv'

class PlayerDB:
    def __init__(self, db_file = database_file):
        self.players_db = db_file
        if not os.path.exists(self.players_db):
            with open(self.players_db, mode='w') as file:
                writer = csv.writer(file)
                writer.writerow(['Username', 'HighScore'])

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
                writer.writerow([username, 0])
            print(f'{username} was added to Database')
            return username
        else:
            return username