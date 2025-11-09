import random

def turno():
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