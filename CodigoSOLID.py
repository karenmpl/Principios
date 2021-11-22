#DATOS DE ENTRADA
ANIMAL= int(input("¿De cual animal quiere conocer la caracteristicas? 1.Leon 2.Ballena 3.Tucan? "))

class Animal:
    def __init__(self, ANIMAL):
        self.ANIMAL = ANIMAL

    def acciones_comun():
        comun = "Comer"
        return comun

    def sentido_vista():
        vista = "Puede ver"
        return vista

class Animal_Tierra:
    def acciones_Tierra():
        Tierra = "camina en cuatro patas"
        return Tierra

class Animal_Agua:
    def acciones_Agua():
        return "Nada bajo el agua"

class Animal_Aire (Animal):
    def acciones_Aire():
        return "Vuela"


class Leon (Animal, Animal_Tierra):
    def llamar():
        caracteristicas = ()
        return caracteristicas


class Ballena(Animal, Animal_Agua):
    def llamar():
        caracteristicas = ()
        return caracteristicas


class Tucan(Animal, Animal_Aire):
    def llamar():
        caracteristicas = ()
        return caracteristicas

if ANIMAL == 1 :
    print ("debe imprimir las caracteristicas del leon, el leon es clase hija de animal y debe agragar animal_tierra" )
elif ANIMAL == 2 :
    print ("lo mismo que el leon, pero con la ballena")
elif ANIMAL == 3 :
    print("Lo mismo pero con el tucan")