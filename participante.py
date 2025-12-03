import pygame as pg
import carta as card
import Modulos.auxiliares as aux





def inicializar_participante (pantalla: pg.Surface, nombre: str, coord_inicial: tuple, coord_final: tuple):
    """
    Inicializa un participante del juego con valores por defecto
    - Asigna nombre, estadísticas iniciales (hp, ataque, defensa)
    - Configura listas de cartas en juego y usadas
    - Define coordenadas iniciales y finales en pantalla
    - Marca el escudo como inactivo

    Recibe: pantalla: Superficie principal de Pygame donde se dibuja el participante / nombre: Nombre del participante (ej. "Player" o "Enemigo") / coord_inicial: Coordenadas iniciales del participante / coord_final: Coordenadas finales del participante
    Retorna: Diccionario con los datos del participante inicializado
    """

    participante = {}

    participante["nombre"] = nombre
    participante["hp_inicial"] = 1
    participante["hp_actual"] = 1
    participante["ataque"] = 1
    participante["defensa"] = 1
    participante["score"] = 0
    participante["cartas_en_juego"] = []
    participante["cartas_usadas"] = []
    participante["bonus_shield_active"] = False
    participante["screen"] = pantalla
    participante["coords_jugador_inicial"] = coord_inicial
    participante["coords_jugador_final"] = coord_final

    return participante

def get_hp_participante (participante: dict) -> int:
    """
    Obtiene los puntos de vida actuales del participante

    Recibe: participante: Diccionario con los datos del participante
    Retorna: Valor entero de HP actual
    """
    return participante.get("hp_actual")

def get_hp_inicial_participante (participante: dict) -> int:
    """
    Obtiene los puntos de vida iniciales del participante

    Recibe: participante: Diccionario con los datos del participante
    Retorna: Valor entero de HP inicial
    """
    return participante.get("hp_inicial")

def get_ataque_participante (participante: dict) -> int:
    """
    Obtiene el valor de ataque del participante

    Recibe: participante: Diccionario con los datos del participante
    Retorna: Valor entero de ataque
    """
    return participante.get("ataque")

def get_defensa_participante (participante: dict) -> int:
    """
    Obtiene el valor de defensa del participante

    Recibe: participante: Diccionario con los datos del participante
    Retorna: Valor entero de defensa
    """
    return participante.get("defensa")

def get_score_participante (participante: dict) -> int:
    """
    Obtiene el puntaje actual del participante

    Recibe: participante: Diccionario con los datos del participante
    Retorna: Valor entero del puntaje
    """
    return participante.get("score")

def get_nombre_participante (participante: dict):
    """
    Obtiene el nombre del participante

    Recibe: participante: Diccionario con los datos del participante
    Retorna: Nombre del participante
    """
    return participante.get("nombre")

def set_nombre_participante (participante:dict, nuevo_nombre: str):
    """
    Asigna un nuevo nombre al participante

    Recibe: participante: Diccionario con los datos del participante
    Recibe: nuevo_nombre: Nombre nuevo a asignar
    """
    participante["nombre"] = nuevo_nombre

def get_cartas_participante (participante:dict) -> list[dict]:
    """
    Obtiene la lista de cartas en juego del participante

    Recibe: participante: Diccionario con los datos del participante
    Retorna: Lista de cartas en juego
    """
    return participante.get("cartas_en_juego")

def get_coords_inicial (participante:dict):
    """
    Obtiene las coordenadas iniciales del participante

    Recibe: participante: Diccionario con los datos del participante
    Retorna: Tupla con coordenadas iniciales (x, y)
    """
    return participante.get("coords_jugador_inicial")

def get_coords_jugadas (participante:dict):
    """
    Obtiene las coordenadas finales del participante

    Recibe: participante: Diccionario con los datos del participante
    Retorna: Tupla con coordenadas finales (x, y)
    """
    return participante.get("coords_jugador_final")

def get_ultima_carta_jugada (participante:dict):
    """
    Obtiene la última carta jugada por el participante

    Recibe: participante: Diccionario con los datos del participante
    Retorna: Diccionario de la última carta jugada, o None si no hay cartas usadas
    """
    cartas_usadas = participante.get("cartas_usadas")
    if cartas_usadas:
        return cartas_usadas[-1]
    return None

