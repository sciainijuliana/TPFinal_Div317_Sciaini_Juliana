import Modulos.Forms.form_base as form_base
from utn_fra.pygame_widgets import Label, Button, ButtonImageSound
from utn_fra.pygame_widgets.label_image import ImageLabel
import Modulos.variables as var
import pygame as pg
import Modulos.stage as stage_juego
import Modulos.auxiliares as aux
import participante as part
import Modulos.Forms.form_options as opt
import random as rd

def create_form_stage (form_dict_data: dict) -> dict:
    """
    Crea y configura el formulario de stage donde se desarrolla el juego

    Recibe: form_dict_data: Diccionario con la configuración inicial del formulario

    Retorna: Diccionario que representa el formulario de stage con todos sus widgets
    """
    form = form_base.create_base_form(form_dict_data)

    form["stage"] = None

    form["stage_restart"] = False
    form["times_up"] = False
    form["stage_timer"] = var.STAGE_TIMER
    form["last_timer_check"] = pg.time.get_ticks()

    form["jugador"] = form_dict_data.get("jugador")

    form["wish_disponible"] = True
    form["shield_disponible"] = True

    form["stage"] = None
    form["clock"] = pg.time.Clock()

    form["label_timer_text"] = Label(x=50, y=20, text= "TIMER", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=20, color=(254, 215, 0))
    form["label_timer"] = Label(x=50, y=50, text= (f"{form.get("stage_timer")}"), screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=20, color=(254, 215, 0))
    form["label_score_text"] = Label(x=950, y=20, text= "SCORE", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=20, color=(254, 215, 0))    
    form["label_score"] = Label(x=950, y=50, text= "0", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=20, color=(254, 215, 0))
    
    form["label_HP_jugador"] = Label(x=200, y=370, text= f"HP:", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=20, color=(254, 0, 0))
    form["label_ATK_jugador"] = Label(x=200, y=390, text= f"ATK:", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=20, color=(254, 0, 0))
    form["label_DEF_jugador"] = Label(x=200, y=410, text= f"DEF:", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=20, color=(254, 0, 0))

    form["label_HP_enemigo"] = Label(x=800, y=370, text= f"HP:", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=20, color=(254, 0, 0))
    form["label_ATK_enemigo"] = Label(x=800, y=390, text= f"ATK:", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=20, color=(254, 0, 0))
    form["label_DEF_enemigo"] = Label(x=800, y=410, text= f"DEF:", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=20, color=(254, 0, 0))

    form["button_shield"] = ButtonImageSound(x=200, y=310, text="",width=90, height=90, screen=form.get("screen"), image_path=var.ICON_SHIELD, sound_path=var.SONIDO_SHIELD, font_size=40, on_click=activar_escudo, on_click_param=form)
    form["button_wish"] = ButtonImageSound(x=130, y=310, text="",width=90, height=90, screen=form.get("screen"), image_path=var.ICON_STAR, sound_path=var.SONIDO_DESEO_IN, font_size=40, on_click=aux.activar_form_a_cambiar, on_click_param="form_wish")
    form["button_jugar"] = ButtonImageSound(x=500, y=760,width=80, height=80, text= "", screen=form_dict_data.get("screen"), image_path=var.ICON_BOLA, sound_path=var.SONIDO_GOLPE, font_size=20, on_click=jugar_mano, on_click_param=form)
    form["button_pausa"] = Button(x=500, y=50, text= "PAUSA", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=20, color=(254, 215, 0), on_click=aux.activar_form_a_cambiar, on_click_param="form_pause")
    
    form["widgets_list"] = [
        form.get("button_pausa"), form.get("label_score_text"), 
        form.get("label_timer_text"), form.get("label_timer"), 
        form.get("label_score"), form.get("button_jugar"),
        form.get("label_HP_jugador"),form.get("label_HP_enemigo"),
        form.get("label_ATK_jugador"), form.get("label_ATK_enemigo"),
        form.get("label_DEF_jugador"), form.get("label_DEF_enemigo")]
    
    form["bonus_widget_list"] = [form.get("button_wish"), form.get("button_shield")]

    var.dict_forms_status[form.get("name")] = form

    return form

def activar_escudo(form_dict_data: dict):
    """
    Activa el escudo del jugador y lo marca como usado.

    Recibe: form_dict_data: Diccionario del formulario de stage
    """
    stage = form_dict_data.get("stage")
    
    jugador = stage.get("jugador")
    
    part.activar_bonus_shield(jugador)
    
    form_dict_data["shield_disponible"] = False

def jugar_mano (stage_data: dict):
    """
    Ejecuta una mano de combate en el stage
    - Si el juego no terminó, se juega un turno.
    - Si el juego ya terminó, se marca el stage para reinicio.

    Recibe: stage_data: Diccionario con los datos del stage
    """
    if not stage_juego.get_estado_juego(stage_data):
        ganador = stage_juego.jugar_turno(stage_data)
    else:
        stage_data["stage_restart"] = True
        
def timer_update (form_dict_data: dict):
    """
    Actualiza el temporizador del stage cada segundo.

    Recibe: form_dict_data: Diccionario del formulario de stage
    """
    tiempo_inicial = form_dict_data.get("stage_timer")
    if tiempo_inicial > 0:
        tiempo_actual = pg.time.get_ticks()
        if tiempo_actual - form_dict_data.get("last_timer_check") > 1000:
            form_dict_data["stage_timer"] -= 1
            form_dict_data["last_timer_check"] = tiempo_actual
            form_dict_data["label_timer"].update_text(f"{form_dict_data['stage_timer']}", color=(254, 215, 0))

