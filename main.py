def pawn_moves(board, row, col):
    #TODO: Implement Pawn movement
    pass

def bishop_moves(board, row, col):
    #TODO: Implement Bishop movement
    pass

def knight_moves(board, row, col):
    #TODO: Implement Knight movement
    pass

def rook_moves(board, row, col):
    #TODO: Implement Rook movement
    pass

def queen_moves(board, row, col):
    #TODO: Implement Queen movement
    pass

def king_moves(board, row, col):
    #TODO: Implement King movement
    pass

def find_legal_moves(board, player):
    moves = []
    for row in board:
        for col,square in enumerate(row):
            if square>0 and player==0 or  square<0 and player==1:
                if abs(square)==1:
                    moves+=pawn_moves(board, row, col)
                elif abs(square)==2:
                    moves+=bishop_moves(board, row, col)
                elif abs(square)==3:
                    moves+=knight_moves(board, row, col)
                elif abs(square)==4:
                    moves+=rook_moves(board, row, col)
                elif abs(square)==5:
                    moves+=queen_moves(board, row, col)
                elif abs(square)==6:
                    moves+=king_moves(board, row, col)
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
    cur_turn = 0 # 0: white, 1: black
    count = 0
    while not game_over:
        count += 1
        find_legal_moves(board, cur_turn)
        cur_turn = not cur_turn


if __name__ == '__main__':
    main()