def jugar_carta (participante:dict):
    """
    Juega una carta del participante
    - Extrae la última carta de la lista de cartas en juego
    - Asigna coordenadas finales
    - Marca la carta como visible
    - Actualiza el rectángulo frontal
    - Mueve la carta a la lista de cartas usadas

    Recibe: participante: Diccionario con los datos del participante
    """
    cartas = participante.get("cartas_en_juego")
    if cartas:
        carta_actual = cartas.pop()

        coords = get_coords_jugadas(participante)
        card.asignar_coords_carta(carta_actual, coords)

        carta_actual["visible"] = True
        carta_actual["rect_frente"] = carta_actual["imagen_frente"].get_rect(topleft=coords)
        
        participante.get("cartas_usadas").append(carta_actual)

def set_score_participante (participante:dict, score: int):
    """
    Incrementa el puntaje del participante

    Recibe: participante: Diccionario con los datos del participante / score: Valor entero a sumar al puntaje actual
    """
    participante["score"] = participante.get("score") + score

def asignar_stats_iniciales (participante:dict):
    """
    Asigna estadísticas iniciales al participante en base a sus cartas
    - HP inicial y actual
    - Ataque total
    - Defensa total

    Recibe: participante: Diccionario con los datos del participante
    Retorna: Diccionario del participante actualizado con estadísticas iniciales
    """
    participante["hp_inicial"] = aux.reducir(card.get_hp, participante.get("cartas_en_juego"))
    participante["hp_actual"] = participante["hp_inicial"]

    participante["ataque"] = aux.reducir(card.get_ataque, participante.get("cartas_en_juego"))

    participante["defensa"] = aux.reducir(card.get_defensa, participante.get("cartas_en_juego"))

    return participante

def check_valor_negativo (stat: int):
    """
    Verifica que un valor no sea negativo

    Recibe: stat: Valor entero a verificar
    Retorna: 0 si el valor es negativo, o el mismo valor si es positivo
    """
    if stat < 0:
        return 0
    return stat

def restar_stats (participante:dict, carta: dict, critico: bool):
    """
    Resta puntos de vida al participante en base al ataque recibido
    - Calcula daño como ataque de la carta menos defensa de la última carta jugada
    - Si el golpe es crítico, multiplica el daño por el bonus de la carta
    - Actualiza HP actual del participante, evitando valores negativos

    Recibe: participante: Diccionario con los datos del participante / carta: Diccionario de la carta atacante / critico: Booleano que indica si el golpe fue crítico
    """
    carta_jugador = participante.get("cartas_usadas")[-1]
    
    calcular_daño = lambda atacante, objetivo, critico: (
        (card.get_ataque(atacante) - card.get_defensa(objetivo)) *
        (card.get_bonus(atacante) if critico else 1)
    )

    daño_final = calcular_daño(carta, carta_jugador, critico)
    participante["hp_actual"] = check_valor_negativo(participante.get("hp_actual") - daño_final)

def activar_bonus_shield (participante: dict):
    """
    Activa el escudo espejo del participante

    Recibe: participante: Diccionario con los datos del participante
    """
    participante["bonus_shield_active"] = True

def desactivar_bonus_shield (participante: dict):
    """
    Desactiva el escudo espejo del participante y reinicia sus usos

    Recibe: participante: Diccionario con los datos del participante
    """
    participante["bonus_shield_active"] = False
    participante["usos_shield"] = 0

def get_estado_shield (participante: dict) -> bool:
    """
    Verifica si el escudo espejo del participante está activo

    Recibe: participante: Diccionario con los datos del participante
    Retorna: True si el escudo está activo, False en caso contrario
    """
    return participante.get("bonus_shield_active")

def draw (participante: dict, screen: pg.Surface):
    """
    Dibuja las cartas del participante en la pantalla

    - Si hay cartas en juego, dibuja la última carta
    - Si hay cartas usadas, dibuja la última carta jugada

    Recibe: participante: Diccionario con los datos del participante / screen: Superficie de Pygame donde se dibujan las cartas
    """
    if participante.get("cartas_en_juego"):
        card.draw_carta(participante.get("cartas_en_juego")[-1], screen)
    if participante.get("cartas_usadas"):
        card.draw_carta(participante.get("cartas_usadas")[-1], screen)