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

CurBoardPosition = list[list[int]]
CurPlayer = int
Square = tuple[int, int]


def name_to_nums(square: str):
    row, col = 0, 0
    for cur_row, i in enumerate(BOARD):
        for cur_col, j in enumerate(i):
            if j == square:
                row, col = cur_row, cur_col
    return row, col


############################################


def pawn_moves(board: CurBoardPosition, square: Square, player: CurPlayer):
    moves = []
    row, col = square
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

    # TODO: en passant
    return moves


# noinspection DuplicatedCode
def bishop_moves(board: CurBoardPosition, square: Square, player: CurPlayer):
    moves = []
    row, col = square
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
    return moves


def knight_moves(square: Square):
    row, col = square
    moves = [(row + 2, col + 1), (row + 2, col - 1), (row - 2, col + 1), (row - 2, col - 1), (row - 1, col + 2),
             (row - 1, col - 2), (row + 1, col - 2), (row + 1, col + 2)]
    return moves


# noinspection DuplicatedCode
def rook_moves(board: CurBoardPosition, square: Square, player: CurPlayer):
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    moves = []
    row, col = square
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
    return moves


def queen_moves(board: CurBoardPosition, square: Square, player: CurPlayer):
    return rook_moves(board, square, player) + bishop_moves(board, square, player)


def king_moves(square: Square):
    row, col = square
    moves = [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col), (row - 1, col - 1),
             (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)]
    # TODO: Add castling
    return moves


############################################

def in_check(board: CurBoardPosition, player: CurPlayer):
    temp_board = Board()
    temp_board.position = board
    king_pos = (None, None)
    for row, line in enumerate(board):
        for col, square in enumerate(line):
            if square == 6 and player == 0:
                king_pos = (row, col)
            elif square == -6 and player == 1:
                king_pos = (row, col)
    temp_board.find_moves(not player)
    for move in temp_board.possible_moves:
        if move[1] == king_pos:
            return True
    return False


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
        self.possible_moves = []  # unformatted with raw position data
        self.legal_moves = []  # formatted
        self.mate = False

    def make_move(self, start, target):
        row, col = start
        piece = self.position[row][col]
        self.position[row][col] = 0
        row, col = target
        self.position[row][col] = piece

    def find_moves(self, player: CurPlayer):  # finds all legal moves without considering checks
        self.possible_moves = []
        for row, line in enumerate(self.position):
            for col, square in enumerate(line):
                start = (row, col)
                if square == 1 and player == 0 or square == -1 and player == 1:
                    for target in pawn_moves(self.position, start, player):
                        self.possible_moves.append((start, target))
                elif square == 2 and player == 0 or square == -2 and player == 1:
                    for target in bishop_moves(self.position, start, player):
                        self.possible_moves.append((start, target))
                elif square == 3 and player == 0 or square == -3 and player == 1:
                    for target in knight_moves(start):
                        self.possible_moves.append((start, target))
                elif square == 4 and player == 0 or square == -4 and player == 1:
                    for target in rook_moves(self.position, start, player):
                        self.possible_moves.append((start, target))
                elif square == 5 and player == 0 or square == -5 and player == 1:
                    for target in queen_moves(self.position, start, player):
                        self.possible_moves.append((start, target))
                elif square == 6 and player == 0 or square == -6 and player == 1:
                    for target in king_moves(start):
                        self.possible_moves.append((start, target))

        # sorts out moves that go out of the board or takes a piece of the player
        valid_moves = []
        for move in self.possible_moves:
            row, col = move[1][0], move[1][1]
            if not (0 <= row <= 7 and 0 <= col <= 7):
                continue
            final_square = self.position[row][col]
            if final_square > 0 and player == 0 or final_square < 0 and player == 1:
                continue
            valid_moves.append(move)

        self.possible_moves = valid_moves

    def sort_check(self, player: CurPlayer):  # sort out position with check
        valid_moves = []
        for move in self.possible_moves:
            tmp = Board()
            tmp.position = copy.deepcopy(self.position)
            tmp.make_move(move[0], move[1])
            if not in_check(tmp.position, player):
                valid_moves.append(move)
        self.possible_moves = valid_moves

    def convert_moves(self):  # Converts own structure to chess notation
        for move in self.possible_moves:
            pass  # TODO: Implement converting own structure to chess notation

    def print_board(self):  # only for debugging purposes
        for i in range(7, -1, -1):
            for col in self.position[i]:
                if col >= 0:
                    print(" ", end="")
                print(col, end=' ')
            print()


class Move:
    def __init__(self, move: str, board: Board, player: CurPlayer):
        self.possible = False
        self.take = False
        if move[0].islower():
            self.piece = 1
        else:
            self.piece = PIECES[move[0]]
            move = move[1:]

        self.target = name_to_nums(move[-2:])
        move = move[:-2]
        start_indication = None
        if len(move) != 0:
            if move[-1] == 'x':
                self.take = True
                move = move[:-1]
            start_indication = move
        if start_indication:
            different_moves = []  # different moves possible to that square using the piece specified
            for i in board.possible_moves:
                row = i[0][0]
                col = i[0][1]
                if i[1] == self.target and abs(board.position[row][col]) == self.piece:
                    different_moves.append(i)
            for j, move in enumerate(different_moves):
                start = move[0]
                if start_indication in BOARD[start[0]][start[1]]:
                    self.start = start
                    self.possible = True
        else:
            for i in board.possible_moves:
                row = i[0][0]
                col = i[0][1]
                if i[1] == self.target and abs(board.position[row][col]) == self.piece:
                    self.start = i[0]
                    self.possible = True


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
        self.player = 0  # 0: white, 1: black
        self.made_moves = []
        self.turns = 0
        self.en_passant = None

    def play_move(self, move):
        self.board.find_moves(self.player)
        self.board.sort_check(self.player)
        self.board.convert_moves()
        self.move = Move(move, self.board, self.player)
        if self.move.possible:
            self.board.make_move(self.move.start, self.move.target)
            self.player = int(not self.player)
            return True
        return False


# TODO: Implement Checkmate/Stalemate
'''
Empty board to copy when debugging
[[0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0]]
 
 !!!IMPORTANT!!! 
 When debugging, don't forget that in chess notation, col comes first then row
'''
