import pygame, sys
from pygame.locals import *
from random import randrange
from pygame import mixer

# Initialising pygame
pygame.init()
clock = pygame.time.Clock()

# Defining size of game window and background picture
screen = pygame.display.set_mode((1920, 1080)) 
background = pygame.image.load('field.png')

# Sound
mixer.music.load("music.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.1)

# Caption and Icon
pygame.display.set_caption("Recycling is FUN!")
icon = pygame.image.load('glass-bin.png')
pygame.display.set_icon(icon)

# Score and Lives counter
score_value = 0
lives_value = 3
eliminated_value = 0
font = pygame.font.Font("freesansbold.ttf", 64)
instruction_font = pygame.font.Font("freesansbold.ttf", 40)
over_font = pygame.font.Font('freesansbold.ttf', 128)

# Definitions for text displays
def show_score():
    score = font.render("Score: " + str(score_value), True, (0, 255, 0))
    screen.blit(score, (10, 10))

def show_lives():
    lives = font.render("Lives: " + str(lives_value), True, (255, 0, 0))
    screen.blit(lives, (1620, 10))

def instructions():
    instruction = instruction_font.render("DRAG TO THE CORRECT BIN!", True, (255, 255, 255))
    screen.blit(instruction, (685, 20))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (535, 460))

fun_fact_randomizer = randrange(0, 9)
def fun_fact(fun_fact_randomizer):
    if fun_fact_randomizer == 0:
        text1 = font.render("Fun Fact: Food should be discarded in general waste, as", True, (255, 111, 255))
        text2 = font.render("they cannot be recycled!", True, (255, 111, 255))
    elif fun_fact_randomizer == 1:
        text1 = font.render("Fun Fact: Plastic disposables such as plates & cups should", True, (255, 111, 255))
        text2 = font.render("be discarded in general waste, as they cannot be recycled!", True, (255, 111, 255))
    elif fun_fact_randomizer == 2:
        text1 = font.render("Fun Fact: Plastic or Glass jars that can be cleaned should be", True, (255, 111, 255))
        text2 = font.render("completely free from food contaminants before recycling!", True, (255, 111, 255))
    elif fun_fact_randomizer == 3:
        text1 = instruction_font.render("Fun Fact: Tissue paper should not be recycled. It is already made from recycled paper. So, ", True, (255, 111, 255))
        text2 = instruction_font.render("it's fibres are too short for recycling!", True, (255, 111, 255))
    elif fun_fact_randomizer == 4:
        text1 = font.render("Fun Fact: Recycling 1,000kg of paper saves 17 trees!", True, (255, 111, 255))
        text2 = font.render(" ", True, (255, 111, 255))
    elif fun_fact_randomizer == 5:
        text1 = font.render("Fun Fact: Recycling an aluminium can saves 95% of the", True, (255, 111, 255))
        text2 = font.render("energy used to make a new one!", True, (255, 111, 255))
    elif fun_fact_randomizer == 6:
        text1 = font.render("Fun Fact: Recycling a glass bottle saves 30% of the energy", True, (255, 111, 255))
        text2 = font.render("used to make a new one!", True, (255, 111, 255))
    elif fun_fact_randomizer == 7:
        text1 = font.render("Not a Fun Fact: Most of Singapore’s trash is incinerated :(", True, (255, 111, 255))
        text2 = font.render(" ", True, (255, 111, 255))
    elif fun_fact_randomizer == 8:
        text1 = font.render("Not a Fun Fact: 40 per cent of trash placed into recycling", True, (255, 111, 255))
        text2 = font.render("bins are contaminated, and thus incinerated :(", True, (255, 111, 255))
    screen.blit(text1, (10, 600))
    screen.blit(text2, (10, 650))

# Recycling Bins
bin1 = pygame.image.load('glass-bin.png')
bin2 = pygame.image.load('paper-bin.png')
bin3 = pygame.image.load('plastic-bin.png')
bin4 = pygame.image.load('metal-bin.png')
bin5 = pygame.image.load('general-waste-bin.png')

bin_array = [bin1, bin2, bin3, bin4, bin5]
bin_rect_array = []
for i in range(5):
    x = bin_array[i]
    rect = x.get_rect()
    rect.center = 92 + 384 * i, 800
    bin_rect_array.append(rect)

