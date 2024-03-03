class SteamUser():
    def __init__(self, username, games: list):
        self.games = games
        self.username = username
        self.played_hours = 0

    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            return f"{self.username} is playing {game}"
        return f"{game} is not in library"

    def buy_game(self, game):
        if game not in self.games:
            

    def status(self):
        pass