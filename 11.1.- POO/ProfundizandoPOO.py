class FabricaCoches():
    def __init__(self, marca, *colores,**modelos):
        self.marca=marca
        self.colores=colores
        self.modelos=modelos
        #en vez de poner self podríamos poner otra palabra pero se recomienda como buena práctica usar el self

coche1 = FabricaCoches("BMW")
print(coche1.marca)
coche1 = FabricaCoches("BMW","Negro", "Azul", "Amarillo", x2=500,m3=600,ix1=100) 

print(coche1.colores)
print(coche1.modelos)

coche1.numPuertas=3 #podemos crear atributos temporales para un solo objeto sin añadirlo a la clase # type: ignore
print( coche1.numPuertas) # type: ignore