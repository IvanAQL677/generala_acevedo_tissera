import random
import json
import os
import time
import modulos.validaciones.valids as v

def cargar_categorias():
    if not os.path.exists('json/categorias.json'):
        return [] 
    with open('json/categorias.json', 'r', encoding="utf-8")  as info:
        categorias_lista = json.load(info)
        for key, value in categorias_lista.items():
            name = value.get("nombre")
            sum_type = value.get("tipo de suma")
            default_score = value.get("puntaje default")
            
            print(f"{key}: name={name}, sum_type={sum_type}, default_score={default_score}")
        return categorias_lista

def print_dados(dados, total):
    for i in dados:
        print(f"┌───┐", end="  ")
    print()
    for i in dados:
        print(f"│ {i} │", end="  ")

    print(f' = {total} TOTAL')

    for i in dados:
        print(f"└───┘", end="  ")
    print()


def decidir_orden(list_jug):
    # cada jugador tira un dado y se guardan en un diccionario, dentro de una lista
    # se evaluan los valores de cada dado y el mayor numero sera el primero
    # se muestra quien gano y comienza a tirar los dados
    info_jugadores = []
    dado_ganador = 0
    ganador = {}

    #   Ciclo para que cada jugador tire un dado y quede guardado su nombre y dado
    for jug in list_jug:
        tirada = input(f"Turno de {jug["nombre"]}.Presione enter para tirar los dados.")
        time.sleep(1)
        # Hacer evento para tocar enter y tirar los dados
        dado = random.randint(1,6)
        datos_jug = {
            "nombre" : jug["nombre"],
            "dado" : 1
        }
        info_jugadores.append(datos_jug)
    
    v.resolver_empates(info_jugadores)

    #   Ciclo para leer los dados y captar al jugador que tiro mejor
    for jug in info_jugadores:
        if jug["dado"] > dado_ganador:
            dado_ganador = jug["dado"]
            ganador = jug

        print("dados ordenados al final")
        print(info_jugadores)
        print(ganador)
        print(f"El jugador {ganador["nombre"]} gano la ronda!. Comenzara primero")

'''
    print('Tira los dados para decidir quien va primero! El que tenga la suma mas grande comienza!')
    while True:
        lanzar = input('Lanza los dados con enter!')
        oponente_tiro = []
        jugador_tiro = []
        oponente_resultado = 0
        jugador_resultado = 0
        
        for i in range(5):
            oponente_tiro.append(random.randint(1, 6))
            jugador_tiro.append(random.randint(1, 6))

        for i in range(5):
            oponente_resultado += oponente_tiro[i-1]
            jugador_resultado += jugador_tiro[i-1]

        print('################/RESULTADOS/################')
        print('#### Jugador: ')
        print_dados(jugador_tiro, jugador_resultado)
        print('Oponente esta tirando...')
        time.sleep(2)

        
        print('#### Oponente: ')
        print_dados(oponente_tiro, oponente_resultado)
        time.sleep(2)

        
        if oponente_resultado > jugador_resultado:
            print('Comienza el oponente!')
            return False
        elif oponente_resultado < jugador_resultado:
            print('Comienza el jugador!')
            return True
        else:
            print('Empate. (Que suerte! O no) Tiren de nuevo.')
        time.sleep(2)

'''


def tirar_dados(conservados):
    lanzar = input('Lanza los dados con Enter!')
    resultados = []
    for i in range(5):
        if conservados[i]:
            resultados[i] = 0
            continue
        resultados[i] = random.randint(1, 6)
    return resultados


def tirar_dados_viejo(): # creo que tendria que rehacerse este

    resultados_final = [0] * 5
    resultados_conservar = [False] * 5

    for i in range(3):
        lanzar = input('Lanza los dados con Enter!')
        resultados = [0] * 5

        # se saltea las posiciones que se hayan guardado y se genera un numero entre 1 y 6
        # se copia los que se hayan guardado a resultado[] para que el print no se tenga que complicar
        for j in range(5):
            if resultados_conservar[j]: 
                resultados[j] = resultados_final[j]
                continue
            resultados[j] = random.randint(1, 6)
        
        print(f'<<< TURNO JUGADOR - TIRO {i+1} DE 3 >>>')
        print('----------------------')
        print(f'----DADOS ACTUALES----')
        print(f'\tPosicion: (1\t)|(2\t)|(3\t)|(4\t)|(5\t)')
        print(f'\tSimbolo: PLACEHOLDER AAAAAH')
        print(f'\tValor:   {resultados[0]}\t|  {resultados[1]}\t|  {resultados[2]}\t|  {resultados[3]}\t|  {resultados[4]}')

        # valor para elegir si saltear o no
        # se usa .strip para sacar los espacios
        guardar = input('Elija los numeros a conservar (separados por comas, ejemplo: 1, 3, 5): ')
        for j in guardar.split(','):
            item = j.strip()
            if item.isdigit():
                item = int(item)
                if item > 0 and item < 6:
                    resultados_conservar[item-1] = True
                    if resultados_final[item-1] == 0:
                        resultados_final[item-1] = resultados[item-1]
        
        todos_conservados = True
        for j in resultados_conservar:
            if not j:
                todos_conservados = False
                break
        if todos_conservados: break
    return resultados_final

'''
lista = [
    {
        "nombre": "Lucas",
        "puntaje": 0,
        "puntaje total": 0
    },
    {
        "nombre": "Eze",
        "puntaje": 0,
        "puntaje total": 0
    },
    {
        "nombre": "Jave",
        "puntaje": 0,
        "puntaje total": 0
    }
]
'''
#decidir_orden(lista)