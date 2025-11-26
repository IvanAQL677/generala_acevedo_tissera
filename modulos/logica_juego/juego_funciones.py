import random
import json
import os
import time

# Comentar este import si se va a usar alguna funcion de manera directa, sobre este archivo
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


# Funcion que solo funciona para printear dados que vayan tirando durante el juego
def print_dados(dados):
    for i in dados:
        print(f"┌───┐", end="  ")
    print()
    for i in dados:
        print(f"│ {i} │", end="  ")
    #comentar este print para que se vea bien el total al la derecha
    print()
    #print(f' = {total} TOTAL')
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
    print("<<<<<<------ Tiren los dados para decidir quien sera el que comienze el juego. ------>>>>>>")
    #   Ciclo para que cada jugador tire un dado y quede guardado su nombre y dado
    for jug in list_jug:
        tirada = input(f"Turno de {jug["nombre"]}. Presione enter para tirar los dados.")
        time.sleep(1)
        # Hacer evento para tocar enter y tirar los dados
        dado = random.randint(1,6)
        datos_jug = {
            "nombre" : jug["nombre"],
            "dado" : dado
        }
        info_jugadores.append(datos_jug)
        print_dados([dado])
        print()
    
    # Si no hay repetidos, saltea el condicional
    valores = [j["dado"] for j in info_jugadores]
    if len(valores) == len(set(valores)):
        pass # no hay empate
    else:
        #   Envia solo los dados en empate y no todos los dados
        maximo = max(j["dado"] for j in info_jugadores)
        empatados = [j for j in info_jugadores if j["dado"] == maximo]
        v.resolver_empates(empatados)

    #   Ciclo para leer los dados y captar al jugador que tiro mejor
    for jug in info_jugadores:
        if jug["dado"] > dado_ganador:
            dado_ganador = jug["dado"]
            ganador = jug

    # Ordena los jugadores de mayor a menor puntuacion de dado, listo para comenzar el primer turno
    info_jugadores.sort(key=lambda j: j["dado"],reverse=True)
    print("< < < < < < - - - - - - - - - - - - - - - - > > > > > >")
    print(f"      El jugador {ganador["nombre"]} gano la ronda!. Comenzara primero")
    print("< < < < < < - - - - - - - - - - - - - - - - > > > > > >")

    return info_jugadores


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

def elegir_conservados(dados):

    eleccion = input("Ingrese las posiciones de los dados que desea conservar.(separados por espacios)")

    if eleccion.strip() == "":
        return [] # No conservo ninguno
    
    indices = [int(x) - 1 for x in eleccion.split()]
    return indices

def aplicar_conservados_y_tirar(dados_actuales, indices_conservados):
    """
    dados_actuales: lista de 5 valores
    indices_conservados: lista de índices (base 0) que se conservan
    Devuelve la lista resultante (misma longitud), donde los no conservados
    han sido re-tirados.
    """
    n = len(dados_actuales)
    # cuántos hay que tirar
    faltan = [i for i in range(n) if i not in indices_conservados]
    nuevos = tirar_dados(len(faltan))

    resultado = dados_actuales.copy()
    for idx_pos, pos in enumerate(faltan):
        resultado[pos] = nuevos[idx_pos]
    return resultado


def tirar_dados(n):
        return [random.randint(1, 6) for _ in range(n)]

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

# Funcion central para determinar el ganador de la partida
# Se encarga de los turnos de todos los jugadores a traves de un ciclo
def turno_jugadores(list_jug):

    for ronda in range(1,11):
        print(f"Ronda {ronda}")
        for jugador in list_jug:
            #   Muestra que es el turno del jugador
            #print("< < < < - - - - - - - - - - - - - - - - > > > >")
            print(f"\t\tTurno de {jugador["nombre"]}")
            #print("< < < < - - - - - - - - - - - - - - - - > > > >")
            
            # PRIMER TIRO
            input("Presione enter para el tiro 1")
            time.sleep(2)
            dados = tirar_dados(5)
            print("Primer Tiro:")
            print_dados(dados)

            #elige los dados que conservara por su posicion
            conservados = elegir_conservados(dados)

            # SEGUNDO TIRO
            input("Presione enter para el tiro 2")
            time.sleep(2)
            dados = aplicar_conservados_y_tirar(dados, conservados)
            print("Segundo Tiro:")
            print_dados(dados)

            conservados = elegir_conservados(dados)

            # ===== TERCER TIRO =====
            input("Presione enter para el tiro 3")
            time.sleep(2)
            dados = aplicar_conservados_y_tirar(dados, conservados)
            print("Tercer tiro:")
            print_dados(dados)

            #   1° Tirar los 5 dados y mostrarlos en consola
            #   Mostrar tablero
            #   Consultar en un input cuales posiciones de dados va a elegir quedarse
            #   
            #   Muestra que es el segundo tiro
            #   Input para presionar enter  
            #   2° Tirar los dados restantes a los que conservo
            #   Mostrar tablero
            #   Volver a consultar cuales conservara
            #  
            #   Muestra que es el tercer tiro
            #   Input para presionar enter
            #   Mostrar tablero
            #   3° Tirar los dados restantes a los que conservo

            #   evaluar los dados, con las jugadas posibles
            #   Mostrar tablero
            #   consultar que anotara el jugador
            #   guardarlo los datos y actualizar

            #   fin de turno jugador 
            

# Prueba practica hasta que funcione 

'''
turno_jugadores([{
    "nombre" : "Lucas"
},{
    "nombre" : "Juan"
}])
'''

'''
tirada = tirar_dados(5)
print(tirada)


# 2) Elegir conservados
conservados = elegir_conservados(tirada)

print(conservados)
'''