import pygame as pg
import Modulos.variables as var
import pygame.mixer as mixer
import Modulos.audio as audio
from utn_fra.pygame_widgets import TextBox

def create_base_form(form_dict_data: dict) -> dict:
    form = {}
    form['name'] = form_dict_data.get('name')
    form['screen'] = form_dict_data.get('screen')
    form['active'] = form_dict_data.get('active')
    form['x_coord'] = form_dict_data.get('coord')[0]
    form['y_coord'] = form_dict_data.get('coord')[1]

    form['music_path'] = form_dict_data.get('music_path')
    form['surface'] = pg.image.load(form_dict_data.get('background')).convert_alpha()
    form['surface'] = pg.transform.scale(form.get('surface'), form_dict_data.get('screen_dimentions'))

    form['rect'] = form['surface'].get_rect()
    form['rect'].x = form_dict_data.get('coord')[0]
    form['rect'].y = form_dict_data.get('coord')[1]
    form["music_config"] = form_dict_data.get("music_config")

    form["volumen_actual"] = form_dict_data.get("music_config").get("volumen_musica")
    return form

def dibujar_widgets (form_data: dict):
    """
    Dibuja los widgets
    """
    for widgets in form_data.get("widgets_list"):
        widgets.draw()

def update_widgets (form_data: dict, eventos: list[pg.event.Event]):
    """
    Actualiza el estado de los widgets por si cambió algo
    """
    for widget in form_data.get("widgets_list"):
        if isinstance(widget, TextBox):
            widget.update(eventos)
        else:
            widget.update()

def update(form_data: dict):
    update_widgets(form_data, None)
    

def draw(form_data: dict):
    screen: pg.Surface = form_data["screen"]
    surface: pg.Surface = form_data["surface"]
    rect: pg.Rect = form_data["rect"]
    screen.blit(surface, rect)


def set_active (form_name: str):
    """
    Primero inactiva todos los formularios, luego activa el que necesito en ese momento
    Recibe el nombre del unico formulario que quiero activo en ese momento
    """
    for form in var.dict_forms_status.values():
        form["active"] = False
    form_activo = var.dict_forms_status[form_name]
    form_activo["active"] = True
    form_activo["volumen_actual"] = form_activo["music_config"].get("volumen_musica")
    audio.stop_music()
    if form_activo["music_config"].get("music_on"):
        audio.play_music(form_activo)

def play_audio (form_dict_data: dict):
    if form_dict_data.get("music_config").get("music_on"):
        audio.play_music(form_dict_data)

def mutear_audio (form_dict_data: dict):
    if form_dict_data.get("music_config").get("music_on"):
        audio.stop_music()
        form_dict_data["music_config"]["music_on"] = False
