import json


escritura = "w"
lectura = "r"
# Por partida, registra cada jugador, y guarda los datos para la partida, en un archivo json
# Si se crea otra partida nueva, los nuevos jugadores pisan a los viejos, dejando solos los nuevos
def registrar_jugador(cant_jug,nombre_archivo):
    jugadores = []
    escritura = "w"

    with open(nombre_archivo, escritura , encoding="utf-8") as archivo:
        for i in range(cant_jug):
            nombre_jug = input(f"Ingrese en nombre del jugador {i + 1} :").strip()

            while nombre_jug == "":
                print("Ingrese un nombre correcto")
                nombre_jug = input(f"Ingrese en nombre del jugador {i + 1} :").strip()
            
            datos_jug = {
                "nombre": nombre_jug,
                "puntaje":  {
                        "Unos" : 0,
                        "Doses" : 0,
                        "Treses": 0,
                        "Cuatros": 0,
                        "Cincos": 0,
                        "Seises": 0,
                        "Escalera": 0,
                        "Full": 0,
                        "Poker": 0,
                        "Generala": 0,
                },
                "puntajeTotal": 0,
            }
            jugadores.append(datos_jug)
        json.dump(jugadores, archivo, indent=4)
    return jugadores

#Se encarga de crear el tablero al principio del juego, justo despues de pedir nombres y antes de que tiren los dados
#Tambien lo guarda en un archivo json para que luego en otra funcion vaya actualizando los puntos 
def creacion_tablero(nombre_archivo_tablero, nombre_archivo_categorias, nombres_archivo_jugadores):

    with open(nombre_archivo_tablero,escritura,encoding="utf-8") as archivo_tablero, \
            open(nombre_archivo_categorias, lectura, encoding="utf-8") as archivo_categorias, \
                open(nombres_archivo_jugadores,lectura,encoding="utf-8") as archivo_jugadores:
                    categorias = json.load(archivo_categorias)
                    nombres_jugadores = json.load(archivo_jugadores)

                    encabezado = "╔" + "═" * 15 + "╦" + ("═" * 15 + "╗") * len(nombres_jugadores)
                    print(encabezado)
                    fila_nombres = "║"
                    fila_separador = "╠"

                    # primer bloque vacío
                    fila_nombres += f"{'':15}║"
                    fila_separador += "═" * 15 + "╬"

                    # columnas para cada jugador
                    for jug in nombres_jugadores:
                            fila_nombres += f"{jug['nombre']:^15}║"
                            fila_separador += "═" * 15 + "╬"

                    # reemplazar último "╬" por "╣"
                    fila_separador = fila_separador[:-1] + "╣"

                    print(fila_nombres)
                    print(fila_separador)
                    
                    # ---- CATEGORÍAS ----
                    for categoria in categorias:
                        nombre_categoria = f"║{categoria['Nombre']:^15}║" + (" " * 7 + f"{int(0)}" + " " * 7+ "║") * len(nombres_jugadores)
                        separador = "╠" + "═" * 15 + "╬" + ("═" * 15 + "╬") * len(nombres_jugadores)
                        print(nombre_categoria)
                        print(separador)
                    
                    # TOTALES
                    fila_total = "║" + f"{'PUNTAJE TOTAL':^15}║"

                    # Cuando tengan puntajes reales, quitar el 0 del ciclo y descomentar lo siguiente
                    for jug in nombres_jugadores:
                        fila_total += f"{jug["puntajeTotal"]:^15}║"

                    pie ="╚" + "═" * 15 + "╩" + ("═" * 15 + "╝") * len(nombres_jugadores)

                    print(fila_total)
                    print(pie)

                    #   Guarda los datos importantes en un json "tablero.json"
                    #   Luego en otra funcion se actualizaran los puntos durante el juego
                    nombres_categorias = []
                    for categoria in categorias:
                        nombres_categorias.append(categoria["Nombre"])

                    puntos_jugs = []
                    for jug in nombres_jugadores:
                        puntos_jugador = jug
                        puntos_jugs.append(puntos_jugador)

                    datos_tablero = [nombres_categorias,puntos_jugs]   
                    json.dump(datos_tablero,archivo_tablero,indent=4)

def leer_tablero(nombre_arch_tablero):
    with open(nombre_arch_tablero,lectura,encoding="utf-8") as arch_tablero:
        tablero = json.load(arch_tablero)
        encabezado = "╔" + "═" * 15 + "╦" + ("═" * 15 + "╗") * len(tablero[1])
        print(encabezado)
        fila_nombres = "║"
        fila_separador = "╠"

        # primer bloque vacío
        fila_nombres += f"{'':15}║"
        fila_separador += "═" * 15 + "╬"

        # columnas para cada jugador
        for jug in tablero[1]:
                fila_nombres += f"{jug['nombre']:^15}║"
                fila_separador += "═" * 15 + "╬"

        # reemplazar último "╬" por "╣"
        fila_separador = fila_separador[:-1] + "╣"

        print(fila_nombres)
        print(fila_separador)

        categorias = list(tablero[1][0]["puntaje"].keys())

        # ---- CATEGORÍAS ----
        for categoria in categorias:
            fila = f"║{categoria:^15}║"
            for jug in tablero[1]:
                punt = jug["puntaje"][categoria]
                fila += f"{punt:^15}║"
            print(fila)

            # separador de categorías
            separador = "╠" + "═" * 15 + "╬" + ("═" * 15 + "╬") * len(tablero[1])
            print(separador)
        # TOTALES
        fila_total = "║" + f"{'PUNTAJE TOTAL':^15}║"

        # Cuando tengan puntajes reales, quitar el 0 del ciclo y descomentar lo siguiente
        for jug in tablero[1]:
            fila_total += f"{jug["puntajeTotal"]:^15}║"

        pie ="╚" + "═" * 15 + "╩" + ("═" * 15 + "╝") * len(tablero[1])

        print(fila_total)
        print(pie)

def actualizar_tablero(nombre_arch_tablero,datos_nuevos):
    with open(nombre_arch_tablero,lectura,encoding="utf-8") as arch_tabl:
        tablero = json.load(arch_tabl)
        print(f"SOY DATOS NUEVOS: \n {datos_nuevos}")
        nombre_buscado = datos_nuevos["nombre"]
        categoria = datos_nuevos["categoria"]
        valor = datos_nuevos["valor"]

        jugadores = tablero[1]

        for jug in jugadores:
            if  jug["nombre"] == nombre_buscado:
                #Actualiza puntaje
                jug["puntaje"][categoria] = valor

                #Actualiza el puntaje total
                jug["puntajeTotal"] = sum(jug["puntaje"].values())
                break
        else:
            print("El jugador " + nombre_buscado + " no existe")
            return
        
        # Guardar cambios
    with open(nombre_arch_tablero, "w", encoding="utf-8") as arch:
        json.dump(tablero, arch, indent=4, ensure_ascii=False)