#el encapsulamiento es aplicar a los atributos cierto alcance para que solo pueda ser usado dentro de la clase 

class A():
    def __init__(self):
        self.contador = 0
    
    def incrementar(self):
        #cada vez que llame al método le va a agregar 1 al contador
        self.contador +=1

    def cuenta(self):
        # va a devolver el valor de contador
        return self.contador

a= A()
print("Objeto 1") 
print(a.cuenta()) 

a.incrementar()

print(a.cuenta())

print(a.contador) # así podemos ver que el atributo es accesible desde fuera de la clase ; esto no se debe de hacer por ningún motivo

class B():
    def __init__(self):
        self.__contador = 0 # si le ponemos las __ delante del nombre del atributo este quedaría encapsulado dentro de la clase ; quedaría en "privado"
    
    def incrementar(self):
        #cada vez que llame al método le va a agregar 1 al contador
        self.__contador +=1

    def cuenta(self):
        # va a devolver el valor de contador
        return self.__contador
    
print("Objeto 2")    
b = B()

print(b.cuenta())
b.incrementar()
print(b.cuenta())
# print(b.__contador) así vemos que da error