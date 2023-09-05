# Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno


class Fabrica():
    def __init__(self,llantas,color,precio):
        self._llantas=llantas
        self._color=color
        self._precio=precio

    @property
    def llantas(self):
        return self._llantas
    
    @property
    def color(self):
        return self._color
    
    @property
    def precio(self):
        return self._precio
    
class Coche(Fabrica):
    def descripcion(self):
        print("El coche tiene {} llantas, Es de Color {}, el precio es de {}.".format(self._llantas, self._color, self._precio))

class Moto(Fabrica):
    def descripcion(self):
        print("La moto tiene {} llantas, Es de Color {}, el precio es de {}.".format(self._llantas, self._color, self._precio))

coche=Coche(4,"Azul","15000")

moto=Moto(2,"Verde","4000")

coche.descripcion()
moto.descripcion()