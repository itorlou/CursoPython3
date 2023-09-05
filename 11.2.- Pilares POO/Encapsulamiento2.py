class A():
    def __init__(self):
        self._contador = 0 #cuando se usen distintos atributos es importante encapsular con el _
        self._cuenta = 0 # type: ignore

    def incrementar(self):
        self._contador+=1

    def cuenta(self):
        return self._contador
    #el _ le va a avisar a "otro programador " de que este objeto está encapsulado; lo correcto sería llamar al método set y al get 

a= A()

# print(a.cuenta)

# a.cuenta = 20 # type: ignore #esto sería incorrecto, deberíamos usar el SET 

# print(a.cuenta)