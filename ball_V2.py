import pygame
import time
import random

pygame.init()

size_x = 600
size_y = 400
black = (1, 1, 1)
green = (100, 100, 100)
orange = (150, 50, 0)
blue = (0, 0, 200)

global white
white = (250, 250, 250)

display = pygame.display.set_mode((size_x, size_y))
surf = pygame.Surface((size_x, size_y))
font = pygame.font.Font(None, 40)
font_1 = pygame.font.Font(None, 25)
font_score = pygame.font.Font(None, 65)
clock = pygame.time.Clock()
backgr_image = pygame.image.load("photo_2023-03-01_23-54-39.jpg")
backgr_image2 = pygame.image.load("1626855870_23-p-fon-soti-krasnie-24.jpg")
surface = pygame.Surface((size_x, size_y))

score = 0
check_win = 0


class Menu:
    def __init__(self):
        self._option_surface = []
        self._callback = []
        self._option_index = 0

    def append_option(self, option, callback):
        self._option_surface.append(font.render(option, True, white))
        self._callback.append(callback)

    def switch(self, direction):
        self._option_index = max(0, min(self._option_index + direction, len(self._option_surface) - 1))

    def select(self):
        self._callback[self._option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._option_surface):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._option_index:
                pygame.draw.rect(surf, green, option_rect)
            surf.blit(option, option_rect)


class color:
    up_color = black

class ball_color:
    ballup_color = white


class image:
    up_image = surface


class exit:
    up_exit = False


class coordinates:
    coordinate = 600


def game_2():
    done = True
    fps = 60
    x = size_x // 2
    y = size_y // 2
    r = 10
    direct_x = 1
    direct_y = 1
    point = 300
    check_lose = 0
    global check_win
    check_win = 0
    global score
    score = score
    a = False
    while done:
        if a:
            for eve in pygame.event.get():
                if eve.type == pygame.QUIT or eve.type == pygame.KEYDOWN and eve.key == pygame.K_ESCAPE:
                    quit()
                if eve.type == pygame.KEYDOWN:
                    if eve.key == pygame.K_SPACE:
                        a = False
            text_pause = font_score.render("pause", True, white)
            display.blit(text_pause, (230, 125))
            pygame.display.update()
        else:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        surf.fill((40, 40, 40))
                        surf.set_alpha(150)
                        display.blit(surf, (50, 50))
                        a = not a
                        pygame.display.update()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                if point + 50 < 600:
                    point += 5
            if keys[pygame.K_LEFT]:
                if point > 0:
                    point -= 5
            if keys[pygame.K_BACKSPACE]:
                done = False
            if point <= x <= point + 50 and size_y - 5 <= y + r <= size_y:
                if check_win >= score:
                    score += 1
                direct_x += 0.5
                direct_y += 0.5
                direct_y = -direct_y
                check_win += 1

            surface.fill(color.up_color)
            display.blit(image.up_image, (0, 0))
            text_game_score = font_score.render(f"{check_win}", True, green)
            display.blit(text_game_score, (280, 170))
            # text_score = font_1.render(f"your score: {score}", True, green)
            # display.blit(text_score, (0, 0))
            pygame.draw.rect(display, white, (point, 395, 50, 5))
            pygame.draw.circle(display, white, (x, y), r)
            if a == True:
                display.blit(surf, (0, 0))
            x += direct_x
            if x + r >= 600 or x - r < 0:
                direct_x = -direct_x
            y += direct_y
            if y - r <= 0:
                direct_y = -direct_y
            if y + r >= 450:
                y = random.randint(10, 200)
                x = random.randint(10, 600)
                # check_lose += 1
                # check_win = 0
                direct_y = 1
                direct_x = 1
                score = score
                # game = True
                done = False

            pygame.display.update()


def orang():
    image.up_image = surface
    color.up_color = orange
    ball_color.ballup_color = orange
    coordinates.coordinate = 83


def blu():
    image.up_image = surface
    color.up_color = blue
    ball_color.ballup_color = blue
    coordinates.coordinate = 133


def blackk():
    image.up_image = surface
    color.up_color = black
    ball_color.ballup_color = white
    coordinates.coordinate = 183


def images():
    image.up_image = backgr_image2
    ball_color.ballup_color = green
    coordinates.coordinate = 233


def ex():
    exit.up_exit = True


def opti():
    opti = True
    menu_1 = Menu()
    menu_1.append_option("orange", orang)
    menu_1.append_option("blue", blu)
    menu_1.append_option("black", blackk)
    menu_1.append_option("image", images)
    menu_1.append_option("back", ex)
    while opti:
        if exit.up_exit == True:
            opti = False
        for even in pygame.event.get():
            if even.type == pygame.QUIT or even.type == pygame.KEYDOWN and even.key == pygame.K_ESCAPE:
                quit()
            if even.type == pygame.KEYDOWN:
                if even.key == pygame.K_DOWN:
                    menu_1.switch(1)
                if even.key == pygame.K_UP:
                    menu_1.switch(-1)
                if even.key == pygame.K_RETURN:
                    # pygame.draw.circle(display, white, (5, 5), 5)
                    menu_1.select()
                    # menu_2.draw(display, 10, 10, 10)
                if even.key == pygame.K_BACKSPACE:
                    opti = False

        display.fill(black)
        text_menu = font.render("выберете цвет фона", True, (green))
        display.blit(text_menu, (150, 15))
        pygame.draw.circle(display, ball_color.ballup_color, (230, coordinates.coordinate), 10)
        menu_1.draw(display, 250, 70, 50)
        pygame.display.update()


menu = Menu()
menu.append_option("PLAY", game_2)
menu.append_option("option", opti)
menu.append_option("exit", quit)

game = True
while game:
    if game == True:
        exit.up_exit = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game = False
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                menu.switch(1)
            if event.key == pygame.K_UP:
                menu.switch(-1)
            if event.key == pygame.K_RETURN:
                menu.select()

    display.blit(backgr_image, (0, 0))
    menu.draw(display, 250, 150, 40)
    text_score = font_1.render(f"Вы набрали: {check_win}", True, (200, 150, 50))
    display.blit(text_score, (220, 100))
    text_score_2 = font_1.render(f"Рекорд: {score}", True, (250, 100, 0))
    display.blit(text_score_2, (0, 380))

    pygame.display.update()
