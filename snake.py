import turtle
import time
import random

posponer = 0.1

#marcador
puntos = 0
puntos_mayor = 0
# Configuración de la pantalla
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

def generar_coordenadas_multiplos():
    x = random.randint(-14, 14) * 20
    y = random.randint(-14, 14) * 20
    return x, y

x, y = generar_coordenadas_multiplos()
comida.goto(x, y)
 

# cuerpo de la serpiente
cuerpo = []

#puntos texto
puntos_texto = turtle.Turtle()
puntos_texto.speed(0)
puntos_texto.color("white")
puntos_texto.penup()
puntos_texto.hideturtle()
puntos_texto.goto(0, 260)
puntos_texto.write("Puntos: 0 Puntos mayor: 0", align="right", font=("Courier", 12, "normal"))
# Funciones de la serpiente
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"

def mov():
    if cabeza.direction != "stop":
        if cabeza.direction == "up":
            y = cabeza.ycor()
            cabeza.sety(y + 20)
        if cabeza.direction == "down":
            y = cabeza.ycor()
            cabeza.sety(y - 20)
        if cabeza.direction == "left":
            x = cabeza.xcor()
            cabeza.setx(x - 20)
        if cabeza.direction == "right":
            x = cabeza.xcor()
            cabeza.setx(x + 20)

#teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")


while True:
    wn.update()

    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"
        for cuerpo in cuerpo:
            cuerpo.goto(1000, 1000)
        cuerpo.clear()

    if cabeza.distance(comida) <= 10:
        x, y = generar_coordenadas_multiplos()
        comida.goto(x, y)
        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.speed(0)
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("white")
        nuevo_cuerpo.penup()
        cuerpo.append(nuevo_cuerpo)
        puntos += 1

    #aumentar puntos    
    
    if puntos > puntos_mayor:
        puntos_mayor = puntos
    puntos_texto.clear()
    puntos_texto.write("Puntos: {} Puntos mayor: {}".format(puntos, puntos_mayor), align="right", font=("Courier", 12, "normal"))
    #mover el cuerpo de la serpiente
    totalseg = len(cuerpo)
    for index in range(totalseg - 1, 0, -1):
        x = cuerpo[index - 1].xcor()
        y = cuerpo[index - 1].ycor()
        cuerpo[index].goto(x, y)
    if totalseg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        cuerpo[0].goto(x, y)    
    mov()
    time.sleep(posponer)
