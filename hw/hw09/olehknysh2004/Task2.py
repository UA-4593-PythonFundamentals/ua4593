import pygame

FPS = 60

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500

COORD_X=50
COORD_Y=50
WIDTH_RECTANGLE=40
HEIGHT_RECTANGLE=60
DELTA_STEP=5

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()


gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first game")


run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    CURRENT_W = gameDisplay.get_width() #додав моніторинг зміни ширини вікна
    CURRENT_H = gameDisplay.get_height() #додав моніторинг зміни висоти вікна

    if keys[pygame.K_LEFT] and COORD_X > 0: #дозволений рух фігури по ширині(Ox) вліво 
        COORD_X = COORD_X-DELTA_STEP
    if keys[pygame.K_RIGHT] and COORD_X < CURRENT_W - WIDTH_RECTANGLE:  #дозволений рух фігури по ширині(Ox) вправо
        COORD_X = COORD_X+DELTA_STEP
    if keys[pygame.K_UP] and COORD_Y >0: #дозволений рух фігури по висоті(Oy) вверх
        COORD_Y = COORD_Y-DELTA_STEP
    if keys[pygame.K_DOWN] and COORD_Y < CURRENT_H - HEIGHT_RECTANGLE: #дозволений рух фігури по висоті(Oy) вниз
        COORD_Y = COORD_Y+DELTA_STEP


    gameDisplay.fill(BLACK_COLOR) 

    pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X, 
                                              COORD_Y, 
                                              WIDTH_RECTANGLE, 
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)
    

