import modulos.juego_funciones as fun
import modulos.json_funciones as jason

def comenzar_ronda():
    turno_contador = 1

    dados_conservados = [0] * 6

    print('EMPIEZA !')

    turno_jugador = fun.decidir_orden()

    if turno_jugador:
        #fun.tirar_dados()

        print('a')
    else:
        print('a')
