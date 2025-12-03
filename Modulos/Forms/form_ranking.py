import Modulos.Forms.form_base as form_base
from utn_fra.pygame_widgets import Label, Button
import Modulos.variables as var
import Modulos.auxiliares as aux


def create_form_ranking (form_dict_data: dict) -> dict:
    """
    Crea y configura el formulario de ranking del juego: muestra la tabla de posiciones con los puntajes de los jugadores
    
    Recibe: form_dict_data: Diccionario con la configuración inicial del formulario

    Retorna: Diccionario que representa el formulario de ranking
    """
    form = form_base.create_base_form(form_dict_data)
    form["label_titulo"] = Label(x=500, y=100, text= "RANKING", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=50, color=(255, 192, 223))
    form["lista_ranking_file"] = []
    form["lista_ranking_GUI"] = []
    form["button_volver"] = Button(x=100, y=750, text="VOLVER", screen=form.get("screen"),font_path=var.FUENTE_PRINCIPAL, font_size=30, on_click=cambiar_pantalla_ranking, on_click_param=["form_menu", form])
    form["data_cargada"] = False
    form["label_rank"] = Label(x=300, y=150, text= "RANK", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(255, 192, 223))
    form["label_nombre"] = Label(x=500, y=150, text= "JUGADOR", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(255, 192, 223))
    form["label_score"] = Label(x=700, y=150, text= "SCORE", screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=(255, 192, 223))
    
    
    form["widgets_list"] = [form.get("label_titulo"), form.get("button_volver"), form.get("label_rank"), form.get("label_nombre"), form.get("label_score")]

    var.dict_forms_status[form.get("name")] = form

    return form

def draw (form_dict_data: dict):
    """
    Renderiza la superficie de fondo, los widgets principales y la lista
    de posiciones del ranking

    Recibe: form_dict_data: Diccionario del formulario de ranking
    """

    form_base.draw(form_dict_data)
    form_base.dibujar_widgets(form_dict_data)
    
    for widget in form_dict_data.get("lista_ranking_GUI"):
        widget.draw()

def update (form_dict_data: dict):
    """
    Actualiza el estado del formulario de ranking
    - Inicializa los datos del archivo de ranking si aún no se cargaron
    - Actualiza los widgets del formulario

    Recibe: form_dict_data: Diccionario del formulario de ranking
    """
    inicializar_archivo_ranking(form_dict_data)
    form_base.update(form_dict_data)

def cambiar_pantalla_ranking (parametros: list):
    """
    Cambia la pantalla activa desde el formulario de ranking a otro formulario.
    - Limpia los datos cargados del ranking.
    - Desactiva el formulario de ranking.
    - Activa el formulario indicado.

    Recibe: parametros: Lista con dos elementos:
                       [0] nombre del formulario al que se desea cambiar.
                       [1] diccionario del formulario de ranking actual.
    """
    form_ranking = parametros[1]
    form_a_cambiar = parametros[0]
    form_ranking["data_cargada"] = False
    form_ranking["lista_ranking_GUI"] = []
    form_ranking["lista_ranking_file"] = []
    form_ranking["active"] = False
    aux.activar_form_a_cambiar(form_a_cambiar)

def inicializar_archivo_ranking (form_dict_data: dict):
    """
    Inicializa los datos del archivo de ranking si aún no se cargaron.
    - Carga los datos desde archivo mediante aux.cargar_ranking.
    - Genera los widgets de la tabla de posiciones.
    - Marca el estado 'data_cargada' como True.

    Recibe: form_dict_data: Diccionario del formulario de ranking.
    """
    if not form_dict_data.get("data_cargada"):
        form_dict_data["lista_ranking_file"] = aux.cargar_ranking(10)
        init_ranking_data(form_dict_data)
        form_dict_data["data_cargada"] = True

def init_ranking_data (form_dict_data: dict):
    """
    Genera los widgets gráficos para mostrar la tabla de posiciones.
    - Recorre la matriz de datos del ranking.
    - Crea etiquetas para posición, nombre y puntaje.
    - Aplica un color especial a los tres primeros lugares.
    - Agrega los widgets a la lista 'lista_ranking_GUI'.

    Recibe: form_dict_data: Diccionario del formulario de ranking
    """
    matriz = form_dict_data.get("lista_ranking_file")
    coord_y = 200
    for indice_fila in range(len(matriz)):
        fila = matriz[indice_fila]
        rank = indice_fila + 1
        color_texto = (255, 192, 223)

        if rank > 0 and rank <= 3:
            color_texto = (239, 184, 16)

        posicion = Label(x= 300, y= coord_y, text= f"{rank}",  screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=color_texto)
        nombre = Label(x= 500, y= coord_y, text= f"{fila[0]}",  screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=color_texto)
        score = Label(x= 700, y= coord_y, text= f"{fila[1]}",  screen=form_dict_data.get("screen"), font_path=var.FUENTE_PRINCIPAL, font_size=30, color=color_texto)

        coord_y += 50

        form_dict_data["lista_ranking_GUI"].append(posicion)
        form_dict_data["lista_ranking_GUI"].append(nombre)
        form_dict_data["lista_ranking_GUI"].append(score)