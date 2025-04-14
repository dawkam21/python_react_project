import sys
sys.path.append("C:/Users/dkaminski1/Desktop/python_react_project")
import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512  # 8x8 board
DIMENSION = 8  # 8x8 board
SQ_SIZE = HEIGHT // DIMENSION  # 64 pixels per square
MAX_FPS = 15  # for animations
IMAGES = {}

def load_images():
    """Wgranie obrazków do słownika."""
    pieces = ['wK', 'wQ', 'wR', 'wB', 'wN', 'wp', 'bK', 'bQ', 'bR', 'bB', 'bN', 'bp']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f'Chess/images/{piece}.png'), (SQ_SIZE, SQ_SIZE))
    # Wywołanie obrazka - np. IMAGES['wK']

#Główny silnik
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    game_state = ChessEngine.GameState()
    load_images() # raz przed loopem
    running = True
    sq_selected = ()  # Tu będzie przechowywana wybrana figura : Tuple (row, col)
    player_clicks = []  # Lista kliknięć gracza : Two Tuples [(row, col), (row, col)]
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # (x, y) w pikselach
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sq_selected == (row, col): #kliknięcie tej samej figury
                    sq_selected = () # odznaczanie figury
                    player_clicks = []  # resetowanie kliknięć
                else:
                    sq_selected = (row, col)
                    player_clicks.append(sq_selected) # dodawanie kliknięcia
                if len(player_clicks) == 2: # po dwukrotnym kliknięciu
                    move = ChessEngine.Move(player_clicks[0], player_clicks[1], game_state.board)
                    # print(move.get_chess_notation())
                    game_state.make_move(move)
                    sq_selected = () # resetowanie kliknięcia
                    player_clicks = [] # resetowanie kliknięć

        draw_game_state(screen, game_state)
        clock.tick(MAX_FPS)
        p.display.flip()

 # Rysowanie planszy i figur / Lewy górny róg planszy zawsze biały
def draw_board(screen):
    colors = [p.Color('lightgray'), p.Color('forestgreen')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": #kwadrat nie pusty
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

 # Cała grafika planszy
def draw_game_state(screen, game_state):
    draw_board(screen)  # rysowanie planszy
    draw_pieces(screen, game_state.board)  # rysowanie figur

if __name__ == "__main__":
    main()

