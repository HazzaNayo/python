import pygame
import sys

# Konfigurasi
WIDTH, HEIGHT = 640, 480
TILE_SIZE = 40
FPS = 60

# Labirin sederhana (1 = dinding, 0 = jalan)
MAZE = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,1,0,1,1,1,0,1,0,1,1,0,1],
    [1,0,1,0,0,0,0,1,0,0,1,0,0,1,0,1],
    [1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
    [1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1],
    [1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

ROWS = len(MAZE)
COLS = len(MAZE[0])

# Posisi awal dan akhir
start_pos = (1, 1)
end_pos = (9, 14)

pygame.init()
screen = pygame.display.set_mode((COLS * TILE_SIZE, ROWS * TILE_SIZE))
pygame.display.set_caption("Game Labirin")
clock = pygame.time.Clock()

player_pos = list(start_pos)

def draw_maze():
    for y in range(ROWS):
        for x in range(COLS):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if MAZE[y][x] == 1:
                pygame.draw.rect(screen, (40, 40, 40), rect)
            else:
                pygame.draw.rect(screen, (200, 200, 200), rect)
    # Tujuan
    pygame.draw.rect(screen, (0, 255, 0), (end_pos[1]*TILE_SIZE, end_pos[0]*TILE_SIZE, TILE_SIZE, TILE_SIZE))

def draw_player():
    pygame.draw.rect(screen, (0, 0, 255), (player_pos[1]*TILE_SIZE, player_pos[0]*TILE_SIZE, TILE_SIZE, TILE_SIZE))

def move_player(dx, dy):
    new_x = player_pos[1] + dx
    new_y = player_pos[0] + dy
    if 0 <= new_x < COLS and 0 <= new_y < ROWS and MAZE[new_y][new_x] == 0:
        player_pos[1] = new_x
        player_pos[0] = new_y

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_player(0, -1)
            elif event.key == pygame.K_DOWN:
                move_player(0, 1)
            elif event.key == pygame.K_LEFT:
                move_player(-1, 0)
            elif event.key == pygame.K_RIGHT:
                move_player(1, 0)

    screen.fill((0, 0, 0))
    draw_maze()
    draw_player()

    if tuple(player_pos) == end_pos:
        font = pygame.font.SysFont(None, 48)
        text = font.render("Menang!", True, (255, 0, 0))
        screen.blit(text, (WIDTH//2 - 80, HEIGHT//2 - 24))

    pygame.display.flip()
    clock.tick(FPS)