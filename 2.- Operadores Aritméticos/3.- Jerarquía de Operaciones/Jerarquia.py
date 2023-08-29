num1 , num2 , num3 , num4= 100 , 50 , 25 , 10

print (num1 +num2 * num3) # vemos que por jerarquía hace primero la multiplicación

print ((num1 +num2) * num3) # si colocamos el paréntesis hace primero la suma y luego la multiplicación

print ((num1 +num2) * num3 - num4) # paréntesis -> multiplicación -> resta

print ((num1 +num2) * (num3 - num4)) # paréntesis -> multiplicación


print ((num1 +num2) * (num3 - num4) / (num1-num4)) # parentesis -> multiplicaicón -> división

