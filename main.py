import pygame

BOARD = (
    ("a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"),
    ("b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8"),
    ("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"),
    ("d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8"),
    ("e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8"),
    ("f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"),
    ("g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8"),
    ("h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"),
)


def pawn_moves(board, row, col):
    # TODO: Implement Pawn movement
    pass


def bishop_moves(board, row, col):
    # TODO: Implement Bishop movement
    pass


def knight_moves(board, row, col):
    moves = [(row + 2, col + 1), (row + 2, col - 1), (row - 2, col + 1), (row - 2, col - 1), (row - 1, col + 2),
             (row - 1, col - 2), (row + 1, col - 2), (row + 1, col - 2)]
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


def find_legal_moves(board, player):
    moves = []
    for row in board:
        for col, square in enumerate(row):
            if square > 0 and player == 0 or square < 0 and player == 1:
                if abs(square) == 1:
                    moves += pawn_moves(board, row, col)
                elif abs(square) == 2:
                    moves += bishop_moves(board, row, col)
                elif abs(square) == 3:
                    moves += knight_moves(board, row, col)
                elif abs(square) == 4:
                    moves += rook_moves(board, row, col)
                elif abs(square) == 5:
                    moves += queen_moves(board, row, col)
                elif abs(square) == 6:
                    moves += king_moves(board, row, col)
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
        find_legal_moves(board, cur_turn)
        cur_turn = not cur_turn


if __name__ == '__main__':
    main()
