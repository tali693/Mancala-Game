class Kalah(object):
    def __init__(self, holes, seeds):
        self.holes = holes
        self.seeds = seeds
        self.board = [seeds for h in range(holes)]
        self.board.append(0)
        self.board = self.board * 2
        self.range = ([0, holes - 1], [holes + 1, holes * 2])
        self.bank = [self.range[0][1] + 1, self.range[1][1] + 1]
        self.player = 0

    def status(self):
        return tuple(self.board)

    def play(self, hole):
        if hole < 0 or hole > self.holes * 2:
            raise IndexError("Illegal hole!")

        if hole in self.bank:
            raise IndexError("Bank!")

        if self.player == 0 and hole > self.holes or \
                self.player == 1 and hole < self.holes:
            raise IndexError("Second player hole!")

        if self.board[hole] == 0:
            raise ValueError("Empty hole!")

        second_player = self.player * -1 + 1
        index = 0
        crossing_second_player_bank = False

        # The seeds are distributed one by one in the holes and the player's own bank,
        # but not into the opponent's bank.
        for i in range(self.board[hole]):
            index = hole + i + 1
            index %= self.holes * 2 + 2
            # Second player's bank
            if index == self.bank[second_player]:
                crossing_second_player_bank = True
                continue
            self.board[index] += 1

        if crossing_second_player_bank:
            index += 1
            index %= self.holes * 2 + 2
            self.board[index] += 1
        self.board[hole] = 0

        # The last seed is dropped into an empty hole owned by the player
        if self.range[self.player][0] < index <= self.range[self.player][1] \
                and self.board[index] == 1:
            # The opposite hole isn't empty
            if self.board[self.holes * 2 - index] > 0:
                self.board[self.bank[self.player]] += self.board[self.holes * 2 - index] + 1
                self.board[self.holes * 2 - index] = 0
                self.board[index] = 0

        second_player_sum_seeds = [sum(self.board[i] for i in range(self.range[second_player][0],
                                                                    self.range[second_player][1] + 1))]

        # End game
        if second_player_sum_seeds[0] == 0:
            player_sum_seeds = 0
            for i in range(self.range[self.player][0], self.range[self.player][1] + 1):
                player_sum_seeds += self.board[i]
                self.board[i] = 0
            self.board[self.bank[self.player]] += player_sum_seeds

            if self.board[self.bank[self.player]] == self.board[self.bank[second_player]]:
                return "Tie!"
            if self.board[self.bank[self.player]] > self.board[self.bank[second_player]]:
                return f"Player {self.player + 1} wins!"
            return f"Player {second_player + 1} wins!"

        # Change turn if the last seed is not dropped into the bank
        if index != self.bank[self.player]:
            self.player = self.player * -1 + 1

        return f"Player {self.player + 1} plays next"
