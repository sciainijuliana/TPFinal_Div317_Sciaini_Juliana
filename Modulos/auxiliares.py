import Modulos.Forms.form_base as form_base
import Modulos.variables as var
import json
import os
import pygame as pg

def activar_form_a_cambiar (form_name: str):
    form_base.set_active(form_name)

def cargar_ranking(top: int= 10):
    ranking = []
    with open(var.RANKING, "r", encoding="utf-8") as file:
        texto = file.read()

        for linea in texto.split("\n"):
            if linea:
                lista_datos = linea.split(",")
                ranking.append(lista_datos)

    mapear_valores(ranking, indice_a_mapear=1, callback=parsear_entero)
    ranking.sort(key=lambda fila: fila[1], reverse=True)

    return ranking[:top]

def mapear_valores (matriz: list[list], indice_a_mapear: int, callback):
    for indice_fila in range(len(matriz)):
        valor = matriz[indice_fila][indice_a_mapear]
        matriz[indice_fila][indice_a_mapear] = callback(valor)

def parsear_entero (valor: str):
    if valor.isdigit():
        return int(valor)
    
def cargar_configs (file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def generar_bd_cartas (file_paths: dict) -> list[dict]:
    mazos_dict = {
        "cartas": {}
    }

    for deck_name, path in file_paths.items():
        reverse_path = ""
        deck_cards = []
    
        for root, dir, files in os.walk(path):
            for carta in files:
                card_path = os.path.join(root, carta)
                if "reverse" in card_path:
                    reverse_path = card_path
                    pass
                else:
                    card_path = card_path.replace("\\", "/")
                    filename = carta
                    deck_name = root.split("\\")[-1]

                    filename = filename.replace(".png", "")
                    datos_crudo = filename.split("_")

                    datos_carta ={
                        "id": datos_crudo[0],
                        "hp": datos_crudo[2],
                        "ataque": datos_crudo[4],
                        "defensa": datos_crudo[6],
                        "bonus": datos_crudo[7],
                        "ruta_frente": card_path,
                        "ruta_reverse": ""
                    }
                    deck_cards.append(datos_carta)

        for index_carta in range(len(deck_cards)):
            deck_cards[index_carta]["ruta_reverse"] = reverse_path
        
        mazos_dict["cartas"][deck_name] = deck_cards

    return mazos_dict

def guardar_info_cartas(file_path: str, dict_cards: dict):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(dict_cards, file, indent=4)

def guardar_info_csv (ruta_csv: str, info: str):
    with open(ruta_csv, "a", encoding="utf-8") as file:
        file.write(info)

def cargar_bd_cartas (stage_data:dict):
    if not stage_data.get("juego_finalizado"):
        stage_data["cartas_mazo_inicial"] = generar_bd_cartas(stage_data.get("ruta_mazo"))

def redimensionar_img (img_path, porcentaje_a_ajustar: int):
    if isinstance(img_path, str):
        imagen_raw = pg.image.load(img_path).convert_alpha()
    else:
        imagen_raw = img_path

    ancho, alto = imagen_raw.get_size()

    nuevo_alto = int(alto * float(f"0.{porcentaje_a_ajustar}"))
    nuevo_ancho = int(ancho * float(f"0.{porcentaje_a_ajustar}"))

    imagen_final = pg.transform.scale(imagen_raw, (nuevo_ancho, nuevo_alto))

    return imagen_final

def reducir (callback, iterable:list):
    suma = 0
    for elemento in iterable:
        suma += callback(elemento)
    return suma

def reset_stage (form_dict_data: dict):
    """
    Reinicia la partida creando un nuevo stage desde cero.
    """
    form_dict_data["stage"] = None
    form_dict_data["stage_restart"] = True
    form_dict_data["juego_finalizado"] = False
    form_dict_data["times_up"] = False
    form_dict_data["ganador"] = None
    form_dict_data["puntaje_stage"] = 0
    form_dict_data["stage_timer"] = var.STAGE_TIMER
    form_dict_data["last_timer_check"] = pg.time.get_ticks()
    form_dict_data["wish_disponible"] = True

    jugador = form_dict_data.get("jugador")
    if jugador:
        jugador["cartas_en_juego"] = []
        jugador["cartas_usadas"] = []
        jugador.pop("imagen_frente", None)
        jugador.pop("imagen_reverso", None)
        jugador.pop("rect_frente", None)
        jugador.pop("rect_reverso", None)