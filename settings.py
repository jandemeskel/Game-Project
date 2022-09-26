import pygame
vec = pygame.math.Vector2

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
VERY_DARK = (10, 10, 10)
GREY = (100, 100, 100)
LIGHTGREY = (170, 170, 170)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY
FONT_NAME = 'arial'

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Effects
LIGHT_MASK = "Environment/light_350_med.png"
LIGHT_RADIUS = (700, 700)
BONE_PILE = ""

# Weapon settings
ARROW_IMG = pygame.transform.scale(pygame.image.load('Images/Environment/arrow/Just_arrow.png'), (20, 20))
ARROW_SPEED = 500
ARROW_LIFETIME = 600
ARROW_RATE = 600
ARROW_DMG = 30
ARROW_OFFSET = vec(16, 16)
KICKBACK = 100
BOW_SPREAD = 5

# Player settings
PLAYER_SPEED = 150
PLAYER_HEALTH = 100
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'Character/standing.png'
player_image = pygame.transform.scale(pygame.image.load('Images/Character/down_1.png'), (30, 30))
player_walkLeft_1 = pygame.transform.scale(pygame.image.load('Images/Character/left_1.png'), (30, 30))
player_walkRight_1 = pygame.transform.scale(pygame.image.load('Images/Character/right_1.png'), (30, 30))
player_walkUp_1 = pygame.transform.scale(pygame.image.load('Images/Character/up_1.png'), (30, 30))
player_walkDown_1 = pygame.transform.scale(pygame.image.load('Images/Character/down_1.png'), (30, 30))
player_walkLeft_2 = pygame.transform.scale(pygame.image.load('Images/Character/left_2.png'), (30, 30))
player_walkRight_2 = pygame.transform.scale(pygame.image.load('Images/Character/right_2.png'), (30, 30))
player_walkUp_2 = pygame.transform.scale(pygame.image.load('Images/Character/up_2.png'), (30, 30))
player_walkDown_2 = pygame.transform.scale(pygame.image.load('Images/Character/down_2.png'), (30, 30))
player_walkLeft_3 = pygame.transform.scale(pygame.image.load('Images/Character/left_3.png'), (30, 30))
player_walkRight_3 = pygame.transform.scale(pygame.image.load('Images/Character/right_3.png'), (30, 30))
player_walkUp_3 = pygame.transform.scale(pygame.image.load('Images/Character/up_3.png'), (30, 30))
player_walkDown_3 = pygame.transform.scale(pygame.image.load('Images/Character/down_3.png'), (30, 30))
player_walkLeft_4 = pygame.transform.scale(pygame.image.load('Images/Character/left_4.png'), (30, 30))
player_walkRight_4 = pygame.transform.scale(pygame.image.load('Images/Character/right_4.png'), (30, 30))
player_walkUp_4 = pygame.transform.scale(pygame.image.load('Images/Character/up_4.png'), (30, 30))
player_walkDown_4 = pygame.transform.scale(pygame.image.load('Images/Character/down_4.png'), (30, 30))
player_walkLeft_5 = pygame.transform.scale(pygame.image.load('Images/Character/left_5.png'), (30, 30))
player_walkRight_5 = pygame.transform.scale(pygame.image.load('Images/Character/right_5.png'), (30, 30))
player_walkUp_5 = pygame.transform.scale(pygame.image.load('Images/Character/up_5.png'), (30, 30))
player_walkDown_5 = pygame.transform.scale(pygame.image.load('Images/Character/down_5.png'), (30, 30))
player_walkLeft_6 = pygame.transform.scale(pygame.image.load('Images/Character/left_6.png'), (30, 30))
player_walkRight_6 = pygame.transform.scale(pygame.image.load('Images/Character/right_6.png'), (30, 30))
player_walkUp_6 = pygame.transform.scale(pygame.image.load('Images/Character/up_6.png'), (30, 30))
player_walkDown_6 = pygame.transform.scale(pygame.image.load('Images/Character/down_6.png'), (30, 30))
player_walkLeft_7 = pygame.transform.scale(pygame.image.load('Images/Character/left_7.png'), (30, 30))
player_walkRight_7 = pygame.transform.scale(pygame.image.load('Images/Character/right_7.png'), (30, 30))
player_walkUp_7 = pygame.transform.scale(pygame.image.load('Images/Character/up_7.png'), (30, 30))
player_walkDown_7 = pygame.transform.scale(pygame.image.load('Images/Character/down_7.png'), (30, 30))
player_walkLeft_8 = pygame.transform.scale(pygame.image.load('Images/Character/left_8.png'), (30, 30))
player_walkRight_8 = pygame.transform.scale(pygame.image.load('Images/Character/right_8.png'), (30, 30))
player_walkUp_8 = pygame.transform.scale(pygame.image.load('Images/Character/up_8.png'), (30, 30))
player_walkDown_8 = pygame.transform.scale(pygame.image.load('Images/Character/down_8.png'), (30, 30))
player_hit_rect = pygame.Rect(0, 0, 35, 35)

