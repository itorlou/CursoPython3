class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0 

    @property #decorador para poder llamarlo como un atributo (sin los paréntesis)
    def cuenta(self):
        return self._cuenta

    #cada atributo debe tener su método get
    @property
    def contador(self):
        return self._contador


a = A()

# print(a._cuenta) #esto es incorrecto puesto que el atributo está encapsulado

# print(a.cuenta()) #así lo hacemos desde el método, no llamamos directamente al atributo, al ser un método debe de llevar estos paréntesis, 

print(a.cuenta)
print(a.contador)