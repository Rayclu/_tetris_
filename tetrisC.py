from random import randint
from random import randrange
import gamelib
ANCHO_JUEGO, ALTO_JUEGO = 9, 18
IZQUIERDA, DERECHA = -1, 1
CUBO = 0
Z = 1
S = 2
I = 3
L = 4
L_INV = 5
T = 6

PIEZAS = (
    ((0, 0), (1, 0), (0, 1), (1, 1)), # Cubo queda igual 
    ((0, 0), (1, 0), (1, 1), (2, 1)), # Z (zig-zag)
    ((0, 0), (0, 1), (1, 1), (1, 2)), # S (-Z)
    ((0, 0), (0, 1), (0, 2), (0, 3)), # I (línea) le cambio los ejes
    ((0, 0), (0, 1), (0, 2), (1, 2)), # L
    ((0, 0), (1, 0), (2, 0), (2, 1)), # -L
    ((0, 0), (1, 0), (2, 0), (1, 1)), # T 

)


def generar_pieza(pieza=None):
    """
    Genera una nueva pieza de entre PIEZAS al azar. Si se especifica el parámetro pieza
    se generará una pieza del tipo indicado. Los tipos de pieza posibles
    están dados por las constantes CUBO, Z, S, I, L, L_INV, T.

    El valor retornado es una tupla donde cada elemento es una posición
    ocupada por la pieza, ubicada en (0, 0). Por ejemplo, para la pieza
    I se devolverá: ( (0, 0), (0, 1), (0, 2), (0, 3) ), indicando que 
    ocupa las posiciones (x = 0, y = 0), (x = 0, y = 1), ..., etc.
    """
    """if pieza is None:
        return PIEZAS[randint(0, 6)]
    return PIEZAS[pieza]"""
    
    if pieza == None:
        pieza = PIEZAS[randrange(0,len(PIEZAS))]
        return pieza
    
    pieza = PIEZAS[pieza]
    return pieza

    
def trasladar_pieza(pieza, dx, dy):
    """
    Traslada la pieza de su posición actual a (posicion + (dx, dy)).

    La pieza está representada como una tupla de posiciones ocupadas,
    donde cada posición ocupada es una tupla (x, y). 
    Por ejemplo para la pieza ( (0, 0), (0, 1), (0, 2), (0, 3) ) y
    el desplazamiento dx=2, dy=3 se devolverá la pieza 
    ( (2, 3), (2, 4), (2, 5), (2, 6) ).
    """

    """pieza = list(pieza)

    for i in range(len(pieza)):
        pieza[i] = (pieza[i][0] + dx, pieza[i][1] + dy)

    return tuple(pieza)
    """
    
    #((0, 0), (1, 0), (0, 1), (1, 1))

    pieza = list(pieza)

    #[(0, 0), (1, 0), (0, 1), (1, 1)]


    for i in range(len(pieza)):
        pieza[i] = (pieza[i][0] + dx, pieza[i][1] + dy)

    return (pieza)

    #pieza = piezatrasladada
    
