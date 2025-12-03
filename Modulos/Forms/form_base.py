import pygame as pg
import Modulos.variables as var
import pygame.mixer as mixer
import Modulos.audio as audio
from utn_fra.pygame_widgets import TextBox

def create_base_form(form_dict_data: dict) -> dict:
    """
    Crea y configura un formulario base con sus propiedades gráficas y de audio

    Recibe: form_dict_data: Diccionario con la configuración inicial del formulario
           Debe contener las claves:
           - 'name': nombre del formulario
           - 'screen': superficie principal de Pygame donde se dibuja
           - 'active': estado de activación del formulario (bool)
           - 'coord': tupla con coordenadas (x, y)
           - 'music_path': ruta del archivo de música
           - 'background': ruta de la imagen de fondo
           - 'screen_dimentions': dimensiones de la pantalla
           - 'music_config': diccionario con configuración de música (volumen, estado)
    Retorna: Un diccionario con los datos
    """

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
    Dibuja todos los widgets asociados al formulario

    Recibe: form_data: Diccionario del formulario que contiene la lista 'widgets_list'
                      con los widgets a dibujar
    """
    for widgets in form_data.get("widgets_list"):
        widgets.draw()

def update_widgets (form_data: dict, eventos: list[pg.event.Event]):
    """
    Actualiza el estado de los widgets del formulario

    Si el widget es un TextBox, se actualiza con la lista de eventos recibida
    Para otros widgets, se actualizan sin parámetros

    Recibe: form_data: Diccionario del formulario que contiene la lista 'widgets_list'. eventos: Lista de eventos de Pygame que pueden afectar a los widgets
    """
    for widget in form_data.get("widgets_list"):
        if isinstance(widget, TextBox):
            widget.update(eventos)
        else:
            widget.update()

def update(form_data: dict):
    """
    Llama a update_widgets para refrescar el estado de todos los widgets, y actualiza el formulario completo

    Recibe: form_data: Diccionario del formulario
    """
    update_widgets(form_data, None)
    

def draw(form_data: dict):
    """
    Dibuja la superficie de fondo del formulario en la pantalla

    Recibe: form_data: Diccionario del formulario con las claves que contienen los pg.Surface
    """
    screen: pg.Surface = form_data["screen"]
    surface: pg.Surface = form_data["surface"]
    rect: pg.Rect = form_data["rect"]
    screen.blit(surface, rect)


def set_active (form_name: str):
    """
    Activa un formulario y desactiva todos los demás
    También actualiza el volumen actual y gestiona la reproducción de música
    según la configuración del formulario

    Recibe: form_name: Nombre del formulario que se desea activar
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
    """
    Reproduce la música asociada al formulario, solo si está habilitada

    Recibe: form_dict_data: Diccionario del formulario con la clave 'music_config'
                           donde se indica si la música está activa
    """
    if form_dict_data.get("music_config").get("music_on"):
        audio.play_music(form_dict_data)

def mutear_audio (form_dict_data: dict):
    """
    Detiene la música del formulario y actualiza la configuración para indicar
    que la música está desactivada

    Recibe: form_dict_data: Diccionario del formulario con la clave 'music_config'
    """
    if form_dict_data.get("music_config").get("music_on"):
        audio.stop_music()
        form_dict_data["music_config"]["music_on"] = False
