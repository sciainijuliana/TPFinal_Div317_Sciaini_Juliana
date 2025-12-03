import pygame as pg
import carta as card
import Modulos.variables as var
import Modulos.auxiliares as aux
import json
import Modulos.stage as stage_juego



def inicializar_participante (pantalla: pg.Surface, nombre: str, coord_inicial: tuple, coord_final: tuple):

    participante = {}

    participante["nombre"] = nombre
    participante["hp_inicial"] = 1
    participante["hp_actual"] = 1
    participante["ataque"] = 1
    participante["defensa"] = 1
    participante["score"] = 0
    participante["cartas_en_juego"] = []
    participante["cartas_usadas"] = []
    participante["screen"] = pantalla
    participante["coords_jugador_inicial"] = coord_inicial
    participante["coords_jugador_final"] = coord_final

    return participante

def get_hp_participante (participante: dict) -> int:
    return participante.get("hp_actual")

def get_hp_inicial_participante (participante: dict) -> int:
    return participante.get("hp_inicial")

def get_ataque_participante (participante: dict) -> int:
    return participante.get("ataque")

def get_defensa_participante (participante: dict) -> int:
    return participante.get("defensa")

def get_score_participante (participante: dict) -> int:
    return participante.get("score")

def get_nombre_participante (participante: dict):
    return participante.get("nombre")

def set_nombre_participante (participante:dict, nuevo_nombre: str):
    participante["nombre"] = nuevo_nombre

def get_cartas_participante (participante:dict) -> list[dict]:
    return participante.get("cartas_en_juego")

def get_coords_inicial (participante:dict):
    return participante.get("coords_jugador_inicial")

def get_coords_jugadas (participante:dict):
    return participante.get("coords_jugador_final")

def get_ultima_carta_jugada (participante:dict):
    cartas_usadas = participante.get("cartas_usadas")
    if cartas_usadas:
        return cartas_usadas[-1]
    return None

def jugar_carta (participante:dict):
    cartas = participante.get("cartas_en_juego")
    if cartas:
        carta_actual = cartas.pop()

        coords = get_coords_jugadas(participante)
        card.asignar_coords_carta(carta_actual, coords)

        carta_actual["visible"] = True
        carta_actual["rect_frente"] = carta_actual["imagen_frente"].get_rect(topleft=coords)
        
        participante.get("cartas_usadas").append(carta_actual)

def set_score_participante (participante:dict, score: int):
    participante["score"] = participante.get("score") + score

def asignar_stats_iniciales (participante:dict):
    participante["hp_inicial"] = aux.reducir(card.get_hp, participante.get("cartas_en_juego"))
    participante["hp_actual"] = participante["hp_inicial"]

    participante["ataque"] = aux.reducir(card.get_ataque, participante.get("cartas_en_juego"))

    participante["defensa"] = aux.reducir(card.get_defensa, participante.get("cartas_en_juego"))

    return participante

def check_valor_negativo (stat: int):
    if stat < 0:
        return 0
    return stat

def restar_stats (participante:dict, carta: dict, critico: bool):

    carta_jugador = participante.get("cartas_usadas")[-1]
    daño = card.get_ataque(carta) - card.get_defensa(carta_jugador)
    damage_amp = 1
    if critico:
        damage_amp = card.get_bonus(carta)
    daño_final = daño * damage_amp
    participante["hp_actual"] = check_valor_negativo(participante.get("hp_actual") - daño_final)

  

def info_to_csv (participante:dict):
    nombre = get_nombre_participante(participante)
    score = get_score_participante(participante)
    return f"{nombre},{score}\n"

def draw (participante: dict, screen: pg.Surface):
    if participante.get("cartas_en_juego"):
        card.draw_carta(participante.get("cartas_en_juego")[-1], screen)
    if participante.get("cartas_usadas"):
        card.draw_carta(participante.get("cartas_usadas")[-1], screen)