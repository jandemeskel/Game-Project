import pygame
from settings import *
from random import uniform
from tilemap import collide_hit_rect
vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = player_walkDown_1
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH, HEIGHT)
        self.hit_rect = self.rect
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.rot = 0
        self.walkCount_Left = 1
        self.walkCount_Right = 1
        self.walkCount_Up = 1
        self.walkCount_Down = 1
        self.last_shot = 0
        self.health = PLAYER_HEALTH


    def get_keys(self):
        self.vel.x, self.vel.y = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel.x = -PLAYER_SPEED
            if self.walkCount_Left == 1:
                self.image = player_walkLeft_1
            elif self.walkCount_Left == 4:
                self.image = player_walkLeft_2
            elif self.walkCount_Left == 7:
                self.image = player_walkLeft_3
            elif self.walkCount_Left == 10:
                self.image = player_walkLeft_4
            elif self.walkCount_Left == 13:
                self.image = player_walkLeft_5
            elif self.walkCount_Left == 16:
                self.image = player_walkLeft_6
            elif self.walkCount_Left == 19:
                self.image = player_walkLeft_7
            elif self.walkCount_Left == 22:
                self.image = player_walkLeft_8
                self.walkCount_Left = 1
            self.rot = 180
            self.walkCount_Left = self.walkCount_Left +1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel.x = PLAYER_SPEED
            if self.walkCount_Right == 1:
                self.image = player_walkRight_1
            elif self.walkCount_Right == 4:
                self.image = player_walkRight_2
            elif self.walkCount_Right == 7:
                self.image = player_walkRight_3
            elif self.walkCount_Right == 10:
                self.image = player_walkRight_4
            elif self.walkCount_Right == 13:
                self.image = player_walkRight_5
            elif self.walkCount_Right == 16:
                self.image = player_walkRight_6
            elif self.walkCount_Right == 19:
                self.image = player_walkRight_7
            elif self.walkCount_Right == 22:
                self.image = player_walkRight_8
                self.walkCount_Right = 1
            self.rot = 0
            self.walkCount_Right = self.walkCount_Right +1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vel.y = -PLAYER_SPEED
            if self.walkCount_Up == 1:
                self.image = player_walkUp_1
            elif self.walkCount_Up == 4:
                self.image = player_walkUp_2
            elif self.walkCount_Up == 7:
                self.image = player_walkUp_3
            elif self.walkCount_Up == 10:
                self.image = player_walkUp_4
            elif self.walkCount_Up == 13:
                self.image = player_walkUp_5
            elif self.walkCount_Up == 16:
                self.image = player_walkUp_6
            elif self.walkCount_Up == 19:
                self.image = player_walkUp_7
            elif self.walkCount_Up == 22:
                self.image = player_walkUp_8
                self.walkCount_Up = 1
            self.rot = 90
            self.walkCount_Up = self.walkCount_Up +1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vel.y = PLAYER_SPEED
            if self.walkCount_Down == 1:
                self.image = player_walkDown_1
            elif self.walkCount_Down == 4:
                self.image = player_walkDown_2
            elif self.walkCount_Down == 7:
                self.image = player_walkDown_3
            elif self.walkCount_Down == 10:
                self.image = player_walkDown_4
            elif self.walkCount_Down == 13:
                self.image = player_walkDown_5
            elif self.walkCount_Down == 16:
                self.image = player_walkDown_6
            elif self.walkCount_Down == 19:
                self.image = player_walkDown_7
            elif self.walkCount_Down == 22:
                self.image = player_walkDown_8
                self.walkCount_Down = 1
            self.rot = 270
            self.walkCount_Down = self.walkCount_Down +1

        if self.game.bow:
            if keys[pygame.K_SPACE]:
                now = pygame.time.get_ticks()
                if now - self.last_shot > ARROW_RATE:
                    self.last_shot = now
                    dir = vec(1, 0).rotate(-self.rot)
                    pos = self.pos + ARROW_OFFSET
                    Arrow(self.game, pos, dir, self.rot)
                    self.vel -= vec(KICKBACK, 0).rotate(self.rot)

        if self.vel.x != 0 and self.vel.y != 0:
            self.vel.x *= 0.7071
            self.vel.y *= 0.7071

    def collide_with_walls(self, dir):
            if dir == 'x':
                hits = pygame.sprite.spritecollide(self, self.game.walls, False)
                if hits:
                    if self.vel.x > 0:
                        self.pos.x = hits[0].rect.left - self.rect.width
                    if self.vel.x < 0:
                        self.pos.x = hits[0].rect.right
                    self.vel.x = 0
                    self.rect.x = self.pos.x
            if dir == 'y':
                hits = pygame.sprite.spritecollide(self, self.game.walls, False)
                if hits:
                    if self.vel.y > 0:
                        self.pos.y = hits[0].rect.top - self.rect.height
                    if self.vel.y < 0:
                        self.pos.y = hits[0].rect.bottom
                    self.vel.y = 0
                    self.rect.y = self.pos.y

    def update(self):
        self.get_keys()
        self.pos.x += self.vel.x * self.game.dt
        self.pos.y += self.vel.y * self.game.dt
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')
        self.rect.center = self.hit_rect.center
        self.collide_with_room1()
        self.collide_with_room2()
        self.collide_with_room3()
    #    print(self.vel.x)
        #print(self.vel.y)

    def collide_with_room1(self):

            hits = pygame.sprite.spritecollide(self, self.game.room1, False)
            if hits:
                if self.game.room != 1:
                    self.game.room = 1
                    self.game.info_box = not self.game.info_box
    def collide_with_room2(self):

        hits = pygame.sprite.spritecollide(self, self.game.room2, False)
        if hits:
            if self.game.room !=2:
                self.game.room =2
                self.game.info_box = not self.game.info_box
    def collide_with_room3(self):

            hits = pygame.sprite.spritecollide(self, self.game.room3, False)
            if hits:
                if self.game.room !=3:
                    self.game.room = 3
                    self.game.info_box = not self.game.info_box

    def add_health(self, amount):
        self.health += amount
        if self.health > PLAYER_HEALTH:
            self.health = PLAYER_HEALTH

