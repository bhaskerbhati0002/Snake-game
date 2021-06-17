import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0,255,0)
cyan = (0,255,255)
blue = (0,0,255)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snake_game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
move = pygame.mixer.Sound('gallery/audio/wing.wav')
die = pygame.mixer.Sound('gallery/audio/hit.wav')
win = pygame.mixer.Sound('gallery/audio/point.wav')
bonus = pygame.mixer.Sound('gallery/audio/bonus.mp3')

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 2
    snake_size = 30
    fps = 60
    ch=1
    ch_1=0
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    exit_game = True

                if event.key == pygame.K_ESCAPE:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        move.play()
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        move.play()
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        move.play()
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        move.play()
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_ESCAPE:
                        exit_game=True

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<6:

                win.play()
                score +=1
                ch=score
                if ch_1==1:
                    bonus.play()
                    score=score+4
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                if ch_1==1:
                    snk_length +=20
                if ch_1==0:
                    snk_length += 5

            if ch%5==0:
                gameWindow.fill(black)
                pygame.draw.rect(gameWindow, blue, [food_x, food_y, snake_size, snake_size])
                ch_1=1

            else:
                gameWindow.fill(black)
                pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
                ch_1=0

            text_screen("Score: " + str(score * 10), cyan, 5, 5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                die.play()
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                die.play()
                game_over = True
            plot_snake(gameWindow, green, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameloop()