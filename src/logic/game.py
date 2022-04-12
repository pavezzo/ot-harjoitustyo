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
        self._insert_new_cell()
        self._insert_new_cell()
        self.score = 0

    def get_gamestate(self):
        return self.board

    def get_score(self):
        return self.score

    def new_keypress(self, direction):
        if direction not in directions:
            return False

        change = self._move_everything(direction)
        if change:
            return self._insert_new_cell()
        return False

    def _insert_new_cell(self):
        if not self._has_space():
            return False

        rand_int = random.randint(1, 2)
        num = 0
        if rand_int == 1:
            num = 2
        else:
            num = 4

        empty_cells = self._get_empty_cell_coordinates()
        next_one = random.randint(0, len(empty_cells)-1)
        self.board[empty_cells[next_one][0]][empty_cells[next_one][1]] = num

        return True

    def _move_everything(self, direction):
        start_y, start_x, end_y, end_x, step_y, step_x = self._calc_move_params(direction)

        change = False
        for i in range(start_y, end_y, step_y):
            for j in range(start_x, end_x, step_x):
                if self.board[i][j] is None:
                    continue

                y = i
                x = j
                while True:
                    old_y = y
                    old_x = x
                    y += directions[direction][0]
                    x += directions[direction][1]
                    if y < 0 or y> len(self.board)-1 or x < 0 or x > len(self.board[0])-1:
                        break
                    if self.board[y][x] is None:
                        self.board[y][x] = self.board[old_y][old_x]
                        self.board[old_y][old_x] = None
                        change = True
                    elif self.board[y][x] == self.board[old_y][old_x]:
                        self.board[y][x] *= 2
                        self.score += self.board[y][x]
                        self.board[old_y][old_x] = None
                        change = True
                        break
                    else:
                        break
        return change

    def _calc_move_params(self, direction):
        start_y = 0
        start_x = 0
        end_y = 0
        end_x = 0
        step_y = 0
        step_x = 0

        if direction == "up":
            start_y = 1
            start_x = 0
            end_y = len(self.board)
            end_x = len(self.board[0])
            step_y = 1
            step_x = 1
        elif direction == "down":
            start_y = len(self.board)-2
            start_x = 0
            end_y = -1
            end_x = len(self.board[0])
            step_y = -1
            step_x = 1
        elif direction == "right":
            start_y = 0
            start_x = len(self.board[0])-2
            end_y = len(self.board)
            end_x = -1
            step_y = 1
            step_x = -1
        elif direction == "left":
            start_y = 0
            start_x = 1
            end_y = len(self.board)
            end_x = len(self.board[0])
            step_y = 1
            step_x = 1
        return (start_y, start_x, end_y, end_x, step_y, step_x)


    def _has_space(self):
        for i, _ in enumerate(self.board):
            if None in self.board[i]:
                return True
        return False


    def _get_empty_cell_coordinates(self):
        coordinates = []
        for i, _ in enumerate(self.board):
            for j, elem in enumerate(self.board[i]):
                if elem is None:
                    coordinates.append([i, j])

        return coordinates

def create_empty_board():
    return [[None]*4 for _ in range(4)]
