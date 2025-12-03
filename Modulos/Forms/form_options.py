import pygame as py
import pygame.mixer as mixer
import Modulos.Forms.form_base as form_base
from utn_fra.pygame_widgets import Label, Button
import Modulos.variables as var
import Modulos.auxiliares as aux
import Modulos.audio as audio



def create_form_options (form_dict_data: dict) -> dict:
    form = form_base.create_base_form(form_dict_data)

    form["label_titulo"] = Label(x=500, y=100, text= "OPCIONES", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=70, color=(255, 192, 223))
    form["label_volumen_actual"] = Label(x=500, y=300, text= f"{audio.get_actual_volume(form)}", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=50, color=(255, 192, 223))
    form["button_music_up"] = Button(x=300, y=300, text="+", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=50, color=(255, 192, 223), on_click=subir_volumen, on_click_param=form)
    form["button_music_down"] = Button(x=700, y=300, text="-", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=50, color=(255, 192, 223), on_click=bajar_volumen, on_click_param=form)
    form["button_music_mute"] = Button(x=600, y=400, text="MUTE", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(255, 192, 223), on_click=mutear_audio, on_click_param=form)
    form["button_music_play"] = Button(x=400, y=400, text="PLAY", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(255, 192, 223), on_click=play_audio, on_click_param=form)
    form["button_volver"] = Button(x=500, y=600, text="VOLVER", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(255, 192, 223), on_click=cambiar_pantalla, on_click_param="form_menu")
    form["widgets_list"] = [form.get("label_titulo"), form.get("button_music_up"), form.get("button_music_down"), form.get("button_music_mute"), form.get("button_volver"), form.get("label_volumen_actual"), form.get("button_music_play")]

    var.dict_forms_status[form.get("name")] = form

    return form

def draw (form_dict_data: dict):
    form_base.draw(form_dict_data)
    form_base.dibujar_widgets(form_dict_data)

def update (form_dict_data: dict):
    form_base.update(form_dict_data)

def cambiar_pantalla (form_a_cambiar: str):
    if form_a_cambiar == "form_stage":
        aux.reset_stage(var.dict_forms_status.get("form_stage"))
    aux.activar_form_a_cambiar(form_a_cambiar)

def subir_volumen (form_dict_data: dict):
    volumen_actual = audio.get_actual_volume(form_dict_data)
    if volumen_actual < 1.0:
        nuevo_volumen = volumen_actual + 0.1
        if nuevo_volumen > 1.0:  
            nuevo_volumen = 1.0
        
        form_dict_data["music_config"]["volumen_musica"] = nuevo_volumen
        form_dict_data["volumen_actual"] = nuevo_volumen
        form_dict_data["widgets_list"][5] = Label(
            x=500, y=300,
            text=f"{nuevo_volumen:.1f}",
            screen=form_dict_data.get("screen"),
            font_path=var.FUENTE_PRINCIPAL,
            font_size=50,
            color=(255, 192, 223)
        )
        form_dict_data["label_volumen_actual"].draw()
        mixer.music.set_volume(nuevo_volumen)
    elif volumen_actual == 0:
        audio.stop_music(None)

    return form_dict_data

def bajar_volumen(form_dict_data: dict):
    volumen_actual = audio.get_actual_volume(form_dict_data)
    if volumen_actual > 0.0:
        nuevo_volumen = volumen_actual - 0.1
        if volumen_actual < 0.0:
            nuevo_volumen = 0.0

        form_dict_data["music_config"]["volumen_musica"] = nuevo_volumen
        form_dict_data["volumen_actual"] = nuevo_volumen
        form_dict_data["widgets_list"][5] = Label(
            x=500, y=300,
            text=f"{nuevo_volumen:.1f}",
            screen=form_dict_data.get("screen"),
            font_path=var.FUENTE_PRINCIPAL,
            font_size=50,
            color=(255, 192, 223)
        )
        form_dict_data["label_volumen_actual"].draw()
        mixer.music.set_volume(nuevo_volumen)

    elif volumen_actual == 0:
        audio.stop_music(None)
        
    return form_dict_data

def mutear_audio (form_dict_data: dict):
    form_dict_data["music_config"]["music_on"] = False
    audio.stop_music()

def play_audio (form_dict_data: dict):
    form_dict_data["music_config"]["music_on"] = True
    audio.play_music(form_dict_data)