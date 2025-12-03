import pygame as pg
import Modulos.Forms.form_base as form_base
from utn_fra.pygame_widgets import Label, Button
import Modulos.variables as var
import sys
import Modulos.auxiliares as aux
import Modulos.Forms.form_stage as form_stage



def crear_form_menu (form_dict_data: dict) -> dict:
    form = form_base.create_base_form(form_dict_data)

    form["label_titulo"] = Label(x=800, y=450, text= "BIENVENIDO", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=50, color=(255, 238, 140))
    form["button_play"] = Button(x=800, y=500, text="JUGAR", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(255, 238, 140), on_click=aux.activar_form_a_cambiar, on_click_param="form_eleccion")
    form["button_options"] = Button(x=800, y=550, text="OPCIONES", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(255, 238, 140), on_click=aux.activar_form_a_cambiar, on_click_param="form_options")
    form["button_exit"] = Button(x=800, y=700, text="SALIR", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(255, 238, 140), on_click=salir_juego, on_click_param=None)
    form["button_tutorial"] = Button(x=800, y=600, text="TUTORIAL", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(255, 238, 140), on_click=aux.activar_form_a_cambiar, on_click_param="form_tutorial")
    form["button_ranking"] = Button(x=800, y=650, text="RANKING", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(255, 238, 140), on_click=aux.activar_form_a_cambiar, on_click_param="form_ranking")
    form["widgets_list"] = [form.get("label_titulo"), form.get("button_play"), form.get("button_options"), form.get("button_exit"), form.get("button_tutorial"), form.get("button_ranking")]
    

    var.dict_forms_status[form.get("name")] = form

    return form

def salir_juego (_):
    pg.quit()
    sys.exit()

def draw(form_dict_data: dict):
    form_base.draw(form_dict_data)
    form_base.dibujar_widgets(form_dict_data)

def update(form_dict_data: dict):
    events_handler()
    form_base.update(form_dict_data)
    if not form_dict_data.get("music_config").get("music_init"):
        form_dict_data["music_config"]["music_init"] = True
        form_base.play_audio(form_dict_data)

def events_handler ():
    events = pg.event.get()

    for event in events:
        if event.type == pg.QUIT:
            salir_juego()
