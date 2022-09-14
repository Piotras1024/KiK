from Board import Board
from Player import Player

# import Board
# potem musisz uzywac Board.Board
#a jakj zaimportujesz uzywajac from jak wyzej to tylko Board

class Game:
    ROUNDS_UNTIL_DRAW = 9

    def __init__(self):
        print("game init")
        self.board = Board()
        self.players = [Player("o", self.board), Player("x", self.board)]
        self.first_player = 0

    def run(self):
        while True:
            self.board.clean_board()
            current_player = self.first_player
            print(f"\nNowa gra. Zaczyna gracz {self.players[current_player].sign}.")
            for i in range(self.first_player, self.first_player + Game.ROUNDS_UNTIL_DRAW):
                self.players[current_player].move()
                self.board.print_board()
                if self.board.get_winner() != None:
                    print(f"Gre wygrał gracz z znakiem {self.board.get_winner()} w {i + 1 - self.first_player} ruchów.")
                    break
                current_player = (i + 1) % 2
            print("!!! REMIS !!! REMIS !!! REMIS !!!")
            self.first_player = (self.first_player+1) % 2
