import Modulos.Forms.form_base as form_base
from utn_fra.pygame_widgets import Button
import Modulos.variables as var
import Modulos.auxiliares as aux

def create_form_tutorial (form_dict_data: dict) -> dict:

    form = form_base.create_base_form(form_dict_data)

    form["button_volver"] = Button(x=800, y=700, text="VOLVER", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(255, 192, 223), on_click=aux.activar_form_a_cambiar, on_click_param=("form_menu"))

    form["widgets_list"] = [form.get("button_volver")]

    var.dict_forms_status[form.get("name")] = form

    return form

def draw (form_dict_data: dict):
    form_base.draw(form_dict_data)
    form_base.dibujar_widgets(form_dict_data)

def update (form_dict_data: dict):
    form_base.update(form_dict_data)

