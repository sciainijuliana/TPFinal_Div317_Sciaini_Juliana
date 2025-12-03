import Modulos.auxiliares as aux
import pygame as pg



def inicializar_cartas_para_juego(cartas: list[dict], coords_inicial: tuple, coords_final: tuple):
    cartas_inicializadas = []
    for dict_carta in cartas:
        carta = dict_carta.copy()
        carta["visible"] = False
        carta["coordenadas"] = coords_inicial
        carta["coordenadas_final"] = coords_final

        frente_img = aux.redimensionar_img(carta["ruta_frente"], 50)
        carta["imagen_frente"] = frente_img
        carta["rect_frente"] = frente_img.get_rect(topleft=carta["coordenadas_final"])

        reverse_img = aux.redimensionar_img(carta["ruta_reverse"], 50)
        carta["imagen_reverso"] = reverse_img
        carta["rect_reverso"] = reverse_img.get_rect(topleft=carta["coordenadas"])

        cartas_inicializadas.append(carta)
    return cartas_inicializadas
    
def esta_visible (dict_carta: dict) -> bool:
    return dict_carta.get("visible")

def cambiar_visibilidad (dict_carta: dict):
    dict_carta["visible"] = True

def get_hp (dict_carta: dict) -> int:
    return int(dict_carta.get("hp"))

def get_ataque (dict_carta: dict) -> int:
    return int(dict_carta.get("ataque"))

def get_defensa (dict_carta: dict) -> int:
    return int(dict_carta.get("defensa"))

def get_bonus (dict_carta: dict) -> int:
    return int(dict_carta.get("bonus"))

def get_id (dict_carta: dict) -> float:
    return dict_carta.get("id")

def asignar_coords_carta (dict_carta: dict, coords: tuple[int]):
    dict_carta["coordenadas"] = coords
    
def draw_carta (carta: dict, screen: pg.Surface):
    if carta.get("visible") == True:
        screen.blit(carta["imagen_frente"], carta["rect_frente"])
    else:
        screen.blit(carta["imagen_reverso"], carta["rect_reverso"])