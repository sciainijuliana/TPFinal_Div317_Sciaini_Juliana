import pygame.mixer as mixer
import Modulos.variables as var

def play_music (form_dict_data: dict):
    """
    Reproduce la música asociada a un formulario
    - Verifica si la música está activada en la configuración
    - Si está desactivada, detiene cualquier reproducción
    - Si está activada, carga el archivo de música indicado, ajusta el volumen
      y comienza la reproducción en bucle

    Recibe: form_dict_data: Diccionario del formulario
    """
    if not form_dict_data.get("music_config").get("music_on"):
        return stop_music(None)
    
    musica = form_dict_data.get("music_path")
    volumen_musica = form_dict_data.get("music_config").get("volumen_musica")
    mixer.music.load(musica)
    mixer.music.set_volume(volumen_musica)
    mixer.music.play(-1)

def stop_music(para_que_no_rompa=None):
    """
    Detiene la reproducción de música

    Recibe: para_que_no_rompa: Parámetro opcional sin uso, incluido para compatibilidad
    """
    mixer.music.stop()

def get_actual_volume (form_dict_data :dict) -> float:
    """
    Obtiene el volumen actual de la música del formulario

    Recibe: form_dict_data: Diccionario del formulario
    Retorna: Valor float que representa el volumen actual (entre 0.0 y 1.0)
    """
    return form_dict_data.get("volumen_actual")