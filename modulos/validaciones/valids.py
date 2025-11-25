import random


# Valida si es un numero
def validar_numero(texto):
    return texto.isdigit()


# Valida texto vacio
# Valida si la estadistica esta vacia
# Valida si es positivo


# Valida que la cantidad de jugadores sea un numero y no un caracter
# Tambien verifica que el numero sea 1,2,3 o 4 , por los jugadores
def validar_cant_jugadores_es_digito_y_entero() -> int:
    jug = input("Numero de jugadores(maximo de 4 jugadores): ").strip()
    while not validar_numero(jug) or not (1 <= int(jug) <= 4):
        print("Ingrese un numero entero valido entre el 1 y el 4.")
        jug = input("Numero de jugadores(maximo de 4 jugadores): ").strip()

    # Una vez la supera al while, retorna la cantidad de jugadores
    jug = int(jug)
    print(f"Cantidad de jugadores valida: {jug}")
    return jug


# Valida que no hay empates en la etapa de quien empieza primero
def resolver_empates(dados_jugadores):
    # Mientras haya dados repetidos, seguir intentando
    while True:
        # obtengo todos los valores de dado
        valores = [j["dado"] for j in dados_jugadores]

        # si NO hay repetidos, listo
        if len(valores) == len(set(valores)):
            return dados_jugadores   # no hay empate

        # si hay repetidos, re-tiro para los que empataron
        for i in range(len(dados_jugadores)):
            for j in range(i + 1, len(dados_jugadores)):
                if dados_jugadores[i]["dado"] == dados_jugadores[j]["dado"]:
                    # empate → ambos vuelven a tirar
                    print(f"Tira el jugador {dados_jugadores[i]["nombre"]}")
                    dados_jugadores[i]["dado"] = random.randint(1, 6)
                    print(f"Tira el jugador {dados_jugadores[j]["nombre"]}")
                    dados_jugadores[j]["dado"] = random.randint(1, 6)