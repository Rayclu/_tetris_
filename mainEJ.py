import gamelib
import tetrisC
import dibujar


def main():
    gamelib.resize(300, 300)

    while gamelib.loop(fps=1):
        for event in gamelib.get_events():
            if event.type==gamelib.EventType.KeyPress and event.key=="q":
                return
            
        pieza_cubo=tetrisC.generar_pieza()

        gamelib.draw_begin()

        dibujar.dibujar_pieza(pieza_cubo)

        gamelib.draw_end()

gamelib.init(main)