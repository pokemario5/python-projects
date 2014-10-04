from turtle import Turtle

harold = Turtle()

harold.speed(200)
harold.pensize(8)
harold.pencolor('chartreuse')

while True:

    for count in range(4):
        harold.forward(100)
        harold.right(90)
    harold.right(10)
