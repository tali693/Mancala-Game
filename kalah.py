class Kalah(object):
    def __init__(self, holes, seeds):
        self.holes = holes
        self.seeds = seeds
        self.board = [seeds for h in range(holes)]
        self.board.append(0)
        self.board = self.board * 2

    def get_board(self):
        return self.board
