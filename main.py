from agent import Agent

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
            if self.win_check():
                print(f'player {player} wins')
                return True
        return False
    
    def win_check(self):
        if not self.last_play:
            return False

        grid = self.grid          # local reference (faster)
        r, q = self.last_play
        player = grid[(r, q)]

        directions = ((1, 0), (0, 1), (1, -1))

        for dr, dq in directions:
            count = 1

            # check both directions using a sign flip
            for sign in (1, -1):
                nr = r + dr * sign
                nq = q + dq * sign

                while grid.get((nr, nq)) == player:
                    count += 1

                    # early win exit
                    if count >= 6:
                        return True

                    nr += dr * sign
                    nq += dq * sign

        return False    


grid = Grid()
turn = 0
won = False

while not won:
    player = turn % 2

    # First round → 1 move each
    if turn == 0:
        moves = 1
    else:
        moves = 2

    print(f"Player {player}'s turn ({moves} moves)")

    for _ in range(moves):
        won = grid.play(player)

    turn += 1
