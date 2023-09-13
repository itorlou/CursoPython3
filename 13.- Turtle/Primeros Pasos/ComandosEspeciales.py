import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.speed(10) # velocidad de la tortuga (del 1 al 10)
t.circle(60) #hace un círculo y le pasamos el radio
t.dot(60, "red") #dibuja un punto y le pasamos el diámetro
t.hideturtle() #para ocultar la tortuga por pantalla
t.circle(70)
t.dot(30, "green")
t.showturtle() #para mostrar la tortuga por pantalla
t.circle(100)
t.setx(-200) #para que mantenga el eje X y avance el número que le des
t.sety(150)

turtle.done()