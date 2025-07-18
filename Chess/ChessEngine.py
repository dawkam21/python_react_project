class GameState():
    def __init__(self):
        # -- reprezentuje puste miejsce
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        self.white_to_move = True
        self.move_log = []
    
    def make_move(self, move):
        self.board[move.start_row][move.start_col] = "--" # Puste miejsce
        self.board[move.end_row][move.end_col] = move.piece_moved # Przeniesienie figury
        self.move_log.append(move) # Dodanie ruchu do logu
        self.white_to_move = not self.white_to_move # Zmiana tury

    def undo_move(self):
        if len(self.move_log) != 0: # Jeśli jest coś do cofnięcia
            move = self.move_log.pop() # Cofnięcie ostatniego ruchu
            self.board[move.start_row][move.start_col] = move.piece_moved # Przywrócenie figury
            self.board[move.end_row][move.end_col] = move.piece_captured # Przywrócenie figury przeciwnika
            self.white_to_move = not self.white_to_move # Zmiana tury

    '''
    Wszystkie ruchy zawierające szach
    '''
    def get_valid_moves(self):
        return self.get_all_possible_moves()

    '''
    Wszystkie ruchy niezawierające szacha
    '''
    def get_all_possible_moves(self):
        moves = [Move((6, 3), (4, 3), self.board)]
        for r in range(len(self.board)): # Iteracja po wierszach
            for c in range(len(self.board[r])): # Iteracja po kolumnach
                turn = self.board[r][c][0] # Kolor figury
                if (turn == 'w' and self.white_to_move) or (turn == 'b' and not self.white_to_move):
                    piece = self.board[r][c][1]
                    if piece == 'p':
                        self.get_pawn_moves(r, c, moves)
                    elif piece == 'R':
                        self.get_rook_moves(r, c, moves)
        return moves
    
    '''
    Zbierz wszystkie ruchy pionka w danym miejscu (kolumnie i wierszu) i dodaj do listy
    '''
    def get_pawn_moves(self, r, c, moves):
        pass
    '''
    Zbierz wszystkie ruchy wieży w danym miejscu (kolumnie i wierszu) i dodaj do listy
    '''
    def get_rook_moves(self, r, c, moves):
        pass

class Move():
    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4, 
                     "5": 3, "6": 2, "7": 1, "8": 0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_cols = {"a": 0, "b": 1, "c": 2, "d": 3,
                     "e": 4, "f": 5, "g": 6, "h": 7}
    cols_to_files = {v: k for k, v in files_to_cols.items()}

    def __init__(self, start_sq, end_sq, board):
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]
        self.move_id = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col
        print(self.move_id)

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.move_id == other.move_id
        return False
    
    # Potem mogę zrobić prawdziwą notację szachową
    def get_chess_notation(self):
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)
    
    def get_rank_file(self, r, c):
        return self.cols_to_files[c] + self.rows_to_ranks[r]