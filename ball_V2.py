import pygame
import random

pygame.init()

size_x = 600
size_y = 400
black = (1, 1, 1)
green = (100, 100, 100)
global white
white = (250, 250, 250)
global coll
coll = black

display = pygame.display.set_mode((size_x, size_y))
font = pygame.font.Font(None, 40)
font_1 = pygame.font.Font(None, 25)
font_score = pygame.font.Font(None, 65)
clock = pygame.time.Clock()
backgr_image = pygame.image.load("photo_2023-03-01_23-54-39.jpg")

score = 0
check_win = 0


class Menu:
    def __init__(self):
        self._option_surface = []
        self._callback = []
        self._option_index = 0
        self._colors = []

    # def set_colors(self, green, xz):
    #     gr = (100, 100, 100)
    #     # x_z = (0, 150,100)
    #     self._colors.append(green, gr)
    #     # self._colors.append(xz, x_z)

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
    coll = black
    # puse = False

    # if puse:
    #     text_pause = font_score.render("paused", True, green)
    #     display.blit(text_pause, (280, 170))
    #     pygame.display.update()
    # else:
    # done
    while done:
        clock.tick(fps)
        for events in pygame.event.get():
            if events.type == pygame.QUIT or events.type == pygame.KEYDOWN and events.key == pygame.K_ESCAPE:
                quit()
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

        # if keys[pygame.K_SPACE]:
        #     puse = True
        #     puse = not puse

        display.fill(coll)
        text_game_score = font_score.render(f"{check_win}", True, green)
        display.blit(text_game_score, (280, 170))
        # text_score = font_1.render(f"your score: {score}", True, green)
        # display.blit(text_score, (0, 0))
        pygame.draw.rect(display, white, (point, 395, 50, 5))
        pygame.draw.circle(display, white, (x, y), r)
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


def col():
    pygame.display.update()


# def ex():
#     return False


#     while ex_1:
#         for even in pygame.event.get():
#             if even.type == pygame.QUIT or even.type == pygame.KEYDOWN and even.key == pygame.K_ESCAPE:
#                 quit()
#         opti = False
#         ex_1 = False
#         game = True
#
#         pygame.display.update()

def opti():
#     # ex = False
    menu_1 = Menu()
    menu_1.append_option("coolor", None)
    menu_1.append_option("exit", None)
#
    opti = True
    while opti:
        for even in pygame.event.get():
            if even.type == pygame.QUIT or even.type == pygame.KEYDOWN and even.key == pygame.K_ESCAPE:
                opti = False
                quit()
            if even.type == pygame.KEYDOWN:
                if even.key == pygame.K_DOWN:
                    menu_1.switch(1)
                if even.key == pygame.K_UP:
                    menu_1.switch(-1)
                if even.key == pygame.K_RETURN:
                    menu_1.select()
                    # opt = False
                if even.key == pygame.K_BACKSPACE:
                    opti = False
                # if even.key == pygame.K_RETURN == "exit":
                #     ex = True
                #     if ex == True:
                #         opti = False
#
        display.fill(black)
        menu_1.draw(display, 100, 50, 30)
        # if opt == True:
        #     q = False
        pygame.display.update()


menu = Menu()
menu.append_option("PLAY", game_2)
menu.append_option("option", opti)
menu.append_option("exit", quit)

game = True
while game:
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
