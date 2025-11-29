import modulos.juego_estado as juego
import modulos.datos.datos_funciones as r


url_tablero = "./json/tablero.json"
datos_nuevos = {
    "nombre" : "C",
    "categoria": "Treses",
    "valor": 15
}


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
5) Salir
                        
6) boton de prueba
                        """)
    opcion = int(input('Su opcion: '))
        
    if opcion == 1: 
        juego.comenzar_juego()
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
    elif opcion == 6:
        r.actualizar_tablero(url_tablero,datos_nuevos)
        r.leer_tablero(url_tablero)
    else:
        print('Opcion no valida')