# orc settings

ORC_SPEED = 85
ORC_HEALTH = 150
ORC_DAMAGE = 15/100
orc_walkleft = pygame.image.load('Images/NPCs/orc_left.png')
orc_walkright = pygame.image.load('Images/NPCs/orc_right.png')
orc_hit_rect = pygame.Rect(0, 0, 30, 30)

# ghost settings
GHOST_SPEED = 70
GHOST_HEALTH = 100
GHOST_DAMAGE = 10/100
ghost_walkleft = pygame.image.load('Images/NPCs/ghost_left.png')
ghost_walkright = pygame.image.load('Images/NPCs/ghost_right.png')
ghost_hit_rect = pygame.Rect(0, 0, 30, 30)

# WIZARD settings
WIZARD_SPEED = 125
WIZARD_HEALTH = 400
WIZARD_DAMAGE = 45/100

wizard_intro = pygame.transform.scale(pygame.image.load('Images/NPCs/Wizarddie2.png'), (50, 50))
wizard_walkleft_1 = pygame.transform.scale(pygame.image.load('Images/NPCs/Wizwalkleft1.png'), (50, 50))
wizard_walkright_1 = pygame.transform.scale(pygame.image.load('Images/NPCs/Wizwalkright1.png'), (50, 50))
wizard_walkleft_2 = pygame.transform.scale(pygame.image.load('Images/NPCs/Wizwalkleft2.png'), (50, 50))
wizard_walkright_2 = pygame.transform.scale(pygame.image.load('Images/NPCs/Wizwalkright2.png'), (50, 50))
wizard_walkleft_3 = pygame.transform.scale(pygame.image.load('Images/NPCs/Wizwalkleft3.png'), (50, 50))
wizard_walkright_3 = pygame.transform.scale(pygame.image.load('Images/NPCs/Wizwalkright3.png'), (50, 50))
wizard_walkleft_4 = pygame.transform.scale(pygame.image.load('Images/NPCs/Wizwalkleft4.png'), (50, 50))
wizard_walkright_4 = pygame.transform.scale(pygame.image.load('Images/NPCs/Wizwalkright4.png'), (50, 50))
wizard_walkleft_5 = pygame.transform.scale(pygame.image.load('Images/NPCs/Wizwalkleft5.png'), (50, 50))
wizard_walkright_5 = pygame.transform.scale(pygame.image.load('Images/NPCs/Wizwalkright5.png'), (50, 50))
wizard_death = pygame.transform.scale(pygame.image.load('Images/NPCs/Wizarddie1.png'), (50, 50))
wizard_fireball = pygame.transform.scale(pygame.image.load('Images/NPCs/wiz_attack_2.png'), (25, 25))
wizard_hit_rect = pygame.Rect(0, 0, 30, 30)

#item settings
fake_sword = pygame.image.load('Images/NPCs/fake_sword.png')
ITEM_IMGS = {'bow': 'Environment/bow.png', 'potion': 'Environment/flasks/flasks_1_1.png'}
POTION_HEALTH = 20
