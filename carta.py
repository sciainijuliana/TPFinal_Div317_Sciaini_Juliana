import Modulos.auxiliares as aux
import pygame as pg



def inicializar_cartas_para_juego(cartas: list[dict], coords_inicial: tuple, coords_final: tuple):
    """
    Inicializa las cartas para el juego asignando sus atributos gráficos y posiciones
    - Copia los datos de cada carta
    - Configura coordenadas iniciales y finales
    - Redimensiona imágenes de frente y reverso
    - Genera rectángulos de renderizado para ambas imágenes
    - Marca la carta como no visible inicialmente

    Recibe: cartas: Lista de diccionarios con datos de las cartas (hp, ataque, defensa, bonus, rutas de imágenes) / coords_inicial: Coordenadas iniciales donde se ubica la carta (tupla x, y) / coords_final: Coordenadas finales donde se mostrará la carta (tupla x, y)
    Retorna: Lista de diccionarios de cartas inicializadas con atributos gráficos y coordenadas
    """
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
    """
    Verifica si una carta está visible en pantalla

    Recibe: dict_carta: Diccionario con los datos de la carta
    Retorna: True si la carta está visible, False en caso contrario
    """
    return dict_carta.get("visible")

def cambiar_visibilidad (dict_carta: dict):
    """
    Cambia el estado de visibilidad de una carta a True

    Recibe: dict_carta: Diccionario con los datos de la carta
    """
    dict_carta["visible"] = True

def get_hp (dict_carta: dict) -> int:
    """
    Obtiene los puntos de vida (HP) de una carta

    Recibe: dict_carta: Diccionario con los datos de la carta
    """
    return int(dict_carta.get("hp"))

def get_ataque (dict_carta: dict) -> int:
    """
    Obtiene el valor de ataque de una carta

    Recibe: dict_carta: Diccionario con los datos de la carta
    Retorna: Valor entero de ataque
    """
    return int(dict_carta.get("ataque"))

def get_defensa (dict_carta: dict) -> int:
    """
    Obtiene el valor de defensa de una carta

    Recibe: dict_carta: Diccionario con los datos de la carta
    Retorna: Valor entero de defensa
    """
    return int(dict_carta.get("defensa"))

def get_bonus (dict_carta: dict) -> int:
    """
    Obtiene el valor de bonus de una carta

    Recibe: dict_carta: Diccionario con los datos de la carta
    Retorna: Valor entero de bonus
    """
    return int(dict_carta.get("bonus"))

def get_id (dict_carta: dict) -> float:
    """
    Obtiene el identificador único de una carta

    Recibe: dict_carta: Diccionario con los datos de la carta
    Retorna: Identificador de la carta (puede ser string o numérico)
    """
    return dict_carta.get("id")

def asignar_coords_carta (dict_carta: dict, coords: tuple[int]):
    """
    Asigna nuevas coordenadas a una carta

    Recibe: dict_carta: Diccionario con los datos de la carta
    Recibe: coords: Tupla con las coordenadas (x, y)
    """
    dict_carta["coordenadas"] = coords
    
def draw_carta (carta: dict, screen: pg.Surface):
    """
    Dibuja una carta en la pantalla

    - Si la carta está visible, se dibuja la imagen frontal
    - Si no está visible, se dibuja la imagen reversa

    Recibe: carta: Diccionario con los datos de la carta / screen: Superficie de Pygame donde se dibuja la carta
    """
    if carta.get("visible") == True:
        screen.blit(carta["imagen_frente"], carta["rect_frente"])
    else:
        screen.blit(carta["imagen_reverso"], carta["rect_reverso"])