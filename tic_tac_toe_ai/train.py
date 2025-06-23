from env import TicTacToe
from agent_model import Agent

class TrainTicTacToe:
    def __init__(self, rounds=5000):
        self.game = TicTacToe()
        self.player1 = Agent(symbol=1)
        self.player2 = Agent(symbol=-1)
        self.rounds = rounds

    def train(self):
        for i in range(self.rounds):
            self.game.reset()
            while not self.game.isEnd:
                positions = self.game.availablePositions()
                p1_action = self.player1.chooseAction(positions, self.game.board)
                self.game.updateState(p1_action, self.player1.symbol)
                self.player1.addState(self.game.getHash())

                win = self.game.winner()
                if win is not None:
                    self.giveReward(win)
                    self.player1.reset()
                    self.player2.reset()
                    break

                positions = self.game.availablePositions()
                p2_action = self.player2.chooseAction(positions, self.game.board)
                self.game.updateState(p2_action, self.player2.symbol)
                self.player2.addState(self.game.getHash())

                win = self.game.winner()
                if win is not None:
                    self.giveReward(win)
                    self.player1.reset()
                    self.player2.reset()
                    break

    def giveReward(self, winner):
        if winner == 1:
            self.player1.feedReward(1)
            self.player2.feedReward(-1)
        elif winner == -1:
            self.player1.feedReward(-1)
            self.player2.feedReward(1)
        else:
            self.player1.feedReward(0.1)
            self.player2.feedReward(0.1)

    def savePolicy(self):
        self.player1.savePolicy('policy_p1.pkl')
        self.player2.savePolicy('policy_p2.pkl')


if __name__ == "__main__":
    trainer = TrainTicTacToe(rounds=10000)
    trainer.train()
    print(" Training complete. Saving policy files...")
    trainer.savePolicy()
    print(" Policies saved as 'policy_p1.pkl' and 'policy_p2.pkl'")
