# heredar, métodos de clase padre que pasen a la clase hija

class Animales():
    def habla(self):
        print("Yo soy un animal")

    def descripcion(self):
        print("Yo soy un {}".format(self.animal)) # type: ignore

class Perro(Animales): #así todos los métodos de "Animales" están en la clase "Perro"
    pass

class Abeja(Animales):
    def __init__(self,animal):
        self.animal=animal

animal = Animales()

animal.habla()
 

perro = Perro()

perro.habla()

abeja = Abeja("Abeja") #iniciamos el objeto abeja con el constructor pasándole el valor de Abeja

abeja.descripcion() #podemos ver cómo se pasa este parámetro de la clase hija a la clase padre