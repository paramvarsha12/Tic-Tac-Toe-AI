import numpy as np
import pickle

class Agent:
    def __init__(self, symbol, exp_rate=0.3, lr=0.2, decay_gamma=0.9):
        self.symbol = symbol
        self.states = []
        self.lr = lr
        self.exp_rate = exp_rate
        self.decay_gamma = decay_gamma
        self.q_values = {}

    def getHash(self, board):
        return str(board.reshape(9))

    def chooseAction(self, positions, current_board):
        if np.random.uniform(0, 1) <= self.exp_rate:
            idx = np.random.choice(len(positions))
            action = positions[idx]
        else:
            value_max = -999
            for p in positions:
                next_board = current_board.copy()
                next_board[p] = self.symbol
                next_hash = self.getHash(next_board)
                value = 0 if self.q_values.get(next_hash) is None else self.q_values.get(next_hash)
                if value >= value_max:
                    value_max = value
                    action = p
        return action

    def addState(self, state):
        self.states.append(state)

    def feedReward(self, reward):
        for st in reversed(self.states):
            if self.q_values.get(st) is None:
                self.q_values[st] = 0
            self.q_values[st] += self.lr * (self.decay_gamma * reward - self.q_values[st])
            reward = self.q_values[st]

    def reset(self):
        self.states = []

    def savePolicy(self, file):
        with open(file, 'wb') as f:
            pickle.dump(self.q_values, f)

    def loadPolicy(self, file):
        with open(file, 'rb') as f:
            self.q_values = pickle.load(f)
