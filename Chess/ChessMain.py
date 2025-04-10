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
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        draw_game_state(screen, game_state)
        clock.tick(MAX_FPS)
        p.display.flip()

 # Rysowanie planszy i figur / Lewy górny róg planszy zawsze biały
def draw_board(screen):
    colors = [p.Color('lightgray'), p.Color('brown')]
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

