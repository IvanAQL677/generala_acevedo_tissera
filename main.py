
juegos_finalizados = 0

while True:
    mensaje_info =print("""
================
    GENERALA
================
Opciones: 
1)Jugar. 
2)Estadisticas. 
3)Creditos. 
4)Crear archivos json. 
5) Salir""")
    opcion = int(input('Su opcion: '))
        
    if opcion == 1: 
        import modulos.juego_estado as juego
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