from turtle import *

#we want to paint a house
speed(30) #drawing speed
width(7)  #line width
#step 1: draw a square

color("brown") #line color
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drowing a door
forward(70)
color("light yellow") #line color
begin_fill()
left(90)

forward(120) #height of the dor
right(90)

forward(65)
right(90)

forward(120)
end_fill()
#end of dor

# drowing roof
penup() #Pen UP
goto(200, 200)
pendown() #Pen Down

color("light blue") #line color
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end drowing roof

#drowing left window
penup() #Pen UP
goto(20, 135)
pendown() #Pen Down
color("white")
begin_fill()
left(120)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
end_fill()
#end frowing left window

#drawing right window
penup() #Pen UP
goto(180, 135)
pendown() #Pen Down
color("white")
begin_fill()
left(180)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
end_fill()
# the end

exitonclick() 









































