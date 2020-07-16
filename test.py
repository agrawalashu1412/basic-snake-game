import pygame
import random
import os


pygame.mixer.init()

pygame.init()

# background image

bgimg = pygame.image.load('image3.jpg')
bgimg = pygame.transform.scale(bgimg, (1320, 760))

startimage = pygame.image.load('snakestart.jpeg')
startimage = pygame.transform.scale(startimage, (1320, 760))





# DEfining colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
GREEN = (0, 255, 0 )
SHADOW = (192, 192, 192)
LIGHTBLUE= (0, 0, 235)
LIGHTRED= (255, 100, 100)
YELLOW=(250,200,0)
pink = (255,200,200)
gray=(128,128,128)
Aqua=(0,128,128)
PURPLE = (102, 0, 102)
lightpink=(255,183,193)
hotpink=(255,105,180)



#window creation
gameWindow=pygame.display.set_mode((1320,720))






#Game Title
pygame.display.set_caption("My first Project in Python")
pygame.display.update()

clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def  plot_snake(gameWindow,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(startimage, (0, 0))
        # text_screen("Welcome to Snake's World",black,340,320)
        # text_screen("Press Space Bar To Play ",black,359,360)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:

                    pygame.mixer.music.load("harrypotter.mp3")
                    pygame.mixer.music.play(-1)

                    game_loop()

        pygame.display.update()
        clock.tick(60)

#creating a game loop
def game_loop():
 # game specific variables
    exit_game = False
    game_over = False
    snake_x = 35
    snake_y = 39
    snake_size = 20
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    fps = 55
    score = 0
    food_x = random.randint(0, 1000)
    food_y = random.randint(0, 500)
    snake_list = []
    snake_length = 1




    with open("hiscore.txt", "r") as f:
        hiscore = f.read()




    while not exit_game:

        if game_over:
            endimage = pygame.image.load("endsnake.jpg")

            endimage = pygame.transform.scale(endimage, (1320, 760))
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)

            gameWindow.blit(endimage, (0, 0))

            # text_screen("Game Over Guys,Try it Again",red,340,320)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        welcome()



        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0

                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0

                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0

                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score +=10
                food_x = random.randint(5, 1000)
                food_y = random.randint(5, 500)
                snake_length +=5
                if score>int(hiscore):
                    hiscore = score



            # try :
            #     if abs(snake_x - food_x)<6 and abs(snake_y-food_y)<6:
            #         score +=10
            #         food_x = random.randint(5, 1000)
            #         food_y = random.randint(5, 500)
            #         snake_length +=5
            #         score > int(hiscore)
            #         hiscore = score


            # except ValueError:
            #     pass


                # try:
                #     score > int(hiscore)

                        # int(hiscore) = score
                # except ValueError:
                #     pass



            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0, 0))
            text_screen("score:" + str(score) + "   Highest Score:"+str(hiscore), red, 5, 5)

            # pygame.draw.circle(gameWindow, hotpink, (65, 76), 15, snake_size)


            pygame.draw.rect(gameWindow,hotpink,[food_x,food_y,snake_size,snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over=True

                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)


            if snake_x<0 or snake_x>1310 or snake_y<0 or snake_y>710:
                game_over=True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)

            plot_snake(gameWindow,GREEN,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()







