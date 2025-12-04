#import modulos.json_funciones as jason
import modulos.logica_juego.juego_funciones as j

def comenzar_juego():
        rondas = 1
        ganador = dict()
        categorias = j.cargar_categorias()
        lista_jug_ordenada = j.principio_juego()
        for i in range(len(categorias) - 1):
                ganador = j.turno_jugadores(rondas, lista_jug_ordenada, categorias)
                rondas += 1

        print("< < < < - - - - - - - - - - - - - - - - > > > >")
        print(f"\t \t JUEGO FINALIZADO")
        print("< < < < - - - - - - - - - - - - - - - - > > > >")
        print(f"\t    Gano {ganador["nombre"]}, con un total de {ganador["puntajeTotal"]} puntos.\n \t     Felicitaciones ! ! ! ")
        print("< < < < - - - - - - - - - - - - - - - - > > > >")


