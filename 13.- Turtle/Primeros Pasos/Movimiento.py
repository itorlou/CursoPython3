import turtle

s = turtle.Screen()
t = turtle.Turtle()
#inicia en el 0.0

t.goto(100,100) #para que vaya a un punto del plano cartesiano
t.goto(-100,100)

#para que regrese al punto 0.0

#t.goto(0,0)
t.home()


#vamos a dibujar un cuadrado
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

turtle.done()