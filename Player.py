class Player:
    def __init__(self, sign, board):
        self.sign = sign
        self.board = board

    def get_input(self):
        x, y = None, None
        while x is None:
            inp = input(f"Ruch gracza {self.sign}. Podaj x y: ")
            tab = inp.split(" ")
            try:
                x, y = int(tab[0]), int(tab[1])
                if not 0 <= x <= 2 or not 0 <= y <= 2:
                    x = None
            except Exception:
                x = None
            if x is None:
                print("Podano niepoprawne wspolrzedne!")
        return x, y

    def move(self):
        ok = False
        while not ok:
            inp = self.get_input()
            ok = self.board.fill_field(inp[0], inp[1], self.sign)

