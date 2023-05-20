import pygame
import time
import random
 
pygame.init() # Инициируем окно
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 640
dis_height = 480
 
dis = pygame.display.set_mode((dis_width, dis_height)) # устанавливаем размеры окна
pygame.display.set_caption('Snake Game by Surmin') # Заглавие окна
 
clock = pygame.time.Clock()
 
snake_block = 10 #Размер блока змеи
snake_speed = 15 #Скорость змеи
 
font_style = pygame.font.SysFont("bahnschrift", 25) #Установка разных стилей для текста
score_font = pygame.font.SysFont("comicsansms", 35)
 
 #Функция изначальной отрисовки очков
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
 #Функция отрисовки змеи. Блок - голова змеи, список - её тело
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 #Отображение сообщения для пользователя. Используется для GAME OVER
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 #Игровой цикл
def gameLoop():
    #Инициализация базовых значений для игры
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    #Генерация еды
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    #Пока  игрок не проиграл
    while not game_over:
        
        while game_close == True:
            dis.fill(blue)
            message("Once more?", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            #Смотрим нажатие кнопок. Если ESC, то закончили. "C" - начинаем заново
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            #Кнопки управление. Манипуляция переменными направления движения змеи
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        #Проверка, если змея вышла за пределы игрового поля
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        #Проверка, если змея кусила саму себя
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        #Перерисовывем змею на экране
        our_snake(snake_block, snake_List)
        #Высчитываем очки игрока как длина змеи минус 1
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        #Если змея скушала что-то, то добавляем ей длины
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        #Тик для движений
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()