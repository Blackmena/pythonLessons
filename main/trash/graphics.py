from turtle import *
bgcolor("black")
speed(0)
pensize(2)
val = 180
colors = ("cyan", "red", "purple", "yellow", "violet", "green")
for col in colors:
    color(col)
    for j in range(8):
        lt(45)
        for i in range(2):
            fd(val)
            lt(60)
            fd(val)
        lt(120)
    val = val - 20
done