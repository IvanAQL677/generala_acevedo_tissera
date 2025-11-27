import json

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
                "puntos":  {
                        "unos" : 0,
                        "doses" : 0,
                        "Treses": 0,
                        "cuatros": 0,
                        "cincos": 0,
                        "seises": 0,
                        "escalera": 0,
                        "full": 0,
                        "poker": 0,
                        "generala": 0,
                },
                "puntaje total": 0,
            }
            jugadores.append(datos_jug)
        json.dump(jugadores, archivo, indent=4)
    return jugadores


#Se encarga de crear el tablero al principio del juego, justo despues de pedir nombres y antes de que tiren los dados
#Tambien lo guarda en un archivo json para que luego en otra funcion vaya actualizando los puntos 
# funciona pero solo imprime hasta ahora, falta guardar en un archivo json
def creacion_tablero(nombre_archivo_tablero, nombre_archivo_categorias, nombres_jugadores):
    escritura = "w"
    lectura = "r"

    with open(nombre_archivo_tablero,escritura,encoding="utf-8") as archivo_tablero, \
            open(nombre_archivo_categorias, lectura, encoding="utf-8") as archivo_categorias:
                categorias = json.load(archivo_categorias)
                
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
                    fila_total += "0" #f"{str(puntajes[jug['nombre']]):^15}║"

                pie ="╚" + "═" * 15 + "╩" + ("═" * 15 + "╝") * len(nombres_jugadores)

                print(fila_total)
                print(pie)
            
            # Faltaria guardar los datos importantes en un json "tablero.json"
            # Luego en otra funcion se actualizaran los puntos durante el juego