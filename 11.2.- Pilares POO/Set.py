class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0 

    @property #decorador para poder llamarlo como un atributo (sin los paréntesis)
    def cuenta(self):
        return self._cuenta
    
    @cuenta.setter #decorador para el setter 
    def cuenta(self, cuenta):
        self._cuenta=cuenta

    @property
    def contador(self):
        return self._contador
    
    @contador.setter #decorador para el setter 
    def contador(self, contador):
        self._contador=contador



a = A()

print(a.cuenta)
print(a.contador)

# metodos setter para modificar su valor 
a.cuenta=50 # llamamos al método set

print(a.cuenta) #llamamos al método get
