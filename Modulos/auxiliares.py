import Modulos.Forms.form_base as form_base
import participante as part
import Modulos.variables as var
import json
import os
import pygame as pg

def activar_form_a_cambiar (form_name: str):
    """
    Activa un formulario específico y desactiva los demás

    Recibe: form_name: Nombre del formulario que se desea activar
    """
    form_base.set_active(form_name)

def cambiar_pantalla_reiniciando (form_a_cambiar: str):
    """
    Cambia la pantalla activa a otro formulario, reiniciando el stage si corresponde
    - Si el formulario a cambiar es 'form_stage', se reinicia el stage
    - Luego se activa el formulario indicado

    Recibe: form_a_cambiar: Nombre del formulario al que se desea cambiar
    """
    if form_a_cambiar == "form_stage":
        reset_stage(var.dict_forms_status.get("form_stage"))
    activar_form_a_cambiar(form_a_cambiar)

def cargar_ranking(top: int= 10):
    """
    Carga los datos del ranking desde archivo CSV
    - Lee el archivo de ranking
    - Convierte los puntajes a enteros
    - Ordena los jugadores por puntaje descendente
    - Devuelve los primeros 'top' registros

    Recibe: top: Número máximo de registros a devolver
    Retorna: Lista de listas con los datos del ranking
    """
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
    """
    Aplica una función de transformación a un valor específico de cada fila de la matriz

    Recibe: matriz: Lista de listas con los datos / indice_a_mapear: Índice de la columna a transformar / callback: Función que recibe el valor y devuelve el valor transformado
    """
    for indice_fila in range(len(matriz)):
        valor = matriz[indice_fila][indice_a_mapear]
        matriz[indice_fila][indice_a_mapear] = callback(valor)

def parsear_entero (valor: str):
    """
    Convierte un valor string a entero si es un número válido

    Recibe: valor: Cadena de texto a convertir
    Retorna: Entero si el valor es numérico, None en caso contrario
    """
    if valor.isdigit():
        return int(valor)
    
def cargar_configs (file_path: str) -> dict:
    """
    Carga un archivo JSON de configuración

    Recibe: file_path: Ruta del archivo JSON
    Retorna: Diccionario con los datos de configuración
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def generar_bd_cartas (file_paths: dict) -> list[dict]:
    """
    Genera la base de datos de cartas a partir de las imágenes en las carpetas de mazos

    - Recorre los directorios de cartas
    - Extrae atributos de cada carta desde el nombre del archivo
    - Asocia la ruta de la imagen frontal y reverso
    - Organiza las cartas por mazo

    Recibe: file_paths: Diccionario con nombres de mazos y sus rutas de carpeta

    Retorna: Diccionario con la base de datos de cartas organizada por mazo
    """
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
    """
    Guarda la información de cartas en un archivo JSON

    Recibe: file_path: Ruta del archivo JSON / dict_cards: Diccionario con la información de cartas
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(dict_cards, file, indent=4)

def guardar_info_csv (ruta_csv: str, info: str):
    """
    Guarda información en un archivo CSV, agregando una nueva línea

    Recibe: ruta_csv: Ruta del archivo CSV / info: Cadena con la información a guardar
    """
    with open(ruta_csv, "a", encoding="utf-8") as file:
        file.write(info)

def cargar_bd_cartas (stage_data:dict):
    """
    Carga la base de datos de cartas en el stage si el juego no está finalizado

    Recibe: stage_data: Diccionario con los datos del stage
    """
    if not stage_data.get("juego_finalizado"):
        stage_data["cartas_mazo_inicial"] = generar_bd_cartas(stage_data.get("ruta_mazo"))

def redimensionar_img (img_path, porcentaje_a_ajustar: int):
    """
    Redimensiona una imagen según un porcentaje dado

    - Si se pasa una ruta, carga la imagen desde archivo
    - Si se pasa una superficie, la usa directamente
    - Ajusta ancho y alto según el porcentaje

    Recibe: img_path: Ruta de la imagen o superficie de Pygame / porcentaje_a_ajustar: Porcentaje de ajuste

    Retorna: Superficie de Pygame redimensionada
    """
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
    """
    Aplica una función a cada elemento de una lista y suma los resultados

    Recibe: callback: Función que recibe un elemento y devuelve un valor numérico / iterable: Lista de elementos a procesar
    Retorna: Suma de los valores devueltos por el callback
    """
    suma = 0
    for elemento in iterable:
        suma += callback(elemento)
    return suma

def reset_stage (form_dict_data: dict):
    """
    Reinicia la partida creando un nuevo stage desde cero
    - Restablece los valores de control del stage
    - Reinicia el puntaje, temporizador y disponibilidad de deseos
    - Limpia las cartas y atributos del jugador

    Recibe: form_dict_data: Diccionario del formulario de stage
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
        jugador["score"] = 0
        jugador.pop("imagen_frente", None)
        jugador.pop("imagen_reverso", None)
        jugador.pop("rect_frente", None)
        jugador.pop("rect_reverso", None)

def info_to_csv (participante:dict):
    """
    Convierte la información de un participante a formato CSV
    - Obtiene el nombre y puntaje del participante
    - Devuelve una cadena con formato "nombre,score"

    Recibe: participante: Diccionario con los datos del participante
    Retorna: Cadena en formato CSV con nombre y puntaje
    """
    nombre = part.get_nombre_participante(participante)
    score = part.get_score_participante(participante)
    return f"{nombre},{score}\n"