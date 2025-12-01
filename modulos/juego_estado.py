#import modulos.json_funciones as jason
import modulos.logica_juego.juego_funciones as j

def comenzar_juego():
    rondas = 1
    categorias = j.cargar_categorias()
    lista_jug_ordenada = j.principio_juego()
    for i in range(len(categorias)):
            j.turno_jugadores(rondas, lista_jug_ordenada["list_jug_ord"], categorias, lista_jug_ordenada["jugadores"])
            rondas += 1
