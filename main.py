import modulos.juego_estado as juego
import modulos.datos.registrar_jug_en_partida as r

url_tablero = "./json/tablero.json"
url_categorias = "./json/categorias.json"
list = [{"nombre": "Lucas"},{"nombre": "Juan"},{"nombre": "Cris"}]

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
                        
6) opcion de prueba                        
                        """
                        )
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
        r.creacion_tablero(url_tablero,url_categorias,list)
    else:
        print('Opcion no valida')