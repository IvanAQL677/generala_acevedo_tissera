#import modulos.json_funciones as jason
import modulos.logica_juego.juego_funciones as j
import modulos.validaciones.valids as v
import modulos.datos.registrar_jug_en_partida as r

nombre_archivo_jugadores = "./json/jugadores.json"


def comenzar_ronda():
    turno_contador = 1

    dados_conservados = [0] * 6

    #   comienza la ronda
    #   se piden los jugadores que desean jugar
    cant_jugadores = v.validar_cant_jugadores_es_digito_y_entero()
    
    #   se pide el nombre de cada jugador
    jugadores = r.registrar_jugador(cant_jugadores,nombre_archivo_jugadores)
    #   una vez ingresen los nombres, cada uno se guarda en un diccionario
    print(jugadores)

    #   una vez guarda los nombres de cada jugador, comienza a tirar cada uno un dado
    j.decidir_orden(jugadores)

    #   el que saca mayor puntuacion es el que comienza primero
    #   se ordenan los jugadores para la ronda y comienza el jugador 1

    #   Tiro 1
    #   *loop*
    #   verificar si hay dados conservados y restarlos del total de dados 
    #   tirar los dados restantes
    #   guardar los dados en una lista y mostrar al usuario
    #   preguntar que posicion de dado quiere guardar y mostrar la Tabla de puntos
    #   validar que lo que elija el jugador este libre para anotar   
    #   guarda los dados conservados y los retorna
    #   *loop*

    #   Tiro 2
    #   lo mismo que el tiro 1
    #   Tiro 3
    #   lo mismo que el tiro 1

    #   al finalizar los tiros, mostrar la tabla y las opciones de anotacion
    #   preguntar al jugador que desea anotar en base a las opciones que le han tocado
    #   se guarda la opcion, se actualiza en la tabla y se guarda 

    print('EMPIEZA !')

#    

#    if turno_jugador:
        #fun.tirar_dados()

#        print('a')
#    else:
#        print('a')

comenzar_ronda()
