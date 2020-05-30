import turtle
t = turtle.Pen()
t.penup()
t.speed(0)
turtle.bgcolor("black")
sides = int(turtle.numinput("Number of sides",
                            "How many sides in your spiral of spirals (2-6)?", 4, 2, 6))
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
for m in range(100):
    t.forward(m*4)
    position = t.position()
    heading = t.heading()
    for n in range(sides):
        t.pendown()
        t.pencolor(colors[n % sides])
        t.circle(m/5)  # I believe that the denominator adjusts the increase in size per rosette.
        t.left(360/sides - 2)
        t.width(m/20)  # I believe that the denominator adjusts the increase in size per rosette.
        t.penup()
    t.setx(position[0])
    t.sety(position[1])
    t.setheading(heading)
    t.left(360/sides + 2)
