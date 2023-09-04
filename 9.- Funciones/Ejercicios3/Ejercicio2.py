# Escribir una función que reciba una muestra de números en una lista y devuelva su medida.

def lenNums(*nums):
    for i in nums:
        print(i)
    return len(nums)

print("La longitud es ",lenNums(1,2,3,4,5))