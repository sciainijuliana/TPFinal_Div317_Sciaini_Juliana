import pygame.mixer as mixer
import Modulos.variables as var

def play_music (form_dict_data: dict):
    if not form_dict_data.get("music_config").get("music_on"):
        return stop_music(None)
    
    musica = form_dict_data.get("music_path")
    volumen_musica = form_dict_data.get("music_config").get("volumen_musica")
    mixer.music.load(musica)
    mixer.music.set_volume(volumen_musica)
    mixer.music.play(-1)

def stop_music(para_que_no_rompa=None):
    mixer.music.stop()

def get_actual_volume (form_dict_data :dict) -> float:
    return form_dict_data.get("volumen_actual")