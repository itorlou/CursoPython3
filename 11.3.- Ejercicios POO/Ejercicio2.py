# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.


class Calculadora():
    def __init__(self):
        self._valor1=float(input("Dime el primer número: "))
        self._valor2=float(input("Dime el segundo número: "))

    def Suma(self):
        print("El resultado de {} + {} es: {}".format(self._valor1, self._valor2,  self._valor1 +self._valor2))
    def Resta(self):
        print("El resultado de {} - {} es: {}".format(self._valor1, self._valor2,  self._valor1 -self._valor2))
    def Mutiplica(self):
        print("El resultado de {} x {} es: {}".format(self._valor1, self._valor2,  self._valor1 *self._valor2))
    def Divide(self):
        print("El resultado de {} / {} es: {}".format(self._valor1, self._valor2,  self._valor1 /self._valor2)) 

calculadora=Calculadora()    
    
calculadora.Suma()
calculadora.Resta()
calculadora.Mutiplica()
calculadora.Divide()

