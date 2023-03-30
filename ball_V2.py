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
red = (255, 0, 0)
white = (250, 250, 250)
colors = [(255, 0, 255), (255, 255, 0), (0, 255, 255), orange, (100, 200, 50), (0, 150, 200), (200, 50, 50),
             (150, 50, 250)]

class colors_1:
    colors_1 = colors[0]

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
    ballup_colors = white


class image:
    up_image = surface


class exit:
    up_exit = False


class coordinates:
    coordinate = 600
    soordinate_2 = 600
    coordinate_3 = 600


class speed:
    up_speed = 60


class color_racket:
    racket = white


def game_2():
    done = True
    fps = speed.up_speed
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
            pygame.draw.rect(display, color_racket.racket, (point, 395, 50, 5))
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
    coordinates.coordinate = 114


def blu():
    image.up_image = surface
    color.up_color = blue
    ball_color.ballup_color = blue
    coordinates.coordinate = 153


def blackk():
    image.up_image = surface
    color.up_color = black
    ball_color.ballup_color = green
    coordinates.coordinate = 193


def images():
    image.up_image = backgr_image2
    ball_color.ballup_color = colors_1.colors_1
    coordinates.coordinate = 233


def ex():
    exit.up_exit = True


class level:
    level_up = False


def levels():
    level.level_up = not level.level_up


class fon:
    fon_up = False


def fonts():
    fon.fon_up = not fon.fon_up


class racket:
    racket_up = False


def rackets():
    racket.racket_up = not racket.racket_up


def racket_blue():
    color_racket.racket = blue
    coordinates.coordinate_3 = 218
    ball_color.ballup_colors = blue

def racket_orange():
    color_racket.racket = red
    coordinates.coordinate_3 = 258
    ball_color.ballup_colors = red


def racket_surprise():
    color_racket.racket = colors_1.colors_1
    coordinates.coordinate_3 = 298
    ball_color.ballup_colors = colors_1.colors_1


def easy():
    speed.up_speed = 30
    coordinates.soordinate_2 = 169


def medium():
    speed.up_speed = 60
    coordinates.soordinate_2 = 208


def hard():
    speed.up_speed = 160
    coordinates.soordinate_2 = 248


def opti():
    opti = True
    menu_1 = Menu()
    menu_1.append_option("Background", fonts)
    menu_1.append_option("Level", levels)
    menu_1.append_option("Racket", rackets)
    menu_1.append_option("Back", ex)
    menu_2 = Menu()
    menu_2.append_option("easy", easy)
    menu_2.append_option("medium", medium)
    menu_2.append_option("hard", hard)
    menu_3 = Menu()
    menu_3.append_option("orange", orang)
    menu_3.append_option("blue", blu)
    menu_3.append_option("black", blackk)
    menu_3.append_option("image", images)
    menu_4 = Menu()
    menu_4.append_option("blue", racket_blue)
    menu_4.append_option("orange", racket_orange)
    menu_4.append_option("surprise", racket_surprise)
    while opti:
        if exit.up_exit == True:
            opti = False
        for even in pygame.event.get():
            if even.type == pygame.QUIT or even.type == pygame.KEYDOWN and even.key == pygame.K_ESCAPE:
                quit()
            if level.level_up == True:
                if even.type == pygame.KEYDOWN:
                    if even.key == pygame.K_DOWN:
                        menu_2.switch(1)
                    if even.key == pygame.K_UP:
                        menu_2.switch(-1)
                    if even.key == pygame.K_RETURN:
                        menu_2.select()
                    if even.key == pygame.K_BACKSPACE:
                        level.level_up = False
            elif fon.fon_up == True:
                if even.type == pygame.KEYDOWN:
                    if even.key == pygame.K_DOWN:
                        menu_3.switch(1)
                    if even.key == pygame.K_UP:
                        menu_3.switch(-1)
                    if even.key == pygame.K_RETURN:
                        menu_3.select()
                    if even.key == pygame.K_BACKSPACE:
                        fon.fon_up = False
            elif racket.racket_up == True:
                if even.type == pygame.KEYDOWN:
                    if even.key == pygame.K_DOWN:
                        menu_4.switch(1)
                    if even.key == pygame.K_UP:
                        menu_4.switch(-1)
                    if even.key == pygame.K_RETURN:
                        menu_4.select()
                    if even.key == pygame.K_BACKSPACE:
                        racket.racket_up = False
            else:
                if even.type == pygame.KEYDOWN:
                    if even.key == pygame.K_DOWN:
                        menu_1.switch(1)
                    if even.key == pygame.K_UP:
                        menu_1.switch(-1)
                    if even.key == pygame.K_RETURN:
                        menu_1.select()
                    if even.key == pygame.K_BACKSPACE:
                        opti = False

        display.fill(black)
        text_menu = font.render("основные настройки", True, (green))
        display.blit(text_menu, (150, 15))
        menu_1.draw(display, 50, 100, 50)
        if level.level_up == True:
            pygame.draw.rect(display, black, (145, 15, 290, 30))
            surf.fill((40, 40, 40))
            surf.set_alpha(150)
            display.blit(surf, (0, 0))
            text_menu2 = font.render("выберете уровень сложности", True, (200, 200, 200))
            text_menu3 = font_1.render("нажмите backspase чтобы вернуться НАЗАД", True, (150, 150, 150))
            pygame.draw.circle(display, white, (285, coordinates.soordinate_2), 10)
            display.blit(text_menu2, (110, 15))
            display.blit(text_menu3, (0, size_y - 17))
            menu_2.draw(display, 305, 155, 40)
        elif fon.fon_up == True:
            pygame.draw.rect(display, black, (145, 15, 290, 30))
            surf.fill((40, 40, 40))
            surf.set_alpha(150)
            display.blit(surf, (0, 0))
            text_menu4 = font.render("выберете цвет фона", True, (200, 200, 200))
            text_menu5 = font_1.render("нажмите backspase чтобы вернуться НАЗАД", True, (150, 150, 150))
            colors_1.colors_1 = colors[random.randint(0, 7)]
            pygame.draw.circle(display, ball_color.ballup_color, (285, coordinates.coordinate), 10)
            display.blit(text_menu4, (150, 15))
            display.blit(text_menu5, (0, size_y - 17))
            menu_3.draw(display, 305, 100, 40)
        elif racket.racket_up == True:
            pygame.draw.rect(display, black, (145, 15, 290, 30))
            surf.fill((40, 40, 40))
            surf.set_alpha(150)
            display.blit(surf, (0, 0))
            text_menu4 = font.render("выберете цвет ракетки", True, (200, 200, 200))
            text_menu5 = font_1.render("нажмите backspase чтобы вернуться НАЗАД", True, (150, 150, 150))
            colors_1.colors_1 = colors[random.randint(0, 7)]
            pygame.draw.circle(display, ball_color.ballup_colors, (285, coordinates.coordinate_3), 10)
            display.blit(text_menu4, (150, 15))
            display.blit(text_menu5, (0, size_y - 17))
            menu_4.draw(display, 305, 205, 40)
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
