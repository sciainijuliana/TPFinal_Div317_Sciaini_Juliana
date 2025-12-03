import Modulos.Forms.form_base as form_base
from utn_fra.pygame_widgets import Label, Button
import Modulos.variables as var
import Modulos.auxiliares as aux
import Modulos.audio as audio
import Modulos.Forms.form_options as opt
import pygame as pg


def create_form_eleccion (form_dict_data: dict) -> dict:
    form = form_base.create_base_form(form_dict_data)

    form["label_titulo"] = Label(x=500, y=100, text= "ELIGE UN MAZO", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=60, color=(254, 0, 0))
    form["button_1"]= Button(x=130, y=220, text="SELECT", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=15, color=(254, 0, 0), on_click=confirmar_eleccion, on_click_param=var.DECKS["DECK_1"])
    form["button_2"]= Button(x=270, y=220, text="SELECT", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=15, color=(254, 0, 0), on_click=confirmar_eleccion, on_click_param=var.DECKS["DECK_2"])
    form["button_3"]= Button(x=405, y=220, text="SELECT", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=15, color=(254, 0, 0), on_click=confirmar_eleccion, on_click_param=var.DECKS["DECK_3"])
    form["button_4"]= Button(x=580, y=220, text="SELECT", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=15, color=(254, 0, 0), on_click=confirmar_eleccion, on_click_param=var.DECKS["DECK_4"])
    form["button_5"]= Button(x=720, y=220, text="SELECT", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=15, color=(254, 0, 0), on_click=confirmar_eleccion, on_click_param=var.DECKS["DECK_5"])
    form["button_6"]= Button(x=860, y=220, text="SELECT", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=15, color=(254, 0, 0), on_click=confirmar_eleccion, on_click_param=var.DECKS["DECK_6"])
    form["button_7"]= Button(x=130, y=407, text="SELECT", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=15, color=(254, 0, 0), on_click=confirmar_eleccion, on_click_param=var.DECKS["DECK_7"])
    form["button_8"]= Button(x=270, y=407, text="SELECT", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=15, color=(254, 0, 0), on_click=confirmar_eleccion, on_click_param=var.DECKS["DECK_8"])
    form["button_9"]= Button(x=405, y=407, text="SELECT", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=15, color=(254, 0, 0), on_click=confirmar_eleccion, on_click_param=var.DECKS["DECK_9"])
    form["button_10"]= Button(x=580, y=407, text="SELECT", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=15, color=(254, 0, 0), on_click=confirmar_eleccion, on_click_param=var.DECKS["DECK_10"])
    form["button_11"]= Button(x=720, y=407, text="SELECT", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=15, color=(254, 0, 0), on_click=confirmar_eleccion, on_click_param=var.DECKS["DECK_11"])
    form["button_12"]= Button(x=860, y=407, text="SELECT", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=15, color=(254, 0, 0), on_click=confirmar_eleccion, on_click_param=var.DECKS["DECK_12"])
    form["button_13"]= Button(x=180, y=600, text="SELECT", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=15, color=(254, 0, 0), on_click=confirmar_eleccion, on_click_param=var.DECKS["DECK_13"])
    form["button_14"]= Button(x=340, y=600, text="SELECT", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=15, color=(254, 0, 0), on_click=confirmar_eleccion, on_click_param=var.DECKS["DECK_14"])
    form["button_15"]= Button(x=500, y=600, text="SELECT", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=15, color=(254, 0, 0), on_click=confirmar_eleccion, on_click_param=var.DECKS["DECK_15"])
    form["button_16"]= Button(x=660, y=600, text="SELECT", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=15, color=(254, 0, 0), on_click=confirmar_eleccion, on_click_param=var.DECKS["DECK_16"])
    form["button_17"]= Button(x=820, y=600, text="SELECT", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=15, color=(254, 0, 0), on_click=confirmar_eleccion, on_click_param=var.DECKS["DECK_17"])
    form["button_volver"] = Button(x=500, y=150, text="VOLVER", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=15, color=(254, 0, 0), on_click=opt.cambiar_pantalla, on_click_param="form_menu")

    form["widgets_list"] = [form.get("button_volver"), form.get("label_titulo"), form.get("button_1"),form.get("button_2"),form.get("button_3"),form.get("button_4"),form.get("button_5"),form.get("button_6"),form.get("button_7"),form.get("button_8"),form.get("button_9"),form.get("button_10"),form.get("button_11"),form.get("button_12"),form.get("button_13"),form.get("button_14"),form.get("button_15"),form.get("button_16"),form.get("button_17")]

    var.dict_forms_status[form.get("name")] = form

    return form

def confirmar_eleccion(mazo_elegido: str):
    var.MAZO_ELEGIDO = mazo_elegido
    form_stage = var.dict_forms_status.get("form_stage")
    aux.reset_stage(form_stage)  
    aux.activar_form_a_cambiar("form_stage")

def update(form_dict_data: dict):
    for boton in form_dict_data["widgets_list"]:
        boton.update()

def draw(form_dict_data: dict):
    form_base.draw(form_dict_data)
    for boton in form_dict_data["widgets_list"]:
        boton.draw()