import gamelib
import tetrisC

"""
X_ORIGEN = 0
Y_ORIGEN = 0
tamaño = 20
ANCHO=tetrisCC.ANCHO_JUEGO
ALTO=tetrisCC.ALTO_JUEGO
"""

X_ORIGEN = 110
Y_ORIGEN = 20
TAMAÑO = 15

def pieza(pieza, x = 0, y = 0):
    
    for x, y in pieza:
        gamelib.draw_rectangle(X_ORIGEN + x * TAMAÑO, Y_ORIGEN + y * TAMAÑO
                            , X_ORIGEN + x * TAMAÑO + TAMAÑO, Y_ORIGEN + y * TAMAÑO + TAMAÑO, fill = "red")

def DrawGrill(juego):
    
    for i in range (tetrisC.ANCHO_JUEGO):
        gamelib.draw_line(X_ORIGEN + i * TAMAÑO, Y_ORIGEN
                          , X_ORIGEN + i * TAMAÑO, Y_ORIGEN + TAMAÑO * tetrisC.ALTO_JUEGO)
       
    for i in range (tetrisC.ALTO_JUEGO):
        gamelib.draw_line(X_ORIGEN, Y_ORIGEN + i * TAMAÑO
                          , X_ORIGEN + TAMAÑO * tetrisC.ANCHO_JUEGO, Y_ORIGEN + i * TAMAÑO)

    for y in range(len(juego[0])):
        for x in range(len(juego[0][y])):
            if tetrisC.hay_superficie(juego, x, y):
                gamelib.draw_rectangle(X_ORIGEN + x * TAMAÑO, Y_ORIGEN + y * TAMAÑO
                            , X_ORIGEN + x * TAMAÑO + TAMAÑO, Y_ORIGEN + y * TAMAÑO + TAMAÑO, fill = "red")

def drawPTS(juego):
    """    
    Verifica si las linas completadas conforman un combo para determinar 
    una cantidad de puntos que luego se añadira al contador final.

    Entrada: 
        Eliminar_pieza(juego)
    Desarrollo:
        #1 linea==100
        #2 lineas==300
        #3 lineas==500
        #4 lineas>==1000
    Retorna:
        Puntos a sumar en el contador
     """
    #gamelib text format:text, x, y, font=None, size=12, bold=False, italic=False, **options
    pts=juego[1]
    gamelib.draw_text(f"La cantidad de puntos acutal es de {pts}",tetrisC.ANCHO_JUEGO,
                       Y_ORIGEN, font=None, bold=False, italic=True)

    

def CountPTS():

    """
    Verifica si las linas completadas conforman un combo para determinar 
    una cantidad de puntos que luego se añadira al contador final.

    Entrada: 
        Eliminar_pieza(juego)
    Desarrollo:
        #1 linea==100
        #2 lineas==300
        #3 lineas==500
        #4 lineas>==1000
    Retorna:
        Puntos a sumar en el contador 
    """
    """
    pts=0

    while 
    
    """
    pass
    
"""
def dibujar_pieza(pieza, x=0, y=0):
    
    for x, y in pieza:
        gamelib.draw_rectangle(X_ORIGEN-tamaño + x * tamaño, Y_ORIGEN + y * tamaño, X_ORIGEN-tamaño + x * tamaño + tamaño, Y_ORIGEN + y * tamaño + tamaño, fill = "red")

"""