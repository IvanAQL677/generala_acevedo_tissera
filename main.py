# import jorjojyyojy as j

import modulos.juego_estado as juego

mensaje_info = "===========\nGENERALA\n=========== \nOpciones: \n\t1) Jugar \n\t2)Estadisticas \n\t3)Creditos \n\t4)Crear archivos json \n\t5) Salir"
juegos_finalizados = 0

while True:
    print(mensaje_info)
    opcion = int(input('Su opcion: '))
        
    if opcion == 1: 
        juego.comenzar_ronda()
        juegos_finalizados += 1
    elif opcion == 2:
        print(f'Jugo {juegos_finalizados} juegos')
    elif opcion == 3:
        print(f'Codigo por: \n\tLucas Tissera \n\tAcevedo')
    elif opcion == 4:
        juego.jason.iniciar_json()
    elif opcion == 5:
        print('Gracias por jugar')
        break
    else:
        print('Opcion no valida')