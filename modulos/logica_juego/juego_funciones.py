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
        input(f"Turno de {jug["nombre"]}. Presione enter para tirar los dados.")
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
    if len(valores) != len(set(valores)):
        #   Envia solo los dados en empate con el mayor numero de todos
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

def elegir_conservados(dados):
    eleccion = input("Ingrese las posiciones de los dados que desea conservar.(separados por espacios)")
    if eleccion.strip() == "":
        return [] # No conservo ninguno
    indices = [int(x) - 1 for x in eleccion.split()]
    return indices

def aplicar_conservados_y_tirar(dados_actuales, indices_conservados):
    #   dados_actuales: lista de 5 valores
    #   indices_conservados: lista de índices (base 0) que se conservan
    #   Devuelve la lista resultante (misma longitud), donde los no conservados
    #   han sido re-tirados.
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

# Funcion central para determinar el ganador de la partida
# Se encarga de los turnos de todos los jugadores a traves de un ciclo
def turno_jugadores(rondas, list_jug, categorias):
    print(f"Ronda {rondas}")
    for jugador in list_jug:
        #   Muestra que es el turno del jugador
        print("< < < < - - - - - - - - - - - - - - - - > > > >")
        print(f"\t\tTurno de {jugador["nombre"]}")
        print("< < < < - - - - - - - - - - - - - - - - > > > >")

        # ===== PRIMER TIRO =====
        input("Presione enter para el tiro 1")
        time.sleep(2)
        dados = tirar_dados(5)
        print("Primer Tiro:")
        print_dados(dados)

        #   Mostrar tablero



        #elige los dados que conservara por su posicion
        conservados = elegir_conservados(dados)

        # ===== SEGUNDO TIRO =====
        input("Presione enter para el tiro 2")
        time.sleep(2)
        dados = aplicar_conservados_y_tirar(dados, conservados)
        print("Segundo Tiro:")
        print_dados(dados)

        #   Mostrar tablero
        
        
        
        conservados = elegir_conservados(dados)

        # ===== TERCER TIRO =====
        input("Presione enter para el tiro 3")
        time.sleep(2)
        dados = aplicar_conservados_y_tirar(dados, conservados)
        print("Tercer tiro:")
        print_dados(dados)

        #   Mostrar tablero
        


        
        #   Mostrar tablero

        tabla_puntajes = puntajes_disponibles(dados, categorias)

        print('---------Tabla de puntajes!--------')
        for i in range(len(categorias)):
            print(f'-- {i+1}. {categorias[i]['Nombre']}: {tabla_puntajes[i]}')

        puntos = elegir_categoria(tabla_puntajes, categorias) # cambia esto despues con un verdadero modelo para los puntos asi se aplica bien


def puntajes_disponibles(dados, categorias):
    resultados = [0] * len(categorias)

    for i in range(len(categorias)):
        categoria = categorias[i]
        if categoria["Tipo"] == 'suma':
            # las sumas. se itera por todos los dados y si el requerimiento es un digito (para no crashear) y el dado es igual al requerimiento, se suma al resultado
            resultado_suma = 0
            for j in dados:
                if categoria["Requerimiento"].isdigit() and j == int(categoria["Requerimiento"]):
                    resultado_suma += j
            resultados[i] = resultado_suma
        
        elif categoria["Tipo"] == 'estatico' and categoria["Puntaje"].isdigit():
            # Secuencia. se ordenan los dados de menor a mayor (salteando el primero)
            # si uno NO es 1 mayor que el anterior, se pone es_secuencia = false y queda como 0
            if categoria["Requerimiento"] == 'secuencia':
                valores_ordenados = sorted(dados)
                es_secuencia = True
                for j in range(1, len(valores_ordenados)):
                    if valores_ordenados[j] != valores_ordenados[j-1] + 1:
                        es_secuencia = False
                        break
                if es_secuencia:
                    resultados[i] = int(categoria["Puntaje"])
                else:
                    resultados[i] = 0

            elif categoria["Requerimiento"] == '2 y 3' or categoria["Requerimiento"] == '4 y 1':
                # se ordena y se hace un diccionario 'conteos' donde se añade cada numero nuevo. si no esta en conteos se lo añade, y si ya esta se le suma 1 a la cantidad 
                conteos = {}
                for j in dados:
                    if j in conteos:
                        conteos[j] += 1
                    else:
                        conteos[j] = 1
                # se itera por cada valor en conteos para ver si tiene la cantidad
                hay_3 = False
                hay_2 = False
                hay_4 = False
                for j in conteos.values():
                    if j == 3:
                        hay_3 = True
                    elif j == 2:
                        hay_2 =  True
                    elif j == 4:
                        hay_4 = True
                
                # condicionales para añadir el puntaje o no
                if categoria["Requerimiento"] == '2 y 3':
                    if hay_3 and hay_2:
                        resultados[i] = int(categoria["Puntaje"])
                    else:
                        resultados[i] = 0
                elif categoria["Requerimiento"] == '4 y 1':
                    if hay_4:
                        resultados[i] = int(categoria["Puntaje"])
                    else:
                        resultados[i] = 0

            # si se encuentra uno diferente se pone como falso
            elif categoria["Requerimiento"] == 'todos':
                todos_iguales = True
                for j in range(1, len(dados)):
                    if dados[j] != dados[j-1]:
                        todos_iguales = False
                        break
                if todos_iguales:
                    resultados[i] = int(categoria["Puntaje"])
                else:
                    resultados[i] = 0
            
    return resultados

def elegir_categoria(puntajes, categorias) -> int:
    # se ingresa una eleccion. despues se fija si es un numero valido y sel regresa con el index correcto
    while True:
        eleccion = input('Elija una categoria (Puede ser su numero o su nombre): ')
        if eleccion.isdigit() and 0 < int(eleccion) <= len(categorias):
            index = int(eleccion)-1
            print(f'Elegiste la categoria {eleccion}. {categorias[index]["Nombre"]}')

            return int(puntajes[index])
        else:
            for i in range(len(categorias)):
                if categorias[i]["Nombre"].lower() == eleccion.lower():
                    print(f'Elegiste la categoria {i+1}. {categorias[i]}')
                    return int(puntajes[i])
        print('Error, opcion invalida o no encontrada.')