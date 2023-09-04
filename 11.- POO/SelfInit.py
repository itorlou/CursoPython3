# init -> constructor
# self -> palabra reservada de python, forma de equiparar los objetos llamándolos a una instancia, cada objeto es necesario que posea ciertos atributos de métodos de instancia

class FabricaTelefonos():
    #atributos
    marca = "Samsung"

    # metodos
    def ElaborarOnePlus(self): #este self nos permite englobar atributos a esta clase
        self.marca = "OnePlus"


telefono = FabricaTelefonos()

telefono.ElaborarOnePlus()

print(telefono.marca) 

############################

#Constructores en python
class FabricaCoches():
    def __init__(self , marca, color): #el init se ejecuta al crear un objeto sin que lo llamemos
        print("Estoy ejecutando el método init, se ha creado un nuevo objeto")
        self.marca=marca
        self.color=color

coche = FabricaCoches("Opel","Negro")

print(coche.marca)
print(coche.color)

#el init es lo primero que se ejecuta, así podemos hacer constructores en python poo, importante el uso del SELF