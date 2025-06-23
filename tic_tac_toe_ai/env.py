import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.isEnd = False

    def getHash(self):
        return str(self.board.reshape(9))

    def availablePositions(self):
        positions = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    positions.append((i, j))
        return positions

    def updateState(self, position, symbol):
        self.board[position[0], position[1]] = symbol

    def winner(self):
        for i in range(3):
            if abs(sum(self.board[i, :])) == 3:
                return int(np.sign(sum(self.board[i, :])))
            if abs(sum(self.board[:, i])) == 3:
                return int(np.sign(sum(self.board[:, i])))

        diag1 = sum([self.board[i, i] for i in range(3)])
        if abs(diag1) == 3:
            return int(np.sign(diag1))

        diag2 = sum([self.board[i, 2 - i] for i in range(3)])
        if abs(diag2) == 3:
            return int(np.sign(diag2))

        if len(self.availablePositions()) == 0:
            return 0

        return None

    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.isEnd = False
