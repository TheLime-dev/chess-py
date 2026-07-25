import pygame

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

def pawn_moves(board, row, col):
    # TODO: Implement Pawn movement
    pass


def bishop_moves(board, row, col):
    # TODO: Implement Bishop movement
    pass


def knight_moves(board, row, col):
    moves = [(row + 2, col + 1), (row + 2, col - 1), (row - 2, col + 1), (row - 2, col - 1), (row - 1, col + 2),
             (row - 1, col - 2), (row + 1, col - 2), (row + 1, col + 2)]
    formated_moves = []
    for move in moves:
        if move[0]>-1 and move[1]>-1 and board[move[0]][move[1]] == 0:
            formated_moves.append(BOARD[move[0]][move[1]])
    return tuple(formated_moves)


def rook_moves(board, row, col):
    # TODO: Implement Rook movement
    pass


def queen_moves(board, row, col):
    # TODO: Implement Queen movement
    pass


def king_moves(board, row, col):
    # TODO: Implement King movement
    pass


def check_if_legal(board, player, move):
    target= move[-2:]
    if move[0] not in PIECES:
        piece = 1
    else:
        piece = PIECES[move[0]]
    if player == 1:
        piece = -piece
    moves = []
    for row, line in enumerate(board):
        for col, square in enumerate(line):
            cur = BOARD[row][col]
            if square == piece:
                if piece == 1:
                    if target in pawn_moves(board, row, col):
                        return cur, target
                elif piece == 2:
                    if target in bishop_moves(board, row, col):
                        return cur, target
                elif piece == 3:
                    if target in knight_moves(board, row, col):
                        return cur, target
                elif piece == 4:
                    if target in rook_moves(board, row, col):
                        return cur, target
                elif piece == 5:
                    if target in queen_moves(board, row, col):
                        return cur, target
                elif piece == 6:
                    if target in king_moves(board, row, col):
                        return cur, target


    return tuple(moves)


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
