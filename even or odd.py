import turtle
t = turtle.Pen()
t.speed(0)
sides = int(turtle.numinput("Number of sides", "How many sides in your spiral?", 4))
for m in range(5, 75):
    t.pencolor("crimson")
    t.left(360/sides + 5)
    t.width(m/25+1)
    t.penup()
    t.forward(m*4)
    t.pendown()
    if (m % 2 == 0):  # modulo 2 means that if the result is 0, then the number is even, as the modulo result is the remainder of division by 2
        for n in range(sides):
            t.pencolor("aquamarine")
            t.circle(m/3)
            t.right(360/sides)
    else:
        for n in range(sides):
            t.pencolor("crimson")
            t.forward(m)
            t.right(360/sides)
