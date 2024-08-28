
# Example file showing a basic pygame "game loop"
import pygame
import tetrisC
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

#Calculate the sizes of screen for center the rect
screen_sizes=list(pygame.display.get_window_size())

location_x=screen_sizes[0]//2
location_y=screen_sizes[1]//2

div=screen_sizes[0]/3



#Create coord of lines, the coords is origin and final that line

coords=["[start_pos(x,y), end_pos(x+1, y+1)]"]
eje_x=[]
eje_y=[]
for x in range(ANCHO_JUEGO+1):
    eje_x.append(x)

for y in range(ALTO_JUEGO+1):
    eje_y.append(y)

print(eje_y)
print("--------------------------------------------")
print(eje_x)
#coord=[ANCHO_JUEGO[x], ALTO_JUEGO[y]]

# Crear las coordenadas de las líneas en función del rectángulo
rect_width = ANCHO_JUEGO * 20  # Ajustar el ancho del rectángulo a una escala deseada
rect_height = ALTO_JUEGO * 15  # Ajustar la altura del rectángulo a una escala deseada


tamaño=20

#distancia entre cada linea
#sizes_rect=list(ANCHO_JUEGO, ALTO_JUEGO)
#sizes_rect_y=sizes_rect*
#x, y=pygame.display.get_window_size()
"""
running = True

while running:
# poll for events
# pygame.QUIT event means the user clicked X to close your window
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

# fill the screen with a color to wipe away anything from last frame
screen.fill("black")
    
# RENDER YOUR GAME HERE
pygame.draw.line(screen, "white", (div, screen_sizes[1]), (div, -screen_sizes[1]))
pygame.draw.line(screen, "white", (2*div, screen_sizes[1]), (2*div, -screen_sizes[1]))

#rect=pygame.draw.rect(screen, "red", (location_x/2, location_y/2, ANCHO_JUEGO*20, ALTO_JUEGO*20))


#L invert

pygame.draw.rect(screen, "red", (location_x-20, location_y, 20, 20))
pygame.draw.rect(screen, "red", (location_x-5, location_y, 20, 20))
pygame.draw.rect(screen, "red", (location_x-5, location_y-20, 20, 20))
pygame.draw.rect(screen, "red", (location_x-5, location_y-40, 20, 20))

pygame.draw.rect(screen, "red", (location_x*(1.5)-5, location_y, 20, 20))
pygame.draw.rect(screen, "red", (location_x*(1.5)-25, location_y, 20, 20))
pygame.draw.rect(screen, "red", (location_x*(1.5)-15, location_y, 20, 20))
pygame.draw.rect(screen, "red", (location_x*(1.5)-5, location_y-20, 20, 20))"""

#draw lines of the grill
"""margenS=pygame.draw.line(screen, "red", (location_x-10, location_y-100), (location_x-10 + rect_width, location_y-100),3)
margenLI=pygame.draw.line(screen, "red", (location_x-10, location_y-100), (location_x-10, location_y+rect_height),3)
margenI=pygame.draw.line(screen, "red", (location_x-10, location_y+260), (location_x-10 + rect_width, location_y+260),3)
"""
# flip() the display to put your work on screen
pygame.display.flip()

clock.tick(60)  # limits FPS to 60

pygame.quit()

def print_piece(pieza):

    pygame.init()

    screen = pygame.display.set_mode((1280, 720))

    clock = pygame.time.Clock()

    screen_sizes=list(pygame.display.get_window_size())

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        screen.fill("black")

        for x,y in tetrisC.pieza:
            pygame.draw.rect(screen, "red", ( ))