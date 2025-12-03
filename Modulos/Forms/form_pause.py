import Modulos.Forms.form_base as form_base
from utn_fra.pygame_widgets import Label, Button
import Modulos.variables as var
import Modulos.auxiliares as aux
import Modulos.Forms.form_options as opt
import pygame as pg
import Modulos.stage as stage

def create_form_pause (form_dict_data: dict) -> dict:
    form = form_base.create_base_form(form_dict_data)

    form["label_titulo"] = Label(x=500, y=100, text= "PAUSA", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=80, color=(0, 0, 0))
    form["button_music_mute"] = Button(x=700, y=300, text="MUTE MUSIC", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(0, 0, 0), on_click=opt.mutear_audio, on_click_param=form)
    form["button_music_play"] = Button(x=300, y=300, text="PLAY MUSIC", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(0, 0, 0), on_click=opt.play_audio, on_click_param=form)
    form["button_tutorial"] = Button(x= 500, y= 500, text= "TUTORIAL", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(0, 0, 0), on_click=opt.cambiar_pantalla, on_click_param="form_tutorial")
    form["button_restart"] = Button(x= 500, y= 600, text= "REINICIAR", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(0, 0, 0), on_click=lambda _: restart_stage(var.dict_forms_status.get("form_stage")))
    form["button_resume"] = Button(x=500, y=400, text="RESUME", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=40, color=(0, 0, 0), on_click=aux.activar_form_a_cambiar, on_click_param="form_stage")
    form["button_exit"] = Button(x=500, y=700, text="SALIR", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=40, color=(0, 0, 0), on_click=opt.cambiar_pantalla, on_click_param="form_menu")
    form["widgets_list"] = [form.get("label_titulo"), form.get("button_music_mute"), 
                            form.get("button_music_play"), form.get("button_tutorial"), 
                            form.get("button_restart"), form.get("button_resume"), 
                            form.get("button_exit")]

    var.dict_forms_status[form.get("name")] = form

    return form


def restart_stage (form_dict_data: dict):
    aux.reset_stage(form_dict_data)
    form_dict_data["label_timer"].update_text(f"{form_dict_data['stage_timer']}", color=(254, 215, 0))
    form_dict_data["label_score"].update_text(f"{form_dict_data['puntaje_stage']}", color=(254, 215, 0))
    form_dict_data["button_jugar"].on_click_param = form_dict_data["stage"]

    aux.activar_form_a_cambiar("form_stage")

def draw (form_dict_data: dict):
    form_base.draw(form_dict_data)
    form_base.dibujar_widgets(form_dict_data)

def update (form_dict_data: dict):
    form_base.update(form_dict_data)
