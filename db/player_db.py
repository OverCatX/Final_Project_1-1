import csv
import os.path

database_file = 'db/players.csv'


class PlayerDB:
    def __init__(self, db_file=database_file):
        self.players_db = db_file
        if not os.path.exists(self.players_db):
            with open(self.players_db, mode='w') as file:
                writer = csv.writer(file)
                writer.writerow(['Username', 'HighScore', 'ReleaseScore'])

    def player_exists(self, username) -> bool:
        username = username.lower()
        with open(self.players_db, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Username'] == username:
                    return True

    def player_login(self, username):
        username = username.lower()
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

class Player:
    def __init__(self, username: str, highscore: int, release_score: int):
        self.username = username
        self.highscore = highscore
        self.release_score = release_score

    def updates(self, score):
        self.release_score = score
        if self.highscore < score:
            self.highscore = score
        print('updated player data')

    def __str__(self):
        return f'Player: {self.username}, HighScore: {self.highscore}, ReleaseScore: {self.release_score}'