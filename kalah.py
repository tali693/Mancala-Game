class Kalah(object):
    def __init__(self, holes, seeds):
        self.holes = holes
        self.seeds = seeds
        self.board = [seeds for h in range(holes)]
        self.board.append(0)
        self.board = self.board * 2
        self.player = 1

    def get_board(self):
        return self.board

    def play(self, hole):
        if hole < 0 or hole >= (self.holes * 2 + 2):
            raise IndexError

        if self.board[hole] == 0:
            raise ValueError

        self.player = 2 if self.player == 1 else 1

        return f"Player {self.player} plays next"
        # return f"Player {self.player} wins"
        # return "Tie"
