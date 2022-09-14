

class Board:
    def __init__(self):
        self.empty_space = "_"
        self.board = None
        self.clean_board()

    def clean_board(self):
        self.board = [
            [self.empty_space, self.empty_space, self.empty_space],
            [self.empty_space, self.empty_space, self.empty_space],
            [self.empty_space, self.empty_space, self.empty_space]
        ]





    # def is_field_empty(self, x, y) - funkcja spawdza czy pole jest puste
    # zwraca True jak jest puste. Jak jest zajęte zwraca False
    # parametry - x, y - wspólrzędne. nie moga wykraczac poza zakres. musza byc poprawne
    def is_field_empty(self, y : int, x : int):
        return self.board[y][x] == self.empty_space

 #       return self.empty_space == self.board[y][x][k]

    # def fill_field(self, x, y, sign) - funkcja wypełnia pole znakiem,
    # jeśli pole jest puste i zwraca True
    # lub zwraca False gdy pole jest zajęte
    def fill_field(self, y, x, sign, k = 0):       # doświadczalnie widze że X w grze jest y :(

        if self.is_field_empty(y , x ):
            self.board[y][x] = sign
            return True
        else:
            print("Pole było już zajęte Cieniasie, Gdzie masz oczy !! ??")
            return False

    def print_board(self): #printuje aktualna sytuacje na planszy
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])
        return ""

    def get_winner_vertical(self):
        for i in range(3):
            sign = self.board[i][0]
            for j in range(1,3):
                if self.board[i][j] != sign:
                    sign = self.empty_space
                    break
            if sign != self.empty_space:
                return sign
        return None

    def get_winner_horizontal(self):
        for i in range(3):
            sign = self.board[0][i]
            for j in range(1,3):
                if self.board[j][i] != sign:
                    sign = self.empty_space
                    break
            if sign != self.empty_space:
                return sign
        return None

    def get_winner_diagonal(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] or \
                self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[1][1] != self.empty_space:
                return self.board[1][1]
        return None

    def get_winner(self):
        return self.get_winner_vertical() or self.get_winner_horizontal() or self.get_winner_diagonal()




    # def is_it_end_of_game(self):
        # if self.board[0][0][0] == self.board[0][1][0] and self.board[0][1][0] == self.board[0][2][0] and self.board[0][0][0] != self.empty_space or self.board[1][0][0] == self.board[1][1][0] and self.board[1][1][0] == self.board[1][2][0] and self.board[1][0][0] != self.empty_space or self.board[2][0][0] == self.board[2][1][0] and self.board[2][1][0] == self.board[2][2][0] and self.board[2][0][0] != self.empty_space:
        #     print("win on the level")
        #     return True, self.board[0][0][0]
        # elif self.board[0][0][0] == self.board[1][0][0] and self.board[2][0][0] == self.board[1][0][0] and self.board[1][0][0] != self.empty_space:
        #     print("Vertical Win x = 0")
        #     return True, self.board[0][0][0]
        # elif self.board[0][1][0] == self.board[1][1][0] and self.board[2][1][0] == self.board[1][1][0] and self.board[1][1][0] != self.empty_space:
        #     print("Vertical Win x = 1")
        #     return True, self.board[0][1][0]
        # elif self.board[0][2][0] == self.board[1][2][0] and self.board[2][2][0] == self.board[1][2][0] and self.board[1][2][0] != self.empty_space:
        #     print("Vertical Win x = 2")
        #     return True, self.board[0][2][0]
        # elif self.board[0][0][0] == self.board[1][1][0] == self.board[2][2][0] or self.board[0][2][0] == self.board[1][1][0] == self.board[2][0][0] and self.board[2][0][0] != self.empty_space:
        #     print("NA SKOS")
        #     return True, self.board[1][1][0]
        # else:
        #     print("Gra Toczy Się Dalej")
        #     return False


    # def who_win(self): ## zwrcała sign zwycięzcy
    #     tab = ()
    #     tab = self.is_it_end_of_game()
    #     print("zwycięzcą jest :")
    #     return tab[1]
    #     pass
