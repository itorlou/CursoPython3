def valores(): #función estática, nunca se modifican
    global num1,num2 # si ponemos la palabra reservada global podemos acceder desde fuera del contexto de la funcion
    num1=110
    num2=40
    resultado = num1 +num2
    return resultado

print(valores())

# resta = num1 - num2 vemos que esto falla (sin poner el global), al variable num1, num2 existen dentro del contexto de la funcion
# print(resta)

resta = num1 - num2 
print(resta)