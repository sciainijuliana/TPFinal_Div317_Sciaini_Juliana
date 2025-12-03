import Modulos.Forms.form_base as form_base
from utn_fra.pygame_widgets import Button, Label
import Modulos.variables as var
import Modulos.auxiliares as aux
import pygame as pg

def create_form_tutorial (form_dict_data: dict) -> dict:
    """
    Crea y configura el formulario de tutorial del juego.

    Recibe: form_dict_data: Diccionario con la configuración inicial del formulario
    
    Retorna: Diccionario que representa el formulario de tutorial
    """

    form = form_base.create_base_form(form_dict_data)

    form["screen"] = pg.display.set_mode((var.DIMENSION_PANTALLA))
    form["backgrounds"] = var.CARRUSEL_TUTORIAL
    form["indice_actual"] = 0


    form["button_siguiente"] =Button(x=800, y=600, text=">>", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=70, color=(255, 192, 50), on_click=siguiente_background, on_click_param=form)
    form["button_anterior"] = Button(x=200, y=600, text="<<", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=70, color=(255, 192, 50), on_click=anterior_background, on_click_param=form)
    form["label_titulo"] = Label(x=500, y=700, text= "TUTORIAL", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=60, color=(254, 192, 50))
    form["button_volver"] = Button(x=500, y=750, text="VOLVER", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(255, 192, 50), on_click=aux.activar_form_a_cambiar, on_click_param=("form_menu"))

    form["widgets_list"] = [form.get("button_volver"), form.get("button_anterior"),
                            form.get("button_siguiente"), form.get("label_titulo")]

    var.dict_forms_status[form.get("name")] = form

    return form

def mostrar_background(form_dict_data: dict):
    """
    Muestra el background actual en la pantalla
    - Obtiene la ruta de la imagen correspondiente al índice actual
    - Carga la imagen con pygame
    - Dibuja (blit) la imagen en la superficie principal en la posición (0,0)

    Recibe: form_dict_data (dict): Diccionario del formulario tutorial
    """
    img_path = form_dict_data["backgrounds"][form_dict_data["indice_actual"]]
    background = pg.image.load(img_path)

    form_dict_data["screen"].blit(background, (0, 0))


def siguiente_background(form_dict_data: dict):
    """
    Cambia al siguiente background en la lista y lo muestra en pantalla.

    Recibe: form_dict_data (dict)
    """
    form_dict_data["indice_actual"] += 1
    if form_dict_data["indice_actual"] >= len(form_dict_data["backgrounds"]):
        form_dict_data["indice_actual"] = 0
    mostrar_background(form_dict_data)

def anterior_background(form_dict_data: dict):
    """
    Cambia al anterior background en la lista y lo muestra en pantalla.

    Recibe: form_dict_data (dict)
    """
    form_dict_data["indice_actual"] -= 1
    if form_dict_data["indice_actual"] < 0:
        form_dict_data["indice_actual"] = len(form_dict_data["backgrounds"]) - 1
    mostrar_background(form_dict_data)

def draw (form_dict_data: dict):
    """
    Renderiza la superficie de fondo y dibuja todos los widgets del formulario

    Recibe: form_dict_data: Diccionario del formulario de tutorial
    """
    mostrar_background(form_dict_data)
    form_base.dibujar_widgets(form_dict_data)
    pg.display.flip()

def update (form_dict_data: dict):
    """
    Actualiza el estado del formulario de tutorial
    Llama a la función base para refrescar los widgets

    Recibe: form_dict_data: Diccionario del formulario de tutorial
    """
    form_base.update(form_dict_data)
    mostrar_background(form_dict_data)

