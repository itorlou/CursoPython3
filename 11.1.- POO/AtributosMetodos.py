# vamos a ver métodos y atributos

#método = funcion dentro de una clase 
#atributos = cualidades o características que tiene un objeto de esta clase

class FabricaTelefonos():
    #atributos
    marca = "OnePlus"
    color = "Space Gray"
    memoriaRam = 8
    memoriaRom = 128
    #metodos
    def llamar(self,mensaje): #metodo de instancia: método que nosotros creamos
        return mensaje
    def escucharMusica(self):
        print("Estás escuchando música")

telefono = FabricaTelefonos()

telefono.marca 
print(telefono.marca)
telefono.color
telefono.memoriaRam
telefono.memoriaRom
print(telefono.memoriaRom)

print(telefono.llamar("Hola, ¿Quién es?"))

telefono.escucharMusica()