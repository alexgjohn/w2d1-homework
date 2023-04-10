class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0
        # self.results = {
        #     "win" : 3,
        #     "lose" : 0,
        #     "draw" : 1
        # }
        #this didn't work, but I'm glad I tried it!

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, searched_player):
        return searched_player in self.players

    def play_game(self, did_win):
        if did_win == True:
            self.points += 3

