# import pygame

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


def format_moves(moves, board, player):
    formatted_moves = []
    for move in moves:
        if 8 > move[0] > -1 and 8 > move[1] > -1 and board[move[0]][move[1]] == 0:
            formatted_moves.append(BOARD[move[0]][move[1]])
        elif (8 > move[0] > -1 and 8 > move[1] > -1) and (
                (player == 0 and board[move[0]][move[1]] < 0) or (player == 1 and board[move[0]][move[1]] > 0)):
            formatted_moves.append('x'+BOARD[move[0]][move[1]])
    return tuple(formatted_moves)


def pawn_moves(board, row, col):
    # TODO: Implement Pawn movement
    pass


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
    return format_moves(moves, board)


def knight_moves(board, row, col):
    moves = [(row + 2, col + 1), (row + 2, col - 1), (row - 2, col + 1), (row - 2, col - 1), (row - 1, col + 2),
             (row - 1, col - 2), (row + 1, col - 2), (row + 1, col + 2)]
    return format_moves(moves, board)


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
    return format_moves(moves, board)


def queen_moves(board, row, col):
    # TODO: Implement Queen movement
    pass


def king_moves(board, row, col):
    moves = [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col), (row - 1, col - 1),
             (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)]
    return format_moves(moves, board)


def check_if_legal(board, player, move):
    target = move[-2:]
    if move[0] not in PIECES:
        piece = 1
    else:
        piece = PIECES[move[0]]
    if player == 1:
        piece = -piece
    for row, line in enumerate(board):
        for col, square in enumerate(line):
            cur = BOARD[row][col]
            if square == piece:
                if abs(piece) == 1:
                    if target in pawn_moves(board, row, col):
                        return cur, target
                elif abs(piece) == 2:
                    if target in bishop_moves(board, row, col, player):
                        return cur, target
                elif abs(piece) == 3:
                    if target in knight_moves(board, row, col):
                        return cur, target
                elif abs(piece) == 4:
                    if target in rook_moves(board, row, col, player):
                        return cur, target
                elif abs(piece) == 5:
                    if target in queen_moves(board, row, col):
                        return cur, target
                elif abs(piece) == 6:
                    if target in king_moves(board, row, col):
                        return cur, target
    return False


def main():
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
    board = [[4, 3, 2, 6, 5, 2, 3, 4],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [-1, -1, -1, -1, -1, -1, -1, -1],
             [-4, -3, -2, -6, -5, -2, -3, -4]]
    game_over = False
    cur_turn = 0  # 0: white, 1: black
    count = 0
    while not game_over:
        count += 1
        print(board)
        move = input("Enter move: ")
        check_if_legal(board, cur_turn, move)

        cur_turn = not cur_turn


if __name__ == '__main__':
    main()
