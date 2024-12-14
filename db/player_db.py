import csv
import os.path

database_file = 'db/players.csv'

class PlayerDB:
    def __init__(self, db_file=database_file):
        self.players_db = db_file
        if not os.path.exists(self.players_db):
            with open(self.players_db, mode='w') as file:
                writer = csv.writer(file)
                writer.writerow(['Username', 'HighScore'])
        self.data = []

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
                writer.writerow([username, 0])
            print(f'{username} was added to Database')
            return Player(username, 0)
        else:
            with open(self.players_db, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Username'] == username:
                        return Player(row['Username'], row['HighScore'])

    def set_new_highscore(self, username, highscore):
        with open(self.players_db, mode='r', encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if row[0] == username:
                    row[1] = highscore
                self.data.append(row)
        with open(self.players_db, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(self.data)

    def get_leaderboard(self):
        data = []
        with open(self.players_db, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return sorted(data, key=lambda x: int(x["HighScore"]), reverse=True)

class Player:
    def __init__(self, username: str, highscore: int):
        self.username = username
        self.highscore = highscore

    def updates_best_score(self, score):
        self.highscore = score
        PlayerDB().set_new_highscore(self.username,self.highscore)
        print(f'updated {self.username} highscore data')

    def __str__(self):
        return f'Player: {self.username}, HighScore: {self.highscore}'