# Glass
g1 = pygame.image.load('trash/glass-cup-1.png')
g2 = pygame.image.load('trash/glass-cup-2.png')
g3 = pygame.image.load('trash/glass-jar.png')
# Metal
m1 = pygame.image.load('trash/metal-can-1.png')
m2 = pygame.image.load('trash/metal-can-2.png')
m3 = pygame.image.load('trash/metal-can-3.png')
m4 = pygame.image.load('trash/metal-tuna-can.png')
# Paper
p1 = pygame.image.load('trash/paper-cereal-carton.png')
p2 = pygame.image.load('trash/paper-coffee-cup.png')
p3 = pygame.image.load('trash/paper-milk-carton.png')
p4 = pygame.image.load('trash/paper-news.png')
p5 = pygame.image.load('trash/paper-box.png')
# Plastic
s1 = pygame.image.load('trash/plastic-drink-1.png')
s2 = pygame.image.load('trash/plastic-bag.png')
s3 = pygame.image.load('trash/plastic-bucket.png')

# Can't be recycled
norecycle1 = pygame.image.load('trash/apple.png')
norecycle2 = pygame.image.load('trash/tissue.png')
norecycle3 = pygame.image.load('trash/battery.png')
norecycle4 = pygame.image.load('trash/vege.png')

# Set maximum high score achievable
MAX_TRASH = 40

# Store all images and it's properties
image_array = [g1, g2, g3, m1, m2, m3, m4, p1, p2, p3, p4, p5, s1, s2, s3, norecycle1, norecycle2, norecycle3, norecycle4]
num_images = len(image_array)
bin1_elements = [g1, g2, g3]
bin2_elements = [p1, p2, p3, p4, p5]
bin3_elements = [s1, s2, s3, g3]
bin4_elements = [m1, m2, m3, m4]
bin5_elements = [norecycle1, norecycle2, norecycle3, norecycle4]
bin_all = [bin1_elements, bin2_elements, bin3_elements, bin4_elements, bin5_elements]

image_on_screen = []
image_on_hold = []
rect_array = [] 
image_x_array = []
image_y_array = []
moving = []
eliminated = []

for i in range(MAX_TRASH):
    x = image_array[randrange(num_images)]
    image_on_hold.append(x)
    rect = x.get_rect()
    image_x = randrange(200, 1800)
    image_x_array.append(image_x)
    image_y = 50
    image_y_array.append(image_y)
    rect.center = image_x, image_y
    rect_array.append(rect)
    moving.append(False)
    eliminated.append(False)


# Timer globals
constant_time = 0
Y_increase = 0
timer1 = 300
timer2 = 0
index = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            for i in range(len(rect_array)):
                if rect_array[i].collidepoint(event.pos) == True:
                    moving[i] = True
                    break;
        elif event.type == MOUSEBUTTONUP:
            for i in range(len(rect_array)):
                moving[i] = False
        elif event.type == MOUSEMOTION:
            for i in range(len(rect_array)):
                if moving[i] == True:
                    rect_array[i].move_ip(event.rel)
                    for j in range(5):
                        if pygame.Rect.colliderect(bin_rect_array[j], rect_array[i]) == True:
                            if image_on_hold[i] in bin_all[j] and lives_value > 0:
                                score_value += 1
                            else:
                                lives_value -= 1
                            rect_array[i].center = 0, 0
                            eliminated[i] = True
                            eliminated_value += 1


    if timer1 == 0 and index < MAX_TRASH:
        image_on_screen.append(image_on_hold[index])
        index += 1
        timer1 = 300 - (timer2 * 2)
        if constant_time >= 6 and constant_time < 15:
            timer2 = 80
        elif constant_time >= 15 and constant_time < 25:
            timer2 = 100
            Y_increase = 1.5
        elif constant_time >= 25:
            timer2 = 125
            Y_increase = 1.5
    constant_time += 0.01
    timer1 += -1

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    screen.blit(bin1, (92, 800))
    screen.blit(bin2, (476, 800))
    screen.blit(bin3, (860, 800))
    screen.blit(bin4, (1244, 800))
    screen.blit(bin5, (1628, 800))

    for i in range(len(image_on_screen)):
        if eliminated[i] == False:
            screen.blit(image_on_screen[i], rect_array[i])
        if moving[i] == False and eliminated[i] == False:
            image_y_array[i] += 4 + Y_increase
            rect_array[i].center = image_x_array[i], image_y_array[i]
            if image_y_array[i] > 920:
                lives_value -= 1
                rect_array[i].center = 0, 0
                image_y_array[i] = 0
                eliminated[i] = True
                eliminated_value += 1

    if lives_value < 1 or eliminated_value == MAX_TRASH:
        lives_value = 0
        game_over_text()
        fun_fact(fun_fact_randomizer)
        
    show_score()
    show_lives()
    instructions()
    pygame.display.update()
    clock.tick(60)