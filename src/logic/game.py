import random

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

class Game:
    def __init__(self):
        self.board = create_empty_board()
        self.score = 0

    def get_gamestate(self):
        return self.board

    def get_score(self):
        return self.score

    def new_keypress(self, direction):
        if direction not in directions:
            return False

        dir = directions[direction]
        new_board = create_empty_board()

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                pass
        
                
        self._insert_new_cell()

    def _insert_new_cell(self):
        if not self._has_space():
            return False

        rand_int = random.randint(1, 2)
        num = 0
        if rand_int == 1: num = 2 
        else: num = 4

        empty_cells = self._get_empty_cell_coordinates()
        next_one = random.randint(0, len(empty_cells)-1)
        self.board[empty_cells[next_one][0]][empty_cells[next_one][1]] = num

        return self.board


    def _has_space(self):
        for i in range(len(self.board)):
            if None in self.board[i]:
                return True
        return False


    def _get_empty_cell_coordinates(self):
        coordinates = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] is None:
                    coordinates.append([i, j])

        return coordinates
    


def create_empty_board():
    return [[None]*4 for _ in range(4)]