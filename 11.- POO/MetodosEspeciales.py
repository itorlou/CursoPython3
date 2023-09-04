class FabricaCoches():
    def __init__(self,marca,color):
        self.marca=marca
        self.color=color
        print("El objeto {} ha sido creado".format(self.marca))


    # clase por defecto del lenguaje llamada object, utilizamos el __str__ para que cuando llames al objeto puedas devolver una descripción del mismo
    def __str__(self):
        return "El objeto es {} {}".format(self.marca,self.color)
    # destructor, programa que se ejecuta al final de un programa que tiene clases y objetos; se encarga de borrar todos los objetos al terminar la ejecución; es automático, no hay que llamarlo
    def __del__(self):
        print("El objeto {} ha sido destruído".format(self.marca))
        pass

coche1=FabricaCoches("opel","azul")
print(coche1.marca,coche1.color)
print(coche1)