def update_wish_widget (form_dict_data: dict):
    """
    Actualiza el widget del wish si está disponible

    Recibe: form_dict_data: Diccionario del formulario de stage
    """

    wish_disponible = form_dict_data.get("wish_disponible")
    if wish_disponible:
            form_dict_data["bonus_widget_list"][0].update()


def draw_wish_widget (form_dict_data: dict):
    """
    Dibuja el widget del wish si está disponible

    Recibe: form_dict_data: Diccionario del formulario de stage
    """

    wish_disponible = form_dict_data.get("wish_disponible")
    if wish_disponible:
            form_dict_data["bonus_widget_list"][0].draw()

def update_shield_widget(form_dict_data: dict):
    """
    Actualiza el widget del shield si está disponible

    Recibe: form_dict_data: Diccionario del formulario de stage
    """
    shield_disponible = form_dict_data.get("shield_disponible")
    if shield_disponible:
        form_dict_data["bonus_widget_list"][1].update()


def draw_shield_widget(form_dict_data: dict):
    """
    Dibuja el widget del shield si está disponible

    Recibe: form_dict_data: Diccionario del formulario de stage
    """
    shield_disponible = form_dict_data.get("shield_disponible")
    if shield_disponible:
        form_dict_data["bonus_widget_list"][1].draw()

def draw_indicador_escudo(form_dict_data: dict):
    """
    Dibuja un indicador visual cuando el escudo espejo está activo

    Recibe: form_dict_data: Diccionario del formulario de stage
    """
    stage = form_dict_data.get("stage")
    jugador = stage.get("jugador")
    screen = form_dict_data.get("screen")
    
    if part.get_estado_shield(jugador):
        label_escudo = ImageLabel(x=400, y=300, text="", screen=screen, image_path=var.ICON_SHIELD_ACTIVE, width= 100, height=200, font_path= var.FUENTE_PRINCIPAL, font_size=20, color=(254, 0, 0))
        label_escudo.draw()    

def draw_indicador_critico(form_dict_data: dict):
    """
    Dibuja un indicador visual cuando el último golpe fue crítico

    Recibe: form_dict_data: Diccionario del formulario de stage
    """
    stage = form_dict_data.get("stage")
    critico = stage.get("golpe_critico")
    screen = form_dict_data.get("screen")

    if critico:
        label_critico = ImageLabel(x=400, y=100, text="", screen=screen, image_path=var.ICON_CRITICAL, width= 300, height=200, font_path= var.FUENTE_PRINCIPAL, font_size=20, color=(254, 0, 0))
        label_critico.draw()


def update_score (form_dict_data: dict):
    """
    Actualiza la etiqueta de puntaje del jugador en el stage

    Recibe: form_dict_data: Diccionario del formulario de stage
    """
    participante = form_dict_data.get("stage").get("jugador")
    score = part.get_score_participante(participante)
    form_dict_data.get("label_score").update_text(text=f"{score}", color=(254, 215, 0))

def update_labels_participante (form_dict_data: dict, participante: str):
    """
    Actualiza las etiquetas de estadísticas (HP, ATK, DEF) de un participante

    Recibe: form_dict_data: Diccionario del formulario de stage / participante: Nombre del participante ("jugador" o "enemigo")
    """
    dict_participante = form_dict_data["stage"][participante]

    form_dict_data[f"label_HP_{participante}"].update_text(text=f"HP: {part.get_hp_participante(dict_participante)}", color=(254, 0, 0))
    form_dict_data[f"label_ATK_{participante}"].update_text(text=f"ATK: {part.get_ataque_participante(dict_participante)}", color=(254, 0, 0))
    form_dict_data[f"label_DEF_{participante}"].update_text(text=f"DEF: {part.get_defensa_participante(dict_participante)}", color=(254, 0, 0))

def update (form_dict_data: dict):
    """
    Actualiza el estado completo del formulario de stage
    - Inicializa el stage si aún no existe
    - Refresca widgets base, wish y shield
    - Actualiza estadísticas de jugador y enemigo
    - Actualiza puntaje y temporizador
    - Verifica estado del juego y cambia pantalla final si corresponde

    Recibe: form_dict_data: Diccionario del formulario de stage
    """
    if var.MAZO_ELEGIDO is not None and form_dict_data.get("stage") is None:
        form_dict_data["stage"] = stage_juego.inicializar_stage(form_dict_data["screen"], var.MAZOS_DICT, var.MAZO_ELEGIDO, var.JSON_CONFIGS, form_dict_data["jugador"])
        form_dict_data["label_timer"].update_text(f"{form_dict_data['stage_timer']}", color=(254, 215, 0))
        form_dict_data["button_jugar"].on_click_param = form_dict_data["stage"]

    form_base.update(form_dict_data)
    update_wish_widget(form_dict_data)
    update_shield_widget(form_dict_data)
    update_labels_participante(form_dict_data, "jugador")
    update_labels_participante(form_dict_data, "enemigo")
    update_score(form_dict_data)
    timer_update(form_dict_data)
    if stage_juego.get_estado_juego(form_dict_data.get("stage")):
        stage_juego.check_ganador(form_dict_data.get("stage"))
        stage_juego.cambiar_pantalla_final(form_dict_data.get("stage"))

def draw (form_dict_data: dict):
    """
    Dibuja el formulario de stage en la pantalla
    - Muestra indicadores de crítico y escudo si corresponden

    Recibe: form_dict_data: Diccionario del formulario de stage
    """
    form_base.draw(form_dict_data)
    draw_wish_widget(form_dict_data)
    draw_shield_widget(form_dict_data)
    form_base.dibujar_widgets(form_dict_data)
    if form_dict_data.get("stage"):
        stage_juego.draw_jugadores(form_dict_data["stage"])
        stage_juego.draw_cartas(form_dict_data["stage"])
        draw_indicador_critico(form_dict_data)
        draw_indicador_escudo(form_dict_data)