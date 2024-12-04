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