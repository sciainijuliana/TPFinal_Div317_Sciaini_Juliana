import pygame as pg
import Modulos.Forms.form_menu as form_menu
import Modulos.variables as var
import Modulos.Forms.form_ranking as form_ranking
import Modulos.Forms.form_options as form_options
import Modulos.Forms.form_tutorial as form_tutorial
import Modulos.Forms.form_pause as form_pause
import Modulos.Forms.form_eleccion as form_eleccion
import Modulos.Forms.form_stage as form_stage
import Modulos.Forms.form_victoria as form_victoria
import Modulos.Forms.form_derrota as form_derrota
import Modulos.Forms.form_wish as form_wish




def create_form_controller (screen: pg.Surface, datos_juego: dict):
    """
    Crea y configura el controlador principal de formularios del juego

    El controlador mantiene la pantalla principal, el estado del juego, el jugador,
    la configuración de música y la lista de formularios disponibles

    Recibe: screen: Superficie principal donde se dibujan los formularios / datos_juego: Diccionario con datos iniciales del juego. 

    Retorna: Diccionario que representa el controlador de formularios
    """
    controller = {}

    controller["main_screen"] = screen
    controller["game_started"] = False
    controller["player"] = datos_juego.get("player")
    controller["music_config"] = datos_juego.get("music_config")
    controller["mazos_dict"] = var.MAZOS_DICT

    controller["forms_list"] = [
        form_menu.crear_form_menu(
            {
                "name": "form_menu",
                "screen": controller.get("main_screen"),
                "active": True,
                "coord": (0, 0),
                "music_path": var.MUSICA_INICIO,
                "background": var.BACKGROUND_INICIO,
                "screen_dimentions": var.DIMENSION_PANTALLA,
                "music_config": controller.get("music_config"),
                "mazos_dict": controller["mazos_dict"],
                "ruta_mazo": var.MAZO_ELEGIDO,
                "jugador": controller.get("player")
            }
        ),
        form_ranking.create_form_ranking(
            {
                "name": "form_ranking",
                "screen": controller.get("main_screen"),
                "active": False,
                "coord": (0,0),
                "music_path": var.MUSICA_RANKING,
                "background": var.BACKGROUND_RANKING,
                "screen_dimentions": var.DIMENSION_PANTALLA,
                "music_config": controller.get("music_config"),
                "mazos_dict": controller["mazos_dict"],
                "ruta_mazo": var.MAZO_ELEGIDO,
                "jugador": controller.get("player")
            }
        ),
        form_options.create_form_options(
            {
                "name": "form_options",
                "screen": controller.get("main_screen"),
                "active": False,
                "coord": (0,0),
                "music_path": var.MUSICA_PAUSA,
                "background": var.BACKGROUND_MENU,
                "screen_dimentions": var.DIMENSION_PANTALLA,
                "music_config": controller.get("music_config"),
                "mazos_dict": controller["mazos_dict"],
                "ruta_mazo": var.MAZO_ELEGIDO,
                "jugador": controller.get("player")
            }
        ),
        form_tutorial.create_form_tutorial(
            {
            "name": "form_tutorial",
            "screen": controller.get("main_screen"),
            "active": False,
            "coord": (0,0),
            "music_path": var.MUSICA_TUTORIAL,
            "backgrounds": var.CARRUSEL_TUTORIAL, 
            "background": var.CARRUSEL_TUTORIAL[0],
            "screen_dimentions": var.DIMENSION_PANTALLA,
            "music_config": controller.get("music_config"),
            "mazos_dict": controller["mazos_dict"],
            "ruta_mazo": var.MAZO_ELEGIDO,
            "jugador": controller.get("player")
            }
        ),
        form_pause.create_form_pause(
            {
            "name": "form_pause",
            "screen": controller.get("main_screen"),
            "active": False,
            "coord": (0,0),
            "music_path": var.MUSICA_PAUSA,
            "background": var.BACKGROUND_PAUSA,
            "screen_dimentions": var.DIMENSION_PANTALLA,
            "music_config": controller.get("music_config"),
            "mazos_dict": controller["mazos_dict"],
            "ruta_mazo": var.MAZO_ELEGIDO,
            "jugador": controller.get("player")
            }
        ),
        form_stage.create_form_stage(
            {
            "name": "form_stage",
            "screen": controller.get("main_screen"),
            "active": False,
            "coord": (0,0),
            "music_path": var.MUSICA_PELEA,
            "background": var.BACKGROUND_PELEA,
            "screen_dimentions": var.DIMENSION_PANTALLA,
            "music_config": controller.get("music_config"),
            "mazos_dict": controller["mazos_dict"],
            "ruta_mazo": var.MAZO_ELEGIDO,
            "jugador": controller.get("player")
            }
        ),
        form_eleccion.create_form_eleccion({
            "name": "form_eleccion",
            "screen": controller.get("main_screen"),
            "active": False,
            "coord": (0,0),
            "music_path": var.MUSICA_ELECCION,
            "background": var.BACKGROUND_ELECCION,
            "screen_dimentions": var.DIMENSION_PANTALLA,
            "music_config": controller.get("music_config"),
            "mazos_dict": controller["mazos_dict"],
            "ruta_mazo": var.MAZO_ELEGIDO,
            "jugador": controller.get("player")
            }
        ),
        form_victoria.create_form_victoria({
            "name": "form_victoria",
            "screen": controller.get("main_screen"),
            "active": False,
            "coord": (0,0),
            "music_path": var.MUSICA_VICTORIA,
            "background": var.BACKGROUND_VICTORIA,
            "screen_dimentions": var.DIMENSION_PANTALLA,
            "music_config": controller.get("music_config"),
            "mazos_dict": controller["mazos_dict"],
            "ruta_mazo": var.MAZO_ELEGIDO,
            "jugador": controller.get("player")
            }
        ),
        form_derrota.create_form_derrota({
            "name": "form_derrota",
            "screen": controller.get("main_screen"),
            "active": False,
            "coord": (0,0),
            "music_path": var.MUSICA_DERROTA,
            "background": var.BACKGROUND_DERROTA,
            "screen_dimentions": var.DIMENSION_PANTALLA,
            "music_config": controller.get("music_config"),
            "mazos_dict": controller["mazos_dict"],
            "ruta_mazo": var.MAZO_ELEGIDO,
            "jugador": controller.get("player")
            }
        ),
        form_wish.crear_form_wish({
            "name": "form_wish",
            "screen": controller.get("main_screen"),
            "active": False,
            "coord": (0,0),
            "music_path": var.MUSICA_DESEOS,
            "background": var.BACKGROUND_DESEOS,
            "screen_dimentions": var.DIMENSION_PANTALLA,
            "music_config": controller.get("music_config"),
            "mazos_dict": controller["mazos_dict"],
            "ruta_mazo": var.MAZO_ELEGIDO,
            "jugador": controller.get("player")
        })
    ]

    return controller