def crear_juego(pieza_inicial):
    """
    Crea un nuevo juego de Tetris.

    El parámetro pieza_inicial es una pieza obtenida mediante 
    generar_pieza(). Ver documentación de esa función para más información.

    El juego creado debe cumplir con lo siguiente:
    - La grilla está vacía: hay_superficie da False para todas las ubicaciones
    - La pieza actual está arriba de todo, en el centro de la pantalla.
    - El juego no está terminado: terminado(juego) da False

    Que la pieza actual esté arriba de todo significa que la coordenada Y de 
    sus posiciones superiores es 0 (cero).
    """
    """grilla = []
    
    for i in range(ALTO_JUEGO):
        fila=[]
        for j in range(ANCHO_JUEGO):
            fila.append(0)
        grilla.append(fila)
    
            
    pieza_inicial = trasladar_pieza(pieza_inicial, ANCHO_JUEGO // 2, 0)
    return grilla, pieza_inicial"""
    pieza_inicial = trasladar_pieza(pieza_inicial, ANCHO_JUEGO // 2, 0) 
    grilla = []
    pts=0
    for _ in range(ALTO_JUEGO):
        fila=[]
        for i in range(ANCHO_JUEGO):
            fila.append(0)  
        grilla.append(fila)

    juego = (grilla, pieza_inicial, pts)
    
    return juego

def dimensiones(juego):
    """grilla = juego[0]
    return len(grilla[0]), len(grilla)"""
    grilla = juego[0]

    return len(grilla[0]), len(grilla)


def pieza_actual(juego):
    """
    Devuelve una tupla de tuplas (x, y) con todas las posiciones de la
    grilla ocupadas por la pieza actual.

    Se entiende por pieza actual a la pieza que está cayendo y todavía no
    fue consolidada con la superficie.

    La coordenada (0, 0) se refiere a la posición que está en la esquina 
    superior izquierda de la grilla.
    """ 
    "return juego[1]"
    pieza_actual = juego[1]

    return pieza_actual


def hay_superficie(juego, x, y):
    """
    Devuelve True si la celda (x, y) está ocupada por la superficie consolidada.
    
    La coordenada (0, 0) se refiere a la posición que está en la esquina 
    superior izquierda de la grilla.
    """
    #funcional, uso de ejemplo
    grilla = juego[0]
    if grilla[y][x]!=0:
        return True
    return False        
    
    #corrección
    """
    grilla = juego[0]

    celda = (x,y)

    if grilla[x][y]!=0:
                return True
    return False
    """"""
    #queda a desorrollo, pero va encaminado
    grilla=juego[0]
    coor= [x] and [y]
    if grilla[coor]!=0:
        return True
    return False"""
    
def mover(juego, direccion):
    
    """
    Mueve la pieza actual hacia la derecha o izquierda, si es posible.
    Devuelve un nuevo estado de juego con la pieza movida o el mismo estado 
    recibido si el movimiento no se puede realizar.

    El parámetro direccion debe ser una de las constantes DERECHA o IZQUIERDA.
   """

    pieza_aux = pieza_actual(juego)
    pieza_aux = trasladar_pieza(pieza_aux, direccion, 0)
    
    for i in range(0, len(pieza_aux)):
        if  not(-1 < pieza_aux[i][0] < ANCHO_JUEGO) or hay_superficie(juego, pieza_aux[i][0], pieza_aux[i][1]):
            return juego
    
    return juego[0], pieza_aux
    """pieza_actual = juego[1]

    pieza_aux = trasladar_pieza(pieza_actual, juego, direccion)
    #juego[1]
    

    for i in range(0,len(pieza_actual)):
        pieza_aux[i] = pieza_aux[0]+direccion

        if not (pieza_aux[i]+direccion > ANCHO_JUEGO) or (pieza_aux[i]+direccion < ANCHO_JUEGO):
            return juego

    for m in range(0,len(pieza_actual)):

        if pieza_actual[3][0] > ANCHO_JUEGO:
            return pieza_actual
        
        pieza_actual[m] = (pieza_actual[m][0]+direccion,pieza_actual[m][1])

    juego[1] = pieza_actual
    return pieza_actual

    pieza = trasladar_pieza(pieza_actual(juego))"""
    return "???"

#def consolidar_pieza(juego):

    pieza = juego[1]

 #   for i in range(len(pieza)):

        



    #  if pieza[0][1] == 

    
    

#def eliminar_fila():


#def cambiar_pieza():





def consolidar_pieza(juego):

    grilla=juego[0]

    for i in range(len(pieza_actual(juego))):
        coor=pieza_actual(juego)[i]
        grilla[coor[1]][coor[0]] = 1
    return grilla, pieza_actual(juego)
    
def eliminar_fila(juego):
    grilla=juego[0]
    
    puntos = juego[2]
    cortar = 0

    for i in range(len(grilla)):
        fila=grilla[i]
        
        if fila.count(1)==ANCHO_JUEGO:
            grilla.pop(i)
            contar += 1
            
            fila_nueva=[]
            for _ in range(ANCHO_JUEGO):
                fila_nueva.append(0)

            grilla.insert(0, fila_nueva)

    puntos += cortar * 200
    return juego, puntos  

def cambiar_pieza_actual(juego, pieza):
    return juego[0], trasladar_pieza(pieza, ANCHO_JUEGO//2, 0)

def avanzar(juego, siguiente_pieza):
    """
    Avanza al siguiente estado de juego a partir del estado actual.
    
    Devuelve una tupla (juego_nuevo, cambiar_pieza) donde el primer valor
    es el nuevo estado del juego y el segundo valor es un booleano que indica
    si se debe cambiar la siguiente_pieza (es decir, se consolidó la pieza
    actual con la superficie).
    
    Avanzar el estado del juego significa:
     - Descender una posición la pieza actual.
     - Si al descender la pieza no colisiona con la superficie, simplemente
       devolver el nuevo juego con la pieza en la nueva ubicación.
     - En caso contrario, se debe
       - Consolidar la pieza actual con la superficie.
       - Eliminar las líneas que se hayan completado.
       - Cambiar la pieza actual por siguiente_pieza.

    Si se debe agregar una nueva pieza, se utilizará la pieza indicada en
    el parámetro siguiente_pieza. El valor del parámetro es una pieza obtenida 
    llamando a generar_pieza().

    **NOTA:** Hay una simplificación respecto del Tetris real a tener en
    consideración en esta función: la próxima pieza a agregar debe entrar 
    completamente en la grilla para poder seguir jugando, si al intentar 
    incorporar la nueva pieza arriba de todo en el medio de la grilla se
    pisara la superficie, se considerará que el juego está terminado.

    Si el juego está terminado (no se pueden agregar más piezas), la funcion no hace nada, 
    se debe devolver el mismo juego que se recibió.
    """

    if terminado(juego):
        return juego, False
    
    #desciende la pieza actual en una posicion
    pieza=trasladar_pieza(pieza_actual(juego), 0, 1)
    
    for i in range(len(pieza)):
        coor=pieza[i]
        if coor[1]>= ALTO_JUEGO or hay_superficie(juego, coor[0], coor[1]):
            #   - Consolidar la pieza actual con la superficie.
            juego = consolidar_pieza(juego)
            #- Eliminar las líneas que se hayan completado.
            juego=eliminar_fila(juego)
            #- Cambiar la pieza actual por siguiente_pieza.
            juego=cambiar_pieza_actual(juego, siguiente_pieza)

            return juego, True
    
    juego = juego[0], pieza
    return juego, False
 
def terminado(juego):

    """
    Devuelve True si el juego terminó, es decir no se pueden agregar
    nuevas piezas, o False si se puede seguir jugando.
    """
    for i in range(len(pieza_actual(juego))):
        coordenada=pieza_actual(juego)[i]

        if hay_superficie(juego, coordenada[0], coordenada[1]):
            return True
    return False


def RotPiece(juego, direeccion):
    "juego[1]=pieza_actual(juego)=pieza_actual(juego+90°)"
    
    pieza=list(juego[1])

    
    
    
    return juego[1]
    


def GDownPiece(juego):
    
    tick=0

    
    while gamelib.loop(fps=30):
        tick+=1

        if tick==20:
            juego[1] = trasladar_pieza((pieza_actual()), 0, -1)


            tick=0  

            return juego[0], juego[1]

def main():
    pass