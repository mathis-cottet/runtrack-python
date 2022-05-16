class Board:
    def __init__(self, board, size):
        self.board = board
        self.ROWS = self.COLS = 10
        self.ROW_WIDTH = size[0] // self.COLS
        self.COL_WIDTH = size[1] // self.ROWS