class OrcMob(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = orc_walkleft
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.rect.center = self.pos
        self.hit_rect = self.rect
        self.health = ORC_HEALTH

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x > 0:
                    #print('moving right')
                    self.pos.x = hits[0].rect.left - self.rect.width
                elif self.vel.x < 0:
                    #print('moving left')
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    #print('moving down')
                    self.pos.y = hits[0].rect.top - self.rect.height
                elif self.vel.y < 0:
                    #print('moving up')
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y

        #self.vel = vec(ORC_SPEED)


    def update(self):

        if (self.pos.x > (self.game.player.pos.x - 100) and self.pos.x < (self.game.player.pos.x + 100)) and ((self.pos.y > self.game.player.pos.y - 100 ) and (self.pos.y < self.game.player.pos.y + 100)):

            if (self.pos.x + 10 < self.game.player.pos.x):
                self.image = orc_walkright
                self.vel.x = ORC_SPEED
                self.pos.x += self.vel.x * self.game.dt

            if (self.pos.x - 10 > self.game.player.pos.x):
                self.image = orc_walkleft
                self.vel.x = -1 * ORC_SPEED
                self.pos.x += self.vel.x * self.game.dt


            if (self.pos.y + 10 < self.game.player.pos.y ):
                self.vel.y = ORC_SPEED
                self.pos.y += self.vel.y * self.game.dt

            if (self.pos.y - 10 > self.game.player.pos.y):
                self.vel.y = -1 * ORC_SPEED
                self.pos.y += self.vel.y * self.game.dt



        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        # self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')
        self.rect.center = self.pos
        if self.health <= 0:
            self.kill()
        #print(self.vel.x)
        #print(self.vel.y)

    def draw_health(self):
        if self.health > 165:
            col = GREEN
        elif self.health > 80:
            col = YELLOW
        else:
            col = RED
        width = int(self.rect.width * self.health / 100)
        self.health_bar = pygame.Rect(0, 0, width, 3)
        if self.health < 249:
            pygame.draw.rect(self.image, col, self.health_bar)

class GhostMob(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = fake_sword
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.vel = vec(GHOST_SPEED, GHOST_SPEED)
        self.rect.center = self.pos
        self.health = GHOST_HEALTH

    def update(self):

        if (self.pos.x > (self.game.player.pos.x - 150) and self.pos.x < (self.game.player.pos.x + 150)) and ((self.pos.y > self.game.player.pos.y - 150 ) and (self.pos.y < self.game.player.pos.y + 150)):

            if (self.pos.x + 10 < self.game.player.pos.x):
                self.image = ghost_walkright
                self.pos.x += self.vel.x * self.game.dt

            elif (self.pos.x - 10 > self.game.player.pos.x):
                self.image = ghost_walkleft
                self.pos.x -= self.vel.x * self.game.dt

            else:
                if (self.pos.y + 10 < self.game.player.pos.y ):
                    self.image = ghost_walkright
                    self.pos.y += self.vel.y * self.game.dt

                elif (self.pos.y - 10 > self.game.player.pos.y):
                    self.image = ghost_walkleft
                    self.pos.y -= self.vel.y * self.game.dt

                else:
                    pass

        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.rect.center = self.pos
        if self.health <= 0:
            self.kill()

    def draw_health(self):
        if self.health > 60:
            col = GREEN
        elif self.health > 30:
            col = YELLOW
        else:
            col = RED
        width = int(self.rect.width * self.health / 100)
        self.health_bar = pygame.Rect(0, 0, width, 3)
        if self.health < 99:
            pygame.draw.rect(self.image, col, self.health_bar)

class Arrow2(pygame.sprite.Sprite):
    def __init__(self, game, pos, dir, rot):
        self.groups = game.all_sprites, game.arrows2
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.transform.rotate(wizard_fireball, 90 + rot)
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        #self.rect.center = pos
        spread = uniform(-BOW_SPREAD, BOW_SPREAD)
        self.vel = dir.rotate(spread) * ARROW_SPEED
        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        if pygame.sprite.spritecollideany(self, self.game.walls):
            self.kill()

class Wizard(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = wizard_intro
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.rect.center = self.pos
        self.hit_rect = self.rect
        self.health = WIZARD_HEALTH
        self.wizwalkCount_right = 0
        self.wizwalkCount_left = 0
        self.projectile = Arrow
        self.wiz_attack_no = 1
        self.movement = False
        self.delay = 0
        self.start_time = 0
        self.phaseTwo = False


    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x > 0:

                    self.pos.x = hits[0].rect.left - self.rect.width
                elif self.vel.x < 0:

                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:

                    self.pos.y = hits[0].rect.top - self.rect.height
                elif self.vel.y < 0:

                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y

# 360 shooting
    def attack_1(self):
        n = 0
        while n < 360:
            rot = n
            dir = vec(1, 0).rotate(-rot)
            Arrow2(self.game, self.pos, dir,rot)
            n += 1

    def attack_2(self):
        if self.phaseTwo == True:
            rot = 0
            dir = vec(1, 0).rotate(-rot)
            Arrow2(self.game, self.pos, dir,rot)

    def update(self):
        if self.wiz_attack_no > 0:
            self.wiz_attack_no +=1
        if self.wiz_attack_no == 100:
            self.attack_1()
            self.movement = False
        if self.wiz_attack_no > 250:
            self.movement = True
        if self.wiz_attack_no > 500:
            self.movement = False
            self.phaseTwo = True
            self.attack_2()
        if self.wiz_attack_no == 700:
            self.phaseTwo = False
            self.movement = True
            self.wiz_attack_no = 1
        if (self.pos.x > (self.game.player.pos.x - 250) and self.pos.x < (self.game.player.pos.x + 250)) and ((self.pos.y > self.game.player.pos.y - 250 ) and (self.pos.y < self.game.player.pos.y + 250)):

            if self.movement == True:

                if (self.pos.x + 20 < self.game.player.pos.x):
                    if self.wizwalkCount_left == 1:
                        self.image = wizard_walkleft_1
                    elif self.wizwalkCount_left == 4:
                        self.image = wizard_walkleft_2
                    elif self.wizwalkCount_left == 7:
                        self.image = wizard_walkleft_3
                    elif self.wizwalkCount_left == 10:
                        self.image = wizard_walkleft_4
                    elif self.wizwalkCount_left == 13:
                        self.image = wizard_walkleft_5
                        self.wizwalkCount_left = 1
                    self.vel.x = WIZARD_SPEED
                    self.pos.x += self.vel.x * self.game.dt
                    self.wizwalkCount_left = self.wizwalkCount_left + 1


                if (self.pos.x - 20 > self.game.player.pos.x):
                    if self.wizwalkCount_right == 1:
                        self.image = wizard_walkright_1
                    elif self.wizwalkCount_right == 4:
                        self.image = wizard_walkright_2
                    elif self.wizwalkCount_right == 7:
                        self.image = wizard_walkright_3
                    elif self.wizwalkCount_right == 10:
                        self.image = wizard_walkright_4
                    elif self.wizwalkCount_right == 13:
                        self.image = wizard_walkright_5
                        self.wizwalkCount_right = 1
                    self.vel.x = -1 * WIZARD_SPEED
                    self.pos.x += self.vel.x * self.game.dt
                    self.wizwalkCount_right = self.wizwalkCount_right + 1


                if (self.pos.y + 20 < self.game.player.pos.y ):
                    self.vel.y = WIZARD_SPEED
                    self.pos.y += self.vel.y * self.game.dt

                if (self.pos.y - 20 > self.game.player.pos.y):
                    self.vel.y = -1 * WIZARD_SPEED
                    self.pos.y += self.vel.y * self.game.dt



        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')
        self.rect.center = self.pos
        if self.health <= 0:
            self.kill()
            self.game.game_win = True
            self.game.playing = False

    def draw_health(self):
        if self.health > 165:
            col = GREEN
        elif self.health > 80:
            col = YELLOW
        else:
            col = RED
        width = int(self.rect.width * self.health / 100)
        self.health_bar = pygame.Rect(0, 0, width, 3)
        if self.health < 249:
            pygame.draw.rect(self.image, col, self.health_bar)

class Arrow(pygame.sprite.Sprite):
    def __init__(self, game, pos, dir, rot):
        self.groups = game.all_sprites, game.arrows
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.transform.rotate(self.game.arrow_img, 90 + rot)
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.rect.center = pos
        spread = uniform(-BOW_SPREAD, BOW_SPREAD)
        self.vel = dir.rotate(spread) * ARROW_SPEED
        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        if pygame.sprite.spritecollideany(self, self.game.walls):
            self.kill()
        if pygame.time.get_ticks() - self.spawn_time > ARROW_LIFETIME:
            self.kill()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.image.load('Maps/tiles/brick.png')
        self.rect = pygame.Rect(x, y, w, h)
        self.rect.center = (WIDTH, HEIGHT)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Room1(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.room1
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x, y, w, h)
        self.rect.center = (WIDTH, HEIGHT)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Room2(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.room2
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x, y, w, h)
        self.rect.center = (WIDTH, HEIGHT)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Room3(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.room3
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x, y, w, h)
        self.rect.center = (WIDTH, HEIGHT)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Item(pygame.sprite.Sprite):
    def __init__(self, game, pos, type):
        self.groups = game.all_sprites, game.items
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.item_images[type]
        self.rect = self.image.get_rect()
        self.type = type
        self.rect.center = pos
