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
        if hole < 0 or hole > self.holes * 2:
            raise IndexError("Illegal hole!")

        if self.player == 1 and hole >= self.holes or \
                self.player == 2 and hole < self.holes + 1:
            raise IndexError("Second player hole!")

        if self.board[hole] == 0:
            raise ValueError

        self.player = 2 if self.player == 1 else 1

        index = 0
        crossing_other_bank = False
        for i in range(self.board[hole]):
            index = hole + i + 1
            index %= self.holes * 2 + 2
            if index == self.holes * self.player + self.player - 1:
                crossing_other_bank = True
                continue
            self.board[index] += 1

        if crossing_other_bank:
            index += 1
            index %= self.holes * 2 + 2
            self.board[index] += 1
        self.board[hole] = 0


        return f"Player {self.player} plays next"
        # return f"Player {self.player} wins"
        # return "Tie"
