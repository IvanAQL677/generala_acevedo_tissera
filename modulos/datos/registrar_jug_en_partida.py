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
                "puntaje": 0,
                "puntaje total": 0,
            }
            jugadores.append(datos_jug)
        json.dump(jugadores, archivo, indent=4)
    return jugadores