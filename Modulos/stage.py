import pygame as pg
import Modulos.variables as var
import Modulos.auxiliares as aux
import random as rd
import carta as card
import json
import participante as part
import random as rd

def inicializar_stage (pantalla: pg.Surface, mazos_dict: dict, ruta_mazo: str, ruta_configs: str, jugador:dict):
    """
    Inicializa el stage de combate
    - Carga configuraciones globales desde archivo
    - Asigna coordenadas iniciales y finales al jugador y enemigo
    - Inicializa al enemigo con un mazo aleatorio
    - Configura estados iniciales del stage (timer, puntaje, flags)
    - Asigna cartas a jugador y enemigo
    - Carga estadísticas iniciales y genera archivo JSON con datos
    - Inicializa las cartas gráficamente en el stage

    Recibe: pantalla: Superficie principal de Pygame / mazos_dict: Diccionario con la base de datos de cartas / ruta_mazo: Nombre del mazo elegido por el jugador / ruta_configs: Ruta del archivo JSON de configuraciones / jugador: Diccionario con los datos del jugador
    Retorna: Diccionario con toda la información del stage inicializado
    """
    
    stage_data = {}
    
    stage_data["configs"] = {}

    configs_globales = aux.cargar_configs(ruta_configs)
    stage_data["configs"] = configs_globales

    stage_data["ruta_mazo"] = ruta_mazo
    stage_data["screen"] = pantalla

    get_stage_configs(configs_globales, stage_data)
    
    jugador["coords_jugador_inicial"] = stage_data["coords_jugador_inicial"]
    jugador["coords_jugador_final"] = stage_data["coords_jugador_final"]

    stage_data["jugador"] = jugador

    
    stage_data["enemigo"] = part.inicializar_participante(pantalla, "Enemigo", stage_data["coords_enemigo_inicial"], stage_data["coords_enemigo_final"])
    mazo_enemigo, cartas_enemigo = elegir_mazo_random(mazos_dict)
    stage_data["enemigo"]["mazo"] = mazo_enemigo
    stage_data["enemigo"]["cartas_en_juego"] = cartas_enemigo

    stage_data["juego_finalizado"] = False
    stage_data["wish_disponible"] = True
    stage_data["puntaje_guardado"] = False
    stage_data["stage_timer"] = var.STAGE_TIMER
    stage_data["data_cargada"] = False
    stage_data["mazos_dict"] = mazos_dict

    asignar_cartas(stage_data)
    cargar_stats(stage_data)
    cargar_json(stage_data)
    inicializar_cartas_stage(stage_data)

    return stage_data

def get_stage_configs (configs_globales: dict, stage_data: dict):
    """
    Extrae configuraciones globales y las asigna al stage

    Recibe: configs_globales: Diccionario con configuraciones cargadas desde archivo / stage_data: Diccionario del stage.
    Retorna: Diccionario del stage actualizado con configuraciones
    """
    stage_data["cantidad_cartas"] = configs_globales.get("cantidad_cartas")
    stage_data["coords_enemigo_inicial"] = tuple(configs_globales.get("coords_enemigo_inicial"))
    stage_data["coords_jugador_inicial"] = tuple(configs_globales.get("coords_jugador_inicial"))
    stage_data["coords_enemigo_final"] = tuple(configs_globales.get("coords_enemigo_final"))
    stage_data["coords_jugador_final"] = tuple(configs_globales.get("coords_jugador_final"))
    stage_data["ganador"] = configs_globales.get("ganador")
    stage_data["puntaje_stage"] = configs_globales.get("puntaje_stage")

    return stage_data


def repartir_cartas (mazo: list[dict], cantidad: int):
    """
    Selecciona aleatoriamente una cantidad especifica de cartas de un mazo

    Recibe: mazo: Lista de cartas disponibles / cantidad: Número de cartas a repartir
    Retorna: Lista de cartas seleccionadas
    """
    return rd.sample(mazo, cantidad)

def asignar_cartas (stage_data:dict):
    """
    Asigna cartas iniciales a jugador y enemigo

    Recibe: stage_data: Diccionario del stage
    Retorna: Diccionario del stage con cartas asignadas
    """
    nombre_mazo_jugador = stage_data["ruta_mazo"]
    mazo_jugador = stage_data["mazos_dict"]["cartas"][nombre_mazo_jugador]

    nombre_mazo_enemigo = stage_data["enemigo"]["mazo"]
    mazo_enemigo = stage_data["mazos_dict"]["cartas"][nombre_mazo_enemigo]

    stage_data["jugador"]["mazo"] = nombre_mazo_jugador
    stage_data["jugador"]["cartas_en_juego"] = repartir_cartas(mazo_jugador, stage_data.get("cantidad_cartas"))

    stage_data["enemigo"]["mazo"] = nombre_mazo_enemigo
    stage_data["enemigo"]["cartas_en_juego"] = repartir_cartas(mazo_enemigo, stage_data.get("cantidad_cartas"))

    return stage_data

def elegir_mazo_random(mazos_dict: dict) -> tuple[str, list[dict]]:
    """
    Elige un mazo al azar de la base de datos de cartas

    Recibe: mazos_dict: Diccionario con mazos y sus cartas
    Retorna: Tupla con nombre del mazo y lista de cartas
    """
    nombre_mazo = rd.choice(list(mazos_dict["cartas"].keys()))
    mazo_elegido_dict = mazos_dict["cartas"][nombre_mazo]
    return nombre_mazo, mazo_elegido_dict


def cargar_stats (stage_data: dict):
    """
    Asigna estadísticas iniciales a jugador y enemigo

    Recibe: stage_data: Diccionario del stage
    """
    stage_data["jugador"] = part.asignar_stats_iniciales(stage_data.get("jugador"))
    stage_data["enemigo"] = part.asignar_stats_iniciales(stage_data.get("enemigo"))
    stage_data["data_cargada"] = True

def cargar_json (stage_data: dict):
    """
    Asigna estadísticas iniciales a jugador y enemigo

    Recibe: stage_data: Diccionario del stage
    """
    jugadores = {
        "jugador": {
            "nombre": stage_data["jugador"]["nombre"],
            "hp_inicial": stage_data["jugador"]["hp_inicial"],
            "hp_actual": stage_data["jugador"]["hp_actual"],
            "ataque": stage_data["jugador"]["ataque"],
            "defensa": stage_data["jugador"]["defensa"],
            "score": stage_data["jugador"]["score"],
            "mazo": stage_data["jugador"]["mazo"],
            "cartas_en_juego": stage_data["jugador"]["cartas_en_juego"],
            "cartas_usadas": stage_data["jugador"].get("cartas_usadas")
        },
        "enemigo": {
            "nombre": stage_data["enemigo"]["nombre"],
            "hp_inicial": stage_data["enemigo"]["hp_inicial"],
            "hp_actual": stage_data["enemigo"]["hp_actual"],
            "ataque": stage_data["enemigo"]["ataque"],
            "defensa": stage_data["enemigo"]["defensa"],
            "score": stage_data["enemigo"]["score"],
            "mazo": stage_data["enemigo"]["mazo"],
            "cartas_en_juego": stage_data["enemigo"]["cartas_en_juego"],
            "cartas_usadas": stage_data["enemigo"].get("cartas_usadas")
        }
    }

    with open(var.JSON_PLAYERS, "w", encoding="utf-8") as file:
        json.dump(jugadores, file, indent=4)

def inicializar_cartas_stage(stage_data: dict):
    """
    Inicializa gráficamente las cartas en el stage para jugador y enemigo

    Recibe: stage_data: Diccionario del stage
    """
    stage_data["jugador"]["cartas_en_juego"] = card.inicializar_cartas_para_juego(
        stage_data["jugador"]["cartas_en_juego"],
        stage_data["coords_jugador_inicial"], stage_data["coords_jugador_final"]
    )

    stage_data["enemigo"]["cartas_en_juego"] = card.inicializar_cartas_para_juego(
        stage_data["enemigo"]["cartas_en_juego"],
        stage_data["coords_enemigo_inicial"], stage_data["coords_enemigo_final"]
    )

def draw_jugadores (stage_data: dict):
    """
    Dibuja al jugador y al enemigo en la pantalla

    Recibe: stage_data: Diccionario del stage
    """
    part.draw(stage_data.get("jugador"), stage_data.get("screen"))
    part.draw(stage_data.get("enemigo"), stage_data.get("screen"))

def draw_cartas (stage_data: dict):
    """
    Dibuja las cartas en juego de jugador y enemigo

    Recibe: stage_data: Diccionario del stage
    """
    screen = stage_data["screen"]
    for carta in stage_data["jugador"].get("cartas_en_juego"):
        card.draw_carta(carta, screen)
    for carta in stage_data["enemigo"].get("cartas_en_juego"):
        card.draw_carta(carta, screen)

def jugar_mano_stage (stage_data: dict):
    """
    Hace que jugador y enemigo jueguen una carta en la mano actual

    Recibe: stage_data: Diccionario del stage
    """
    part.jugar_carta(stage_data.get("jugador"))
    part.jugar_carta(stage_data.get("enemigo"))


def randomizar_critico () -> bool:
    """
    Determina aleatoriamente si un golpe es crítico

    Retorna: True si el golpe es crítico, False en caso contrario
    """
    resultado = rd.choice([True,False,False,False,False,False,False,False,False,False])
    return resultado

def comparar_damage (stage_data: dict):
    """
    Compara el daño entre jugador y enemigo en una mano
    - Obtiene las últimas cartas jugadas
    - Calcula ataque y defensa
    - Aplica daño considerando escudo y crítico
    - Actualiza puntaje si corresponde

    Recibe: stage_data: Diccionario del stage
    Retorna: Cadena con el ganador de la mano ("Player" o "Enemigo")
    """
    ganador_mano = None

    jugador = stage_data.get("jugador")
    enemigo = stage_data.get("enemigo")

    carta_jugador = part.get_ultima_carta_jugada(jugador)
    carta_enemigo = part.get_ultima_carta_jugada(enemigo)
    
    ataque_jugador = card.get_ataque(carta_jugador)
    ataque_enemigo = card.get_ataque(carta_enemigo)

    stage_data["golpe_critico"] = False

    calcular_daño = lambda carta, objetivo, critico: (
        (card.get_ataque(carta) - card.get_defensa(objetivo)) * (card.get_bonus(carta) if critico else 1)
    )

    critico = randomizar_critico()
    stage_data["golpe_critico"] = critico

    if ataque_enemigo > ataque_jugador:
        ganador_mano = "Enemigo"

        if part.get_estado_shield(jugador):
            ganador_mano = "Player"
            part.restar_stats(enemigo, carta_enemigo, critico)
            part.desactivar_bonus_shield(jugador)
        else:
            part.restar_stats(jugador, carta_enemigo, critico)
    else:
        ganador_mano = "Player"
        score = calcular_daño(carta_jugador, carta_enemigo, False)
        part.restar_stats(enemigo, carta_jugador, critico)
        if score > 0:
            part.set_score_participante(jugador, score)

    return ganador_mano

def check_ganador (stage_data: dict):
    """
    Verifica si hay un ganador en el stage
    - Evalúa HP de jugador y enemigo
    - Considera cartas restantes
    - Ajusta puntaje del jugador si pierde

    Recibe: stage_data: Diccionario del stage
    """
    jugador = stage_data.get("jugador")
    enemigo = stage_data.get("enemigo")
    hp_enemigo = part.get_hp_participante(enemigo)
    hp_jugador = part.get_hp_participante(jugador)

    if len(part.get_cartas_participante(jugador)) == 0:
        if hp_jugador > hp_enemigo:
            set_ganador(stage_data, jugador)
        elif hp_jugador < hp_enemigo:
            set_ganador(stage_data, enemigo)
            puntaje_actual = part.get_score_participante(jugador) // 2
            part.set_score_participante(jugador, puntaje_actual)
    else:
        if hp_enemigo == 0 and hp_jugador > 0:
            set_ganador(stage_data, jugador)
        elif hp_jugador == 0 and hp_enemigo > 0:
            set_ganador(stage_data, enemigo)
            puntaje_actual = part.get_score_participante(jugador) // 2
            part.set_score_participante(jugador, puntaje_actual)
        elif hp_enemigo == 0 and hp_jugador == 0:
            set_ganador(stage_data, enemigo)
            puntaje_actual = part.get_score_participante(jugador) // 2
            part.set_score_participante(jugador, puntaje_actual)


def cambiar_pantalla_final(stage_data: dict):
    """
    Cambia la pantalla al formulario de victoria o derrota según el ganador

    Recibe: stage_data: Diccionario del stage
    """
    ganador = stage_data.get("ganador")

    if ganador == stage_data.get("jugador"):
        var.dict_forms_status["form_victoria"]["jugador"] = stage_data["jugador"]
        aux.activar_form_a_cambiar("form_victoria")

    elif ganador == stage_data.get("enemigo"):
        var.dict_forms_status["form_derrota"]["jugador"] = stage_data["jugador"]
        aux.activar_form_a_cambiar("form_derrota")


def set_ganador (stage_data: dict, participante: dict):
    """
    Define al ganador del stage y marca el juego como finalizado

    Recibe: stage_data: Diccionario del stage / participante: Diccionario del jugador o enemigo ganador
    """
    stage_data["ganador"] = participante
    stage_data["juego_finalizado"] = True

def get_estado_juego (stage_data: dict) -> bool:
    """
    Devuelve si el juego está finalizado

    Recibe: stage_data: Diccionario del stage
    Retorna: True si el juego terminó, False en caso contrario
    """
    return stage_data.get("juego_finalizado")

def get_ganador (stage_data: dict):
    """
    Devuelve el participante ganador del stage

    Recibe: stage_data: Diccionario del stage
    Retorna: Diccionario del participante ganador
    """
    return stage_data.get("ganador")

def jugar_turno(stage_data: dict):
    """
    Ejecuta un turno completo en el stage

    - Jugador y enemigo juegan una carta
    - Se compara el daño
    - Se verifica si hay ganador

    Recibe: stage_data: Diccionario del stage
    Retorna: Cadena con el ganador de la mano, o None si el juego terminó
    """
    if not stage_data.get("juego_finalizado"):
        jugar_mano_stage(stage_data)
        ganador_mano = comparar_damage(stage_data)
        check_ganador(stage_data)
        return ganador_mano
    return None
     
