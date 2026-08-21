import copy

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


class Board:
    def __init__(self):
        self.position = [[4, 3, 2, 5, 6, 2, 3, 4],
                         [1, 1, 1, 1, 1, 1, 1, 1],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [-1, -1, -1, -1, -1, -1, -1, -1],
                         [-4, -3, -2, -5, -6, -2, -3, -4]]

    def make_move(self, cur, target):
        row, col = name_to_nums(cur)
        piece = self.position[row][col]
        self.position[row][col] = 0
        row, col = name_to_nums(target)
        self.position[row][col] = piece

    def print_board(self):  # only for debugging purposes
        for i in range(7, -1, -1):
            for col in self.position[i]:
                if col >= 0:
                    print(" ", end="")
                print(col, end=' ')
            print()


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

    # TODO: Implement en passant 4
    return format_moves(moves, board, player)


# noinspection DuplicatedCode
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


# noinspection DuplicatedCode
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
    # TODO: Add castling 5
    return format_moves(moves, board, player)


############################################

def check(board, player):
    king_pos = ''
    for row, line in enumerate(board):
        for col, square in enumerate(line):
            if square == 6 and player == 0:
                king_pos = BOARD[row][col]
            elif square == -6 and player == 1:
                king_pos = BOARD[row][col]
    possible_moves = find_moves(board, int(not player))
    for move in possible_moves:
        print(move)
        if move[1][-2:] == king_pos:
            return True
    return False


def find_moves(board, player):  # finds every square where a piece can move to (not considering checks)
    moves = []
    for row, line in enumerate(board):
        for col, square in enumerate(line):
            cur = BOARD[row][col]
            if square == 1 and player == 0 or square == -1 and player == 1:
                for val in pawn_moves(board, row, col, player):
                    moves.append((cur, val))
            elif square == 2 and player == 0 or square == -2 and player == 1:
                for val in bishop_moves(board, row, col, player):
                    moves.append((cur, 'B' + val))
            elif square == 3 and player == 0 or square == -3 and player == 1:
                for val in knight_moves(board, row, col, player):
                    moves.append((cur, 'N' + val))
            elif square == 4 and player == 0 or square == -4 and player == 1:
                for val in rook_moves(board, row, col, player):
                    moves.append((cur, 'R' + val))
            elif square == 5 and player == 0 or square == -5 and player == 1:
                for val in queen_moves(board, row, col, player):
                    moves.append((cur, 'Q' + val))
            elif square == 6 and player == 0 or square == -6 and player == 1:
                for val in king_moves(board, row, col, player):
                    moves.append((cur, 'K' + val))
    return moves


def find_legal_moves(board, player):
    moves = []
    for val in find_moves(board, player):
        start, move = val
        temp_board = Board()
        temp_board.position = copy.deepcopy(board)
        temp_board.make_move(start, move[-2:])
        if not check(temp_board.position, player):
            moves.append((start, move))
    if moves:
        return moves
    else:
        return None  # Checkmate/Stalemate


def check_if_legal(board, player, move):
    legal_moves = find_legal_moves(board, player)
    if legal_moves:
        for val in legal_moves:
            start, possible_move = val
            if possible_move == move:
                return True, start
    return False, None


class Game:
    def __init__(self):
        self.board = Board()
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
        self.moves = []
        self.turns = 0

    def move(self, move):
        target = move[-2:]
        legal, start = check_if_legal(self.board.position, self.turn, move)
        if legal:
            self.board.make_move(start, target)
            if self.turn == 0:
                self.moves.append(move)
            else:
                self.moves.append([self.moves.pop(), move])
            self.turns += 1
            self.turn = int(not self.turn)
            return True

        return False
