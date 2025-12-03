import pygame as pg
import Modulos.Forms.form_base as form_base
from utn_fra.pygame_widgets import Label, Button
import Modulos.variables as var
import sys
import Modulos.auxiliares as aux
def create_form_ranking (form_dict_data: dict) -> dict:
    form = form_base.create_base_form(form_dict_data)
    form["label_titulo"] = Label(x=500, y=100, text= "RANKING", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=50, color=(255, 192, 223))
    form["lista_ranking_file"] = []
    form["lista_ranking_GUI"] = []
    form["button_volver"] = Button(x=100, y=750, text="VOLVER", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=30, on_click=cambiar_pantalla, on_click_param=["form_menu", form])
    form["data_cargada"] = False
    form["label_rank"] = Label(x=300, y=150, text= "RANK", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(255, 192, 223))
    form["label_nombre"] = Label(x=500, y=150, text= "JUGADOR", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(255, 192, 223))
    form["label_score"] = Label(x=700, y=150, text= "SCORE", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(255, 192, 223))
    
    
    form["widgets_list"] = [form.get("label_titulo"), form.get("button_volver"), form.get("label_rank"), form.get("label_nombre"), form.get("label_score")]

    var.dict_forms_status[form.get("name")] = form

    return form

def draw (form_dict_data: dict):
    form_base.draw(form_dict_data)
    form_base.dibujar_widgets(form_dict_data)
    
    for widget in form_dict_data.get("lista_ranking_GUI"):
        widget.draw()

def update (form_dict_data: dict):
    inicializar_archivo_ranking(form_dict_data)
    form_base.update(form_dict_data)

def cambiar_pantalla (parametros: list):
    form_ranking = parametros[1]
    form_a_cambiar = parametros[0]
    form_ranking["data_cargada"] = False
    form_ranking["lista_ranking_GUI"] = []
    form_ranking["lista_ranking_file"] = []
    form_ranking["active"] = False
    aux.activar_form_a_cambiar(form_a_cambiar)

def inicializar_archivo_ranking (form_dict_data: dict):
    if not form_dict_data.get("data_cargada"):
        form_dict_data["lista_ranking_file"] = aux.cargar_ranking(10)
        init_ranking_data(form_dict_data)
        form_dict_data["data_cargada"] = True

def init_ranking_data (form_dict_data: dict):
    matriz = form_dict_data.get("lista_ranking_file")
    coord_y = 200
    for indice_fila in range(len(matriz)):
        fila = matriz[indice_fila]
        rank = indice_fila + 1
        color_texto = (255, 192, 223)

        if rank > 0 and rank <= 3:
            color_texto = (239, 184, 16)

        posicion = Label(x= 300, y= coord_y, text= f"{rank}",  screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=color_texto)
        nombre = Label(x= 500, y= coord_y, text= f"{fila[0]}",  screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=color_texto)
        score = Label(x= 700, y= coord_y, text= f"{fila[1]}",  screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=color_texto)

        coord_y += 50

        form_dict_data["lista_ranking_GUI"].append(posicion)
        form_dict_data["lista_ranking_GUI"].append(nombre)
        form_dict_data["lista_ranking_GUI"].append(score)