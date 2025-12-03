import pygame as pg
import Modulos.Forms.form_base as form_base
from utn_fra.pygame_widgets import Label, ButtonImageSound, ButtonSound
import Modulos.variables as var
import random as rd
import Modulos.auxiliares as aux
import Modulos.Forms.form_options as opt
import participante as part



def crear_form_wish (form_dict_data: dict) -> dict:
    form = form_base.create_base_form(form_dict_data)
    form["jugador"] = form_dict_data.get("jugador")
    form["wish"] = ""

    form["label_titulo"] = Label(x=500, y=300, text= "ELIGE UN DESEO", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=60, color=(254, 215, 0))
    form["button_volver"] = ButtonSound(x=500, y=700, text="", screen=form.get("screen"), sound_path=var.SONIDO_DESEO_OUT,font_path=var.FUENTE_PRINCIPAL, font_size=40, color=(0, 0, 0), on_click=opt.cambiar_pantalla, on_click_param="form_stage")
    form["button_jackpot"] = ButtonImageSound(x=700, y=500, width=120, height=100, text="", screen=form.get("screen"), image_path=var.ICON_JACKPOT, sound_path=var.SONIDO_JACKPOT, font_size=30,  on_click=update_wish, on_click_param=(form, "JACKPOT"))
    form["button_curar"] = ButtonImageSound(x=300, y=500, width=120, height=110, text="", screen=form.get("screen"),image_path=var.ICON_HEAL, sound_path=var.SONDIO_HEAL, font_size=30,  on_click=update_wish, on_click_param=(form, "CURAR"))
    
    form["widgets_list"] = [form.get("label_titulo"), 
                            form.get("button_volver"), 
                            form.get("button_jackpot"),
                            form.get("button_curar")]

    var.dict_forms_status[form.get("name")] = form

    return form

def update_wish(param: tuple):
    form_dict_data, wish = param
    form_dict_data["wish"] = wish
    init_wish(form_dict_data)

def init_wish (form_dict_data: dict):
    wish = form_dict_data.get("wish")
    jugador = form_dict_data.get("jugador")

    if wish == "JACKPOT":
        bonus = rd.choice([1,2,3,4])
        score_jackpot = part.get_score_participante(jugador) * bonus
        part.set_score_participante(jugador, score_jackpot)
    else:
        hp_actual = part.get_hp_participante(jugador)
        hp_inicial = part.get_hp_inicial_participante(jugador)
        hp_cura = hp_inicial // 3
        jugador["hp_actual"] = hp_actual + hp_cura
    
    stage_form = var.dict_forms_status.get("form_stage")
    stage_form["wish_disponible"] = False

    opt.cambiar_pantalla("form_stage")

def update(form_dict_data: dict):
    form_base.update(form_dict_data)

def draw (form_dict_data: dict):
    form_base.draw(form_dict_data)
    form_base.dibujar_widgets(form_dict_data)