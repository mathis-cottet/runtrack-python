from Crate import Crate

class Player:
    def __init__(self, board):
        # Déclaration de l'attribut qui stocke la position du joueur
        self.pos = ()
        self.BOARD = board

    def move(self, direction):
        new_pos = ()

        if direction == 'up':
            new_pos = (self.pos[0] - 1, self.pos[1])
        elif direction == 'down':
            new_pos = (self.pos[0] + 1, self.pos[1])
        elif direction == 'left':
            new_pos = (self.pos[0], self.pos[1] - 1)
        elif direction == 'right':
            new_pos = (self.pos[0], self.pos[1] + 1)

        if self.check_move(new_pos, direction):
            self.BOARD.board[self.pos[0]][self.pos[1]] = 0
            self.pos = new_pos
            self.BOARD.board[self.pos[0]][self.pos[1]] = 2
        

    def check_move(self, new_pos, direction):
        if new_pos[0] > (self.BOARD.COLS - 1) or new_pos[0] < 0:
            return False
        if new_pos[1] > (self.BOARD.ROWS - 1) or new_pos[1] < 0:
            return False

        if (self.BOARD.board[new_pos[0]][new_pos[1]] != 1 and self.BOARD.board[new_pos[0]][new_pos[1]] != 4):
            if self.BOARD.board[new_pos[0]][new_pos[1]] == 3:
                crate = Crate((new_pos[0], new_pos[1]), self.BOARD)
                return crate.move(direction)
            else:
                return True
        else:
            return False