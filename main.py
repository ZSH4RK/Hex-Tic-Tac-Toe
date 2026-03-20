
class Grid:
    def __init__(self):
        self.grid = {}
        self.last_play = ()



    def check_hex(self):
        r, q = map(int, input('Where do you want to play? ').split(','))
        if (r, q) not in self.grid:
            return True, r, q
        else:
            print('square occupied')
            return self.check_hex()

    def play(self, player):
        free, r, q = self.check_hex()
        if free:
            self.grid[(r, q)] = player
            self.last_play = (r, q)
    
    def win_check(self):
        pass
        


grid = Grid()
turn = 0

while True:
    player = turn % 2

    # First round → 1 move each
    if turn == 0:
        moves = 1
    else:
        moves = 2

    print(f"Player {player}'s turn ({moves} moves)")

    for _ in range(moves):
        grid.play(player)
    
    print(grid.grid)

    turn += 1