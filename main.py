# import keyboard
import random
import time

import pygame
score = 0
food_count = 0
symbol = ' '
update = True
PACKMAN_X = 0
PACKMAN_Y = 0
width = 20
height = 10
block_size = 80
open = True
pole = []
direction = "right"
enemy = 0
def draw_pacman(screen, x, y):
    surface = pygame.Surface((block_size, block_size))
    pygame.draw.circle(surface, (255, 0, 0), (block_size // 2, block_size // 2), block_size // 2)
    pygame.draw.circle(surface, (0, 0, 0), (block_size // 2, block_size // 2 * 0.5), block_size // 10)
    if open:
        pygame.draw.polygon(surface, (0, 0, 0), [(block_size // 2, block_size // 2), (block_size, block_size),
                                                 (block_size, block_size // 2 * 0.5)])
    else:
        pygame.draw.line(surface, (0, 0, 0), (block_size // 2, block_size // 2), (block_size, block_size // 2))

    if direction == "up":
        surface = pygame.transform.rotate(surface, 90)
    if direction == "down":
        surface = pygame.transform.rotate(surface, -90)
    if direction == "left":
        surface = pygame.transform.flip(surface, True, False)

    screen.blit(surface, (x, y))

def draw_enemy(screen, x,y):
    surface = pygame.Surface((block_size,block_size))

    pygame.draw.circle(surface, (11, 252, 3),(block_size // 2,block_size // 4),block_size // 4)
    pygame.draw.rect(surface, (11, 252, 3),(block_size // 4 + 1,block_size // 4,block_size // 2 - 1,block_size // 2 + block_size //4))
    pygame.draw.circle(surface, (0,0,0), (block_size // 2 + 5, block_size // 2 * 0.5),block_size // 15)
    pygame.draw.circle(surface, (0, 0, 0), (block_size // 2 + 5, block_size // 2 * 0.5), block_size // 15)

    screen.blit(surface, (x,y))


def generate_blok():
    for i in range(10):
        S = random.choice(["|", "-"])

        y = random.randint(0, height - 1)
        x = random.randint(0, width - 1)
        while (x == PACKMAN_X and y == PACKMAN_Y) or pole[y][x] == ".":
            y = random.randint(0, height - 1)
            x = random.randint(0, width - 1)

        pole[y][x] = S


def generate_pole():
    line = []
    for x in range(width):
        line.append(symbol)

    for y in range(height):
        pole.append(line.copy())


def print_pole():
    global update

    if not update:
        return

    print("-" * (width + 2))
    for line in pole:
        print("|" + "".join(line) + "|")
    print("-" * (width + 2))
    print(food_count)

    update = False


def print_pole_gui(screen):
    screen.fill((0, 0, 0))

    for y, line in enumerate(pole):
        for x, item in enumerate(line):
            if item == "@":
                draw_pacman(screen, x * block_size, y * block_size)
            if item == ".":
                pygame.draw.circle(screen, (255, 0 , 0), (x * block_size+block_size//2, y * block_size+block_size//2), block_size // 10)
                # pygame.draw.rect(screen, (255, 0, 0), (
                #     x * block_size,
                #     y * block_size,
                #
                #     x * block_size + block_size,
                #     y * block_size + block_size
                # ))


def move(x, y):
    global PACKMAN_X, PACKMAN_Y, pole, update, food_count, score

    if x >= width:
        x = 0

    if y >= height:
        y = 0

    if x < 0:
        x = width - 1

    if y < 0:
        y = height - 1

    # if pole[y][x] == "|" or pole[y][x] == "-":
    #     return
    #
    # if pole[y][x] == ".":
    #     food_count = food_count - 1
    if pole[y][x] == ".":
        score += 1

    pole[y][x] = "@"
    pole[PACKMAN_Y][PACKMAN_X] = symbol
    PACKMAN_X = x
    PACKMAN_Y = y
    update = True

def go_enemy():
    global enemy_last_time
    step_time = int(time.perf_counter() - start_time)
    if ste










def go(dir):
    global direction

    if dir == 'left':
        direction = "left"
        move(PACKMAN_X - 1, PACKMAN_Y)
    if dir == 'right':
        direction = "right"
        move(PACKMAN_X + 1, PACKMAN_Y)
    if dir == "up":
        direction = "up"
        move(PACKMAN_X, PACKMAN_Y - 1)
    if dir == "down":
        direction = "down"
        move(PACKMAN_X, PACKMAN_Y + 1)


def generate_food():
    global food_count

    for i in range(10):
        y = random.randint(0, height - 1)
        x = random.randint(0, width - 1)
        while (x == PACKMAN_X and y == PACKMAN_Y) or pole[y][x] == ".":
            y = random.randint(0, height - 1)
            x = random.randint(0, width - 1)

        pole[y][x] = "."
        food_count = food_count + 1


def chekc_game_end():
    global game_starte
    pass

def print_MENU():
    menu_w = width * block_size // 3
    menu_h = height * block_size // 2
    surface = pygame.Surface((menu_w, menu_h))

    surface.fill((145, 36, 103))


    pygame.draw.rect(
        surface, (134,20,300),
        (
            30,
            30,
            menu_w - 60,
            menu_w // 3 - 60
        )
    )

    pygame.draw.rect(
        surface, (134,20,300),
        (
            30,
            30,
            menu_w - 60,
            menu_w // 3 - 60
        )
    )

    pygame.draw.rect(
        surface, (134, 20, 300),
        (
            30,
            30,
            menu_w - 60,
            menu_w // 3 - 60
        )
    )

    screen.blit(surface,(width * block_size // 2 - menu_w // 2, height * block_size // 2 - menu_w // 2))










def map():
    global screen, clock
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 20)

    generate_food()
    # generate_blok()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    go('up')
                if event.key == pygame.K_DOWN:
                    go('down')
                if event.key == pygame.K_LEFT:
                    go('left')
                if event.key == pygame.K_RIGHT:
                    go('right')
        print_pole_gui(screen)
        text_s = font.render(F"score:{score}",False,(255,255,255))
        screen.blit(text_s, (5,5))
        pygame.display.update()
        # print_pole()
        clock.tick(10)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((width * block_size, height * block_size))
    pygame.display.set_caption('PACMAN')
    clock = pygame.time.Clock()

    generate_pole()
    map()
    # keyboard.add_hotkey('w', lambda: go('up'))
    # keyboard.add_hotkey('s', lambda: go('down'))
    # keyboard.add_hotkey('
