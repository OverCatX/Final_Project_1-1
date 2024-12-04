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

