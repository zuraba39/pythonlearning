from turtle import *
# we want to paint a house
shape("turtle")
#step 1: draw a square

width(3)
color("red")
begin_fill()
forward(150)
left(90)

forward(150)
left(90)

forward(150)
left(90)

forward(150)
left(90)
end_fill()

#end of square

#drawing a door

forward(50)
color("green")
begin_fill()
left(90)
forward(60)   # height of the door
right(90)
forward(40)
right(90)
forward(60)
end_fill()
penup()
goto(150,150)
pendown()

color("purple")
begin_fill()
right(140)
forward(120)
left(100)
forward(120)
end_fill()

#window

penup()
goto(30,90)
pendown()

color ("pink")
begin_fill()
left(120)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)



penup()
goto(100,90)
pendown()

left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()





exitonclick()









































