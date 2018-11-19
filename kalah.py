class Kalah(object):
    def __init__(self, holes, seeds):
        self.holes = holes
        self.seeds = seeds
        self.board = [seeds for h in range(holes)]
        self.board.append(0)
        self.board = self.board * 2
        self.player = 1

    def status(self):
        return tuple(self.board)

    def play(self, hole):
        if hole < 0 or hole >= (self.holes * 2 + 2):
            raise IndexError

        if self.board[hole] == 0:
            raise ValueError

        for i in range(self.board[hole]):
            index = hole + i + 1
            if index >= (self.holes * 2 + 2):
                index -= (self.holes * 2 + 2)
            self.board[index] += 1
        self.board[hole] = 0

        self.player = 2 if self.player == 1 else 1

        return f"Player {self.player} plays next"
        # return f"Player {self.player} wins"
        # return "Tie"
