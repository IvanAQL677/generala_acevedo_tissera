#import modulos.json_funciones as jason
import modulos.logica_juego.juego_funciones as j
import modulos.validaciones.valids as v
import modulos.datos.registrar_jug_en_partida as r

nombre_archivo_jugadores = "./json/jugadores.json"

def principio_juego():
    #   comienza la ronda
    #   se piden los jugadores que desean jugar
    cant_jugadores = v.validar_cant_jugadores_es_digito_y_entero()
    
    #   se pide el nombre de cada jugador
    jugadores = r.registrar_jugador(cant_jugadores,nombre_archivo_jugadores)
    #   una vez ingresen los nombres, cada uno se guarda en un diccionario

    #   una vez guarda los nombres de cada jugador, comienza a tirar cada uno un dado
    lista_jug_ordenadas = j.decidir_orden(jugadores)
    return lista_jug_ordenadas


def comenzar_juego():
    categorias = j.cargar_categorias()
    turno_contador = 1
    dados_conservados = [0] * 6

    #   el que saca mayor puntuacion es el que comienza primero
    #   se ordenan los jugadores para la ronda y comienza el jugador con mas puntuacion de dado
    lista_jug_ordenada = principio_juego()
    rondas = 1

    for i in range(len(categorias)):
            j.turno_jugadores(rondas, lista_jug_ordenada, categorias)
            rondas += 1

    print('EMPIEZA !')
