import pygame
from settings import *


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w = WIDTH / 2
        self.mid_h = HEIGHT / 2

        self.surface = self.game.surface
        self.screen = self.game.screen

    # displays menu onto screen
    def blit_screen(self):
        self.screen.blit(self.surface, (0, 0))
        pygame.display.update()

    def draw_text(self, text, size, x, y, color):

        font = pygame.font.Font(pygame.font.get_default_font(), size)
        # draws text, last arg is text colour. returns a rectangle image of text
        text_surface = font.render(text, True, color)
        # gets dimentions of the text rectangle
        text_rect = text_surface.get_rect()
        # assigns x and y position to the center of the rectangle
        text_rect.center = (x, y)
        self.surface.blit(text_surface, text_rect)


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        # changes location of where text is displayed. Y is being offset by 20 for each menu option
        self.quitButton = button(GREY, self.mid_w - 80, self.mid_h + 110, 160, 50, 'Quit Game')
        self.settingsButton = button(GREY, self.mid_w - 80, self.mid_h - 5, 160, 50, 'Controls')
        self.startButton = button(GREY, self.mid_w - 80, self.mid_h - 120, 160, 50, 'Start Game')
        self.menu_bg = pygame.image.load('Images/Menu Background/Menu_BG.jpg')

    # Can create new menus options
    def display_menu(self):
        self.surface.blit(self.menu_bg, (0, 0))
        self.quitButton.draw(self.surface, BLACK)
        self.settingsButton.draw(self.surface, BLACK)
        self.startButton.draw(self.surface, BLACK)
        self.check_input()
        self.blit_screen()

    def check_input(self):
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                self.game.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.quitButton.is_over(pos):
                    pygame.quit()
                    quit()
                elif self.startButton.is_over(pos):
                    self.game.playing = True

                elif self.settingsButton.is_over(pos):
                    self.game.curr_menu = self.game.options
            else:
                self.colour_change(pos)



    def colour_change(self, pos):
        if self.startButton.is_over(pos):
            self.startButton.color = LIGHTGREY
        else:
            self.startButton.color = GREY
        if self.settingsButton.is_over(pos):
            self.settingsButton.color = LIGHTGREY
        else:
            self.settingsButton.color = GREY
        if self.quitButton.is_over(pos):
            self.quitButton.color = LIGHTGREY
        else:
            self.quitButton.color = GREY


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        # Selects start state of menu
        self.state = 'Volume'
        # aligns text in middle of screen with some y offset
        self.backButton = button(GREY, 5, 5, 80, 25, 'Back')
        self.options_bg = pygame.image.load('Images/Menu Background/Options_BG.jpg')
        self.asdw_img = pygame.transform.scale(pygame.image.load('Images/Asd_img.png'), (288, 187))
        self.arrow_img = pygame.transform.scale(pygame.image.load('Images/Arrowk_Img.png'), (288, 187))
        # dictates where cursor starts

    def display_menu(self):
        self.surface.blit(self.options_bg, (0, 0))
        self.draw_text('Options', 70, WIDTH / 2, HEIGHT / 2 - 190, WHITE)
        self.backButton.draw(self.surface, BLACK)
        self.surface.blit(self.asdw_img, (self.mid_w + 100, self.mid_h - 80))
        self.surface.blit(self.arrow_img, (self.mid_w - 400, self.mid_h - 80))
        self.check_option_input()
        self.blit_screen()

    # logic for different inputs, e.g press backspace will return to main menu
    def check_option_input(self):
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.backButton.is_over(pos):
                    self.game.curr_menu = self.game.main_menu
            else:
                self.option_colour_change(pos)

    def option_colour_change(self, pos):
        if self.backButton.is_over(pos):
            self.backButton.color = LIGHTGREY
        else:
            self.backButton.color = GREY


class button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 1, self.y - 1, self.width + 2, self.height + 2), 0)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 35)
            text = font.render(self.text, True, BLACK)
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y +
                               (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False
