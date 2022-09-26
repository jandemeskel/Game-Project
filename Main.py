import pygame
import sys
import os
from settings import *
from sprites import *
from tilemap import *
import Menu
from os import path

def draw_player_health(surf,x,y,pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 300
    BAR_HEIGHT = 10
    fill = pct * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    if pct > 0.6:
        col = GREEN
    elif pct > 0.3:
        col = YELLOW
    else:
        col = RED
    pygame.draw.rect(surf, col, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect,2)

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.Surface((WIDTH, HEIGHT))
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()
        self.playing = False
        self.main_menu = Menu.MainMenu(self)
        self.options = Menu.OptionsMenu(self)
        self.curr_menu = self.main_menu
        self.font_name = pygame.font.match_font(FONT_NAME)
        self.game_win = False


    # text functionality, default font is arial, position is midtop
    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'Images')
        # game paused, a transparent screen displays
        self.dim_screen = pygame.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0, 0, 0, 100))

        self.dark = pygame.Surface((WIDTH, HEIGHT))
        self.dark.fill(DARKGREY)
        self.light_mask = pygame.image.load(path.join(img_folder, LIGHT_MASK)).convert_alpha()
        self.light_mask = pygame.transform.scale(self.light_mask, LIGHT_RADIUS)
        self.light_rect = self.light_mask.get_rect()
        self.arrow_img = ARROW_IMG.convert_alpha()
        self.arrow_image2 = pygame.image.load('Images/Environment/arrow/Just_arrow.png').convert_alpha()
        self.player_img = pygame.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.item_images = {}
        for item in ITEM_IMGS:
            self.item_images[item] = pygame.image.load(path.join(img_folder, ITEM_IMGS[item])).convert_alpha()


    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.arrows = pygame.sprite.Group()
        self.arrows2 = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.map = TiledMap('Maps/Maze.tmx')
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.room1 = pygame.sprite.Group()
        self.room2 = pygame.sprite.Group()
        self.room3 = pygame.sprite.Group()
        self.room = 1
        self.info_box = True
        self.vision = True
        self.paused = False
        self.draw_debug = False
        self.bow = False
        self.sword = False

        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x + tile_object.width / 2,
                             tile_object.y + tile_object.height / 2)
            if tile_object.name == 'Spawn':
                self.player = Player(self, tile_object.x, tile_object.y)

            if tile_object.name == 'Wall':
                Obstacle(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)

            if tile_object.name == 'orc':
                OrcMob(self, tile_object.x, tile_object.y)

            if tile_object.name == 'ghost':
                GhostMob(self, tile_object.x, tile_object.y)

            if tile_object.name == 'Wizard':
                Wizard(self, tile_object.x, tile_object.y)

            if tile_object.name == 'room1':
                Room1(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

            if tile_object.name == 'room2':
                Room2(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

            if tile_object.name == 'room3':
                Room3(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

            if tile_object.name in ['bow']:
                Item(self, obj_center, tile_object.name)

            if tile_object.name in ['potion']:
                Item(self, obj_center, tile_object.name)

        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False


    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            if not self.paused:
                self.update()
            self.draw()



    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        # Player hits item
        hits = pygame.sprite.spritecollide(self.player, self.items, False)
        for hit in hits:
            if hit.type == 'bow':
                hit.kill()
                self.bow = True
                self.sword = False
            if hit.type == 'potion' and self.player.health < PLAYER_HEALTH:
                hit.kill()
                self.player.add_health(POTION_HEALTH)
        # Arrow hits mob
        hits = pygame.sprite.groupcollide(self.mobs, self.arrows, False, True)
        for hit in hits:
            hit.health -= ARROW_DMG
        #    hit.vel = vec(0, 0)
        # Ghost hit player
        hits = pygame.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
        for hit in hits:
            self.player.health -= GHOST_DAMAGE
        #    hit.vel = vec(0, 0)
            if self.player.health <= 0:
                self.playing =  False
        # Wizard arrows
        hits = pygame.sprite.spritecollide(self.player, self.arrows2, False, collide_hit_rect)
        for hit in hits:
            self.player.health -= GHOST_DAMAGE
            #    hit.vel = vec(0, 0)
            if self.player.health <= 0:
                self.playing = False
        #if hits:
            #self.player.pos += vec(ORC_KNOCKBACK, 0).rotate(-hits[0].rot)
            #self.player.pos += vec(GHOST_KNOCKBACK, 0)
        # Orc hit player
        hits = pygame.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
        for hit in hits:
            self.player.health -= ORC_DAMAGE
        #    hit.vel = vec(0, 0)
            if self.player.health <= 0:
                self.playing =  False

        #if hits:
            #self.player.pos += vec(ORC_KNOCKBACK, 0).rotate(-hits[0].rot)
            #self.player.pos += vec(ORC_KNOCKBACK, 0)


    def draw(self):
        #self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.draw_debug:
                pygame.draw.rect(self.screen, GREEN, self.camera.apply_rect(sprite.rect), 1)
            if isinstance(sprite, OrcMob):
                sprite.draw_health()
            if isinstance(sprite, GhostMob):
                sprite.draw_health()
        if self.draw_debug:
            for wall in self.walls:
                pygame.draw.rect(self.screen, GREEN, self.camera.apply_rect(wall.rect), 1)
        if self.vision:
            self.render_darkness()
        if self.info_box:
            self.render_info_box(self.room)
        draw_player_health(self.screen, 50, 10, self.player.health/ PLAYER_HEALTH)
        if self.paused:
            self.screen.blit(self.dim_screen, (0, 0))
            self.draw_text("Paused", 60, YELLOW, WIDTH / 2, HEIGHT / 3)
        pygame.display.flip()

    def events(self):
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.show_start_screen()
                # if event.key == pygame.K_h:
                #     self.draw_debug = not self.draw_debug
                # if event.key == pygame.K_v:
                #     self.vision = not self.vision
                if event.key == pygame.K_i:
                    self.info_box = not self.info_box
                # if event.key == pygame.K_b:
                #     self.bow = not self.bow
                if event.key == pygame.K_p:
                    self.paused = not self.paused

    def render_darkness(self):
        self.dark.fill(VERY_DARK)
        self.light_rect.center = self.camera.apply(self.player).center
        self.dark.blit(self.light_mask, self.light_rect)
        self.screen.blit(self.dark, (0, 0), special_flags=pygame.BLEND_MULT)

    def render_info_box(self,room):
        if room == 1:
            self.screen.blit(pygame.image.load('Images/info1.png'),(300,200))

        elif room == 2:
            self.screen.blit(pygame.image.load('Images/info2.png'),(300,200))

        elif room == 3:
            self.screen.blit(pygame.image.load('Images/info3.png'),(300,200))

    def show_start_screen(self):
        while not self.playing:
            self.curr_menu.display_menu()

    def show_go_screen(self):
        if self.game_win == True:
            # self.screen.fill(BLACK)

            # self.draw_text("Congratulations!", 48, GREEN, WIDTH / 2, HEIGHT / 4)
            # self.draw_text("You have defeated the evil Wizard. Press a key to play again", 20,
            #                WHITE, WIDTH / 2, HEIGHT / 2)
            self.screen.blit(pygame.image.load('Images/winscreen.jpg'),(0,0))
        else:
            # self.screen.fill(BLACK)
            self.screen.blit(pygame.image.load('Images/gameover.jpg'),(0,0))
            # self.draw_text("Game Over", 48, RED, WIDTH / 2, HEIGHT / 4)
            # self.draw_text("You lose your life. Press a key to play again", 20,
            #                WHITE, WIDTH / 2, HEIGHT / 2)


        pygame.display.flip()
        self.game_win = False
        self.wait_for_key()



    def wait_for_key(self):
        pygame.event.wait()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                       waiting = False
                    elif event.key == pygame.K_ESCAPE:
                        waiting = False
                        self.quit()
