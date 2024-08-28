import gamelib
import tetrisC
import dibujar



ESPERAR_DESCENDER = 20

def main():

    # Inicializar el estsado del juego
    gamelib.resize(360, 400)
    juego = tetrisC.crear_juego(tetrisC.generar_pieza())
    pieza_sig = tetrisC.generar_pieza()
    cambiar_pieza = False
     
    timer = 0

    consolidados=[]

    while gamelib.loop(fps=30):
        
        # Dibujar la pantalla con el estado del juego
        gamelib.draw_begin()

        dibujar.DrawGrill(juego)
        dibujar.pieza(tetrisC.pieza_actual(juego))
        dibujar.drawPTS(juego)
        
        gamelib.draw_end()
       

        for event in gamelib.get_events():
            # Actualizar el estado del juego segun corresponda
            if event.type == gamelib.EventType.KeyPress and event.key=='q':
                 return
            if event.type == gamelib.EventType.KeyPress and event.key == 'a':
                juego = tetrisC.mover(juego, tetrisC.IZQUIERDA)
            
            if event.type == gamelib.EventType.KeyPress and event.key == 'd':
                juego = tetrisC.mover(juego, tetrisC.DERECHA)
            
            if event.type == gamelib.EventType.KeyPress and event.key == 's':
                juego, cambiar_pieza = tetrisC.avanzar(juego, pieza_sig)
                if cambiar_pieza:
                    pieza_sig = tetrisC.generar_pieza()
            if event.type == gamelib.EventType.KeyPress and event.key == 'l':
                juego, cambiar_pieza = tetrisC.RotPiece(juego)
        

            

                    #gamelib.draw_rectangle()
        # Descenso de la pieza automatica
        timer += 1
        if timer == ESPERAR_DESCENDER:
            juego, cambiar_pieza = tetrisC.avanzar(juego, pieza_sig)
            timer = 0

        if cambiar_pieza:
                    pieza_sig = tetrisC.generar_pieza()


gamelib.init(main)

"""

espera=20
#screen = pygame.display.set_mode((1280, 720))


def main():  
    #inicializa el estado del juego
    # 
    #  
    gamelib.resize(180,360)

    juego = tetrisCC.crear_juego(tetrisC.generar_pieza())
    pieza_sig=tetrisC.generar_pieza()
    change=False
    tick=0

    while gamelib.loop(60):
      #dibujar pantalla con estado del juego
        
        gamelib.draw_begin()
        
        
        dibujar.DrawGrill(ANCHO=tetrisC.ANCHO_JUEGO, ALTO=tetrisC.ALTO_JUEGO, TAMAÑO=dibujar.TAMAÑO)
        
        dibujar.pieza(tetrisC.pieza_actual(juego), 20, 400)
        
        gamelib.draw_end()

        for event in gamelib.get_events():
#            if event.type==gamelib.EventType.KeyPress and:
        
            if event.type == gamelib.EventType.KeyPress and event.key == 'q':
            
                return   
            
            if event.type == gamelib.EventType.KeyPress and event.key == 'a':
            
                juego=tetrisC.mover(juego, tetrisC.IZQUIERDA)   
            
            if event.type == gamelib.EventType.KeyPress and event.key == 'd':
            
                juego=tetrisC.mover(juego, tetrisC.DERECHA)   
            
            if event.type == gamelib.EventType.KeyPress and event.key == 's':
            
                juego, change=tetrisC.avanzar(juego, pieza_sig)


            #Descenso de la pieza automatica
        tick+=1
        if tick == espera:
            tetrisC.avanzar(juego, pieza_sig)
            tick=0
        if change:  
    
            pieza_sig=tetrisC.generar_pieza()

gamelib.init(main)"""
"""
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()


dimensiones=list(pygame.display.get_window_size())


x_org=dimensiones[0]//3
y_org=dimensiones[1]//3
"""
"""
print(f"Origen x: {x_org}")


print(f"Origen y: {y_org}")
running=True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        screen.fill("black")
""""""
def main():
    gamelib.resize(300, 300)

    while gamelib.loop(fps=1):
        for event in gamelib.get_events():
            if event.type==gamelib.EventType.KeyPress and event.key=="q":
                juego=tetrisC.mover(juego)
            
        pieza_cubo=tetrisC.generar_pieza()

        gamelib.draw_begin()

        dibujar.dibujar_pieza(pieza_cubo)

        gamelib.draw_end()

gamelib.init(main)"""


#def main():
#    x_org=
#    y_org=


 
#gamelib.init(draw_grill(ANCHO,ALTO, TAMAÑO))
