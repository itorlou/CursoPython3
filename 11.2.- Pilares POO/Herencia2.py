#vamos a ver qué tipo de errores puede dar el uso de herencia, hay algunos métodos que no se van a heredar correctamente

class Animales():
    def __init__(self, nombre):
        self.nombre=nombre
    
class Perro(Animales):
    def __init__(self,nombre, sonido):
        super().__init__(nombre) #usamos la palabra reservada super para heredar el atributo del __init__ de la clase padre
        self._sonido=sonido

    @property
    def sonido(self):
        return self._sonido
    
perro = Perro("Firulais","Guau")

print(perro.nombre)
print(perro.sonido)