# import jorjojyyojy as j

mensaje_info = "===========\nGENERALREA\n=========== \nOpciones: \n\t1) Jugar \n\t2)Estadisticas \n\t3)Creditos \n\t4) Salir"
juegos_finalizados = 0

while True:
    print(mensaje_info)
    try:
        opcion = int(input('Su opcion: '))
    except ValueError:
        print('Error: Opcion no es un numero entero. Intente una opcion valida.')
        continue
    
    if opcion == 1:
        print('Esta jugando')
        juegos_finalizados += 1
    elif opcion == 2:
        print(f'Jugo {juegos_finalizados} juegos')
    elif opcion == 3:
        print(f'Codigo por: \n\tLucas Tissera \n\tAcevedo')
    elif 4:
        print('Gracias por jugar')
        break
    else:
        print('Opcion no valida')