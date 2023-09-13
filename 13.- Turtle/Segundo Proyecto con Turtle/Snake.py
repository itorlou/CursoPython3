import turtle
import time
import random

retraso = 0.1
marcador = 0
marcador_alto = 0

s = turtle.Screen()
s.setup(650,650)
s.bgcolor('gray')
s.title('Snake')
s.tracer()

serpiente = turtle.Turtle()
serpiente.speed(1)
serpiente.shape('square')
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = 'stop' # type: ignore
serpiente.color('green')

comida = turtle.Turtle()
comida.shape('circle')
comida.color('orange')
comida.penup()
comida.goto(0,100)
comida.speed(0)

cuerpo = []

texto = turtle.Turtle()
texto.speed(0)
texto.color('black')
texto.penup()
texto.hideturtle()
texto.goto(0, -260)
texto.write("Marcador: 0\tMarcador más alto: 0", align="center", font=("verdana", 24, "normal"))


def arriba():
    serpiente.direction = 'up' # type: ignore

def abajo():
    serpiente.direction = 'down' # type: ignore

def derecha(): 
    serpiente.direction = 'right'# type: ignore

def izquierda():
    serpiente.direction = 'left'# type: ignore

def movimiento():
    if serpiente.direction == 'up':# type: ignore
        y = serpiente.ycor()
        serpiente.sety(y + 20)
    if serpiente.direction == 'down':# type: ignore
        y = serpiente.ycor()
        serpiente.sety(y - 20)
    if serpiente.direction == 'right':# type: ignore
        x = serpiente.xcor()
        serpiente.setx(x + 20)
    if serpiente.direction == 'left':# type: ignore
        x = serpiente.xcor()
        serpiente.setx(x - 20)

s.listen()
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(izquierda, "Left")
s.onkeypress(derecha, "Right")

while True:
    s.update()

    if serpiente.xcor() > 300 or serpiente.xcor() < -300 or serpiente.ycor() > 300 or serpiente.ycor() < -300:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        serpiente.home()
        serpiente.direction = 'stop' # type: ignore   
        cuerpo.clear()

        marcador = 0 
        texto.clear()
        texto.write("Marcador:{}\tMarcador más alto:{}".format(marcador, marcador_alto),align="center", font=("verdana", 24, "normal"))

    if serpiente.distance(comida) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        comida.goto(x,y)

        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape('square')
        nuevo_cuerpo.color('green')
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo)

        marcador += 10
        if marcador > marcador_alto:
            marcador_alto = marcador
            texto.clear()
            texto.write("Marcador:{}\tMarcador más alto:{}".format(marcador, marcador_alto),align="center", font=("verdana", 24, "normal"))
        
    total = len(cuerpo)
    for index in range(total -1, 0, -1):
        x = cuerpo[index-1].xcor()
        y = cuerpo[index-1].ycor()
        cuerpo[index].goto(x,y)
            
    if total > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x,y)

    movimiento()

    for i in cuerpo:
        if i.distance(serpiente) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serpiente.home()
            cuerpo.clear()
            serpiente.direction = "stop"# type: ignore

    time.sleep(retraso)

turtle.done()