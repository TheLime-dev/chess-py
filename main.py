BOARD = (
    ("a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"),
    ("a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"),
    ("a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"),
    ("a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"),
    ("a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"),
    ("a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"),
    ("a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"),
    ("a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"),
)

PIECES = {
    'B': 2,
    'N': 3,
    'R': 4,
    'Q': 5,
    'K': 6
}


def name_to_nums(square):
    row, col = 0, 0
    for cur_row, i in enumerate(BOARD):
        for cur_col, j in enumerate(i):
            if j == square:
                row, col = cur_row, cur_col
    return row, col


def format_moves(moves, board, player):
    formatted_moves = []
    for move in moves:
        if 8 > move[0] > -1 and 8 > move[1] > -1 and board[move[0]][move[1]] == 0:
            formatted_moves.append(BOARD[move[0]][move[1]])
        elif (8 > move[0] > -1 and 8 > move[1] > -1) and (
                (player == 0 and board[move[0]][move[1]] < 0) or (player == 1 and board[move[0]][move[1]] > 0)):
            formatted_moves.append('x' + BOARD[move[0]][move[1]])
    return tuple(formatted_moves)


def pawn_moves(board, row, col, player):
    moves = []
    if player == 0:
        if board[row + 1][col] == 0:
            moves.append((row + 1, col))
            if row == 1 and board[row + 2][col] == 0:
                moves.append((row + 2, col))
        if col < 7 and board[row + 1][col + 1] < 0:
            moves.append((row + 1, col + 1))
        if col > 0 and board[row + 1][col - 1] < 0:
            moves.append((row + 1, col - 1))
    elif player == 1:
        if board[row - 1][col] == 0:
            moves.append((row - 1, col))
            if row == 6 and board[row - 2][col] == 0:
                moves.append((row - 2, col))
        if col < 7 and board[row - 1][col + 1] > 0:
            moves.append((row - 1, col + 1))
        if col > 0 and board[row - 1][col - 1] > 0:
            moves.append((row - 1, col - 1))

    # TODO: Implement en passant
    return format_moves(moves, board, player)


def bishop_moves(board, row, col, player):
    moves = []
    for i in range(-1, 2, 2):
        for j in range(-1, 2, 2):
            cur_row = row
            cur_col = col
            while True:
                cur_row = cur_row + i
                cur_col = cur_col + j
                if not (0 <= cur_col <= 7 and 0 <= cur_row <= 7):
                    break
                if board[cur_row][cur_col] == 0:
                    moves.append((cur_row, cur_col))
                elif player == 0 and board[cur_row][cur_col] < 0 or player == 1 and board[cur_row][cur_col] > 0:
                    moves.append((cur_row, cur_col))
                    break
                else:
                    break
    return format_moves(moves, board, player)


def knight_moves(board, row, col, player):
    moves = [(row + 2, col + 1), (row + 2, col - 1), (row - 2, col + 1), (row - 2, col - 1), (row - 1, col + 2),
             (row - 1, col - 2), (row + 1, col - 2), (row + 1, col + 2)]
    return format_moves(moves, board, player)


def rook_moves(board, row, col, player):
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    moves = []
    for x, y in directions:
        cur_row = row
        cur_col = col
        while True:
            cur_row = cur_row + x
            cur_col = cur_col + y
            if not (0 <= cur_col <= 7 and 0 <= cur_row <= 7):
                break
            if board[cur_row][cur_col] == 0:
                moves.append((cur_row, cur_col))
            elif player == 0 and board[cur_row][cur_col] < 0 or player == 1 and board[cur_row][cur_col] > 0:
                moves.append((cur_row, cur_col))
                break
            else:
                break
    return format_moves(moves, board, player)


def queen_moves(board, row, col, player):
    return rook_moves(board, row, col, player) + bishop_moves(board, row, col, player)


def king_moves(board, row, col, player):
    moves = [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col), (row - 1, col - 1),
             (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)]
    # TODO: Add castling
    return format_moves(moves, board, player)


def check_if_legal(board, player, move):
    target = move[-2:]
    if move[0] not in PIECES:
        piece = 1
        if move[0] != 'x':
            target = move
    else:
        piece = PIECES[move[0]]
    if player == 1:
        piece = -piece
    for row, line in enumerate(board):
        for col, square in enumerate(line):
            cur = BOARD[row][col]
            if square == piece:
                if abs(piece) == 1:
                    if move in pawn_moves(board, row, col, player):
                        return True, cur, target
                elif abs(piece) == 2:
                    if move[1:] in bishop_moves(board, row, col, player):
                        return True, cur, target
                elif abs(piece) == 3:
                    if move[1:] in knight_moves(board, row, col, player):
                        return True, cur, target
                elif abs(piece) == 4:
                    if move[1:] in rook_moves(board, row, col, player):
                        return True, cur, target
                elif abs(piece) == 5:
                    if move[1:] in queen_moves(board, row, col, player):
                        return True, cur, target
                elif abs(piece) == 6:
                    if move[1:] in king_moves(board, row, col, player):
                        return True, cur, target
    # TODO: Add Check and Checkmate
    return False, None, None


class Game:
    def __init__(self):
        self.board = [[4, 3, 2, 6, 5, 2, 3, 4],
                      [1, 1, 1, 1, 1, 1, 1, 1],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [-1, -1, -1, -1, -1, -1, -1, -1],
                      [-4, -3, -2, -6, -5, -2, -3, -4]]
        """
        0: empty square
        1: pawn
        2: bishop
        3: knight
        4: rook
        5: queen
        6: king
        -: black
        +: white
        """
        self.turn = 0  # 0: white, 1: black

    def make_move(self, cur, target):
        row, col = name_to_nums(cur)
        piece = self.board[row][col]
        self.board[row][col] = 0
        row, col = name_to_nums(target)
        self.board[row][col] = piece

    def print_board(self):
        for i in range(7, -1, -1):
            for col in self.board[i]:
                if col >= 0:
                    print(" ", end="")
                print(col, end=' ')
            print()

    def move(self, move):
        legal, starting_square, target = check_if_legal(self.board, self.turn, move)
        if legal:
            self.make_move(starting_square, target)
            self.turn = int(not self.turn)
            return True

        return False
