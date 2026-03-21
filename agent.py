class Agent:
    def __init__(self, player):
        self.player = player # 0 or 1
        self.best_elo = 0
        self.best_move = ()

    def move(self, grid):
        for move in self.move_search(grid):
            self.evaluation(grid, move)
        move = self.best_move
        return move

    def evaluation(self, grid, move): # Returns move, elo
        elo = 0
        
        if elo > self.best_elo:
            self.best_elo = elo
            self.best_move = move
        
    def move_search(self, grid, search_space):
        moves = set()

        # no stones yet → play center
        if not grid.grid:
            return [(0, 0)]

        for r0, q0 in grid.grid.keys():

            # iterate over hex radius
            for dr in range(-search_space, search_space + 1):
                for dq in range(-search_space, search_space + 1):

                    # hex distance check
                    if abs(dr) + abs(dq) + abs(dr + dq) > 2 * search_space:
                        continue

                    pos = (r0 + dr, q0 + dq)

                    # must be empty
                    if pos not in grid.grid:
                        moves.add(pos)

        return list(moves)
    
