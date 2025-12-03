import Modulos.Forms.form_base as form_base
from utn_fra.pygame_widgets import Label, Button,TextBox
import Modulos.variables as var
import pygame as pg
import Modulos.stage as stage_juego
import Modulos.auxiliares as aux
import participante as part

def create_form_victoria (form_dict_data: dict) -> dict:
    """
    Crea y configura el formulario de victoria del juego

    Recibe: form_dict_data: Diccionario con la configuración inicial del formulario

    Retorna: Diccionario que representa el formulario de victoria
    """
    form = form_base.create_base_form(form_dict_data)
    jugador = form_dict_data.get("jugador")
    form["jugador"] = jugador

    form["label_victoria"] = Label(x=500, y=500, text= "ERES EL GANADOR:", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=60, color=(254, 215, 0))
    form["label_score"] = Label(x=500, y=600, text= f"Tu score es:{part.get_score_participante(jugador)}", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(254, 215, 0))
    form["label_titulo"] = Label(x=500, y=620, text= "Ingresa tu nombre:", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(254, 215, 0))

    form["button_submit"] = Button(x=800, y=750, text= ">>", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=50, color=(254, 215, 0), on_click=subir_nombre, on_click_param=form)

    form["text_box"] = TextBox(x=400, y=700, text= "", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=20, color=(0, 0, 0))
    form["text_box"].selected = True
    form["label_input"] = Label(x=500, y=700, text= "", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(0, 0, 0))

    form["widgets_list"] = [form.get("text_box"), form.get("label_victoria"), form.get("label_titulo"), form.get("label_score"), form.get("label_input"), form.get("button_submit")]

    var.dict_forms_status[form.get("name")] = form

    return form

def subir_nombre (form_dict_data: dict):
    """
    Registra el nombre del jugador en el ranking tras la victoria

    Recibe: form_dict_data: Diccionario del formulario de victoria
    """
    jugador = form_dict_data.get("jugador")
    nombre_jugador = form_dict_data.get("text_box").writing
    part.set_nombre_participante(jugador, nombre_jugador)

    data_to_csv = aux.info_to_csv(jugador)
    aux.guardar_info_csv(var.RANKING, data_to_csv)

    form_base.set_active("form_ranking")

def update (form_dict_data: dict, eventos: list[pg.event.Event]):
    """
    Actualiza el estado del formulario de victoria

    Recibe: form_dict_data: Diccionario del formulario de victoria / eventos: Lista de eventos de Pygame que pueden afectar a los widgets
    """
    jugador = form_dict_data.get("jugador")
    score_actual = part.get_score_participante(jugador)
    form_dict_data["label_score"].update_text(text=f"SCORE: {score_actual}", color=(254, 215, 0))
    
    texto_actual = form_dict_data["text_box"].writing
    form_dict_data["label_input"].update_text(text=f"{texto_actual.upper()}", color=(0, 0, 0))
    form_base.update_widgets(form_dict_data, eventos)

def draw(form_dict_data: dict):
    """
    Dibuja el formulario de victoria en la pantalla
    
    Recibe: form_dict_data: Diccionario del formulario de victoria
    """
    form_base.draw(form_dict_data)
    form_base.dibujar_widgets(form_dict_data)
    form_dict_data.get("text_box").draw()
    