def forms_update (form_controller: dict, eventos: list[pg.event.Event]):
    """
    Actualiza y dibuja el formulario que se encuentra activo, ejecuta la lógica de actualización y dibujo de cada form

    Recibe: form_controller: Diccionario del controlador de formularios / Lista de eventos de Pygame que pueden afectar a los formularios.
    """

    lista_formularios = form_controller.get("forms_list")
    events = eventos

    for form in lista_formularios:
        if form.get("active"):
            match form.get("name"):
                case "form_menu":
                    formulario_menu = lista_formularios[0]
                    form_menu.update(formulario_menu)
                    form_menu.draw(formulario_menu)
                case "form_ranking":
                    formulario_ranking = lista_formularios[1]
                    form_ranking.update(formulario_ranking)
                    form_ranking.draw(formulario_ranking)
                case "form_options":
                    formulario_opciones = lista_formularios[2]
                    form_options.update(formulario_opciones)
                    form_options.draw(formulario_opciones)
                case "form_tutorial":
                    formulario_tutorial = lista_formularios[3]
                    form_tutorial.update(formulario_tutorial)
                    form_tutorial.draw(formulario_tutorial)
                case "form_pause":
                    formulario_pausa = lista_formularios[4]
                    form_pause.update(formulario_pausa)
                    form_pause.draw(formulario_pausa)
                case "form_stage":
                    formulario_stage = lista_formularios[5]
                    form_stage.update(formulario_stage)
                    form_stage.draw(formulario_stage)
                case "form_eleccion":
                    formulario_eleccion = lista_formularios[6]
                    form_eleccion.update(formulario_eleccion)
                    form_eleccion.draw(formulario_eleccion)
                case "form_victoria":
                    formulario_victoria = lista_formularios[7]
                    form_victoria.update(formulario_victoria, events)
                    form_victoria.draw(formulario_victoria)
                case "form_derrota":
                    formulario_derrota = lista_formularios[8]
                    form_victoria.update(formulario_derrota, events)
                    form_victoria.draw(formulario_derrota)
                case "form_wish":
                    formulario_deseo = lista_formularios[9]
                    form_wish.update(formulario_deseo)
                    form_wish.draw(formulario_deseo)

    

def update(form_controller: dict, eventos: list[pg.event.Event]):
    """
    Llama a forms_update para refrescar el estado y dibujar el formulario activo

    Recibe: form_controller: Diccionario del controlador de formularios / eventos: Lista de eventos de Pygame que pueden afectar a los formularios
    """
    forms_update(form_controller, eventos)