import Modulos.Forms.form_base as form_base
from utn_fra.pygame_widgets import Label, Button,TextBox
import Modulos.variables as var
import pygame as pg
import Modulos.Forms.form_victoria as vic
import Modulos.auxiliares as aux
import participante as part

def create_form_derrota (form_dict_data: dict) -> dict:
    form = form_base.create_base_form(form_dict_data)
    jugador = form_dict_data.get("jugador")
    form["jugador"] = jugador

    form["label_derrota"] = Label(x=500, y=500, text= "HAS SIDO DERROTADO:", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=60, color=(254, 215, 0))
    form["label_score"] = Label(x=500, y=600, text= f"Tu score es:{part.get_score_participante(jugador)}", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(254, 215, 0))
    form["label_titulo"] = Label(x=500, y=620, text= "Ingresa tu nombre:", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(254, 215, 0))

    form["button_submit"] = Button(x=800, y=750, text= ">>", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=50, color=(254, 215, 0), on_click=vic.subir_nombre, on_click_param=form)

    form["text_box"] = TextBox(x=400, y=700, text= "", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=20, color=(0, 0, 0))
    form["label_input"] = Label(x=500, y=700, text= "", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(0, 0, 0))

    form["widgets_list"] = [form.get("text_box"), form.get("label_derrota"), form.get("label_titulo"), form.get("label_score"), form.get("label_input"), form.get("button_submit")]

    var.dict_forms_status[form.get("name")] = form

    return form


    
    