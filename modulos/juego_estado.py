#import modulos.json_funciones as jason
import modulos.logica_juego.juego_funciones as j

def comenzar_juego():
    rondas = 1
    categorias = j.cargar_categorias()
    lista_jug_ordenada = j.principio_juego()
    for i in range(len(categorias)):
            j.turno_jugadores(rondas, lista_jug_ordenada, categorias)
            rondas += 1
