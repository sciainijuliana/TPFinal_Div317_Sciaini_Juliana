import pygame as pg
import Modulos.variables as var
import sys
import Modulos.Forms.form_controller as form_controller
import Modulos.auxiliares as aux
import participante as part
import Modulos.stage as stage


def dbzgame ():
    pg.init()
    
    pg.display.set_caption(var.TITULO_JUEGO)
    pantalla_juego = pg.display.set_mode(var.DIMENSION_PANTALLA)
    limite_fps = pg.time.Clock()
    

    corriendo = True

    datos_juego = {
        "puntaje" : 0,
        "vida_base" : var.VIDA_DEFAULT,
        "player" : part.inicializar_participante(pantalla_juego, "Player", (0,0), (0,0)),
        "music_config": {
            "music_on": True,
            "volumen_musica" : var.VOLUMEN_INICIAL,
            "music_init": False
        }
    }
    
    var.MAZOS_DICT = aux.generar_bd_cartas(var.DECKS)

    form_control = form_controller.create_form_controller(pantalla_juego, datos_juego)

    while corriendo:
        eventos = pg.event.get()
        for evento in eventos:
            if evento.type == pg.QUIT:
                corriendo = False

        form_controller.update(form_control, eventos)
        pg.display.flip()
    pg.quit()
    sys.exit()


    