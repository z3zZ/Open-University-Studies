import turtle

sides = int(input("Enter the number of sides: "))
length = int(input("Enter the length of each side: "))

angle = 360 / sides

t = turtle.Turtle()
t.speed(3)

for i in range(sides):
    t.forward(length)
    t.left(angle)

turtle.done()