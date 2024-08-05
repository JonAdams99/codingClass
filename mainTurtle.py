# jon adams
#July first protjects

import turtle

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
t = turtle.Turtle()
t.speed(1)

sides=3
angle=360/sides

def back(len):
  t.penup()
  t.backward(len)
  t.pendown()

def equalShape(sides, size, color, move, penWidth, speed):
  back(move)
  angle=360/sides
  t.color(color)
  t.pensize(penWidth)
  t.speed(speed)
  for i in range(sides):

    #t.color(color)
    t.forward(size)
    t.left(angle)
    
def equalShapeRight(sides, size, color, move, penWidth, speed):
  back(move)
  angle=360/sides
  t.color(color)
  t.pensize(penWidth)
  t.speed(speed)
  for i in range(sides):
 
    t.forward(size)
    t.right(angle)

def equalShapeLeft(sides, size, color, move, penWidth, speed):
  back(move)
  angle=360/sides
  t.color(color)
  t.pensize(penWidth)
  t.speed(speed)
  for i in range(sides):

    t.forward(size)
    t.left(angle)

def rectangle(sideOne, sideTwo, color, move, penWidth, speed):
  back(move)
  angle=360/(2*2)
  t.color(color)
  t.pensize(penWidth)
  t.speed(speed)
  for i in range(2):
    
    t.forward(sideOne)
    t.right(angle)
    t.forward(sideTwo)
    t.right(angle)

# sideWidth = int(input("Enter width of the rectangle: "))
# sideHeight = int(input("Enter height of the rectangle: "))
sideLength = int(input("Enter length of the side: "))

rectangle((sideLength/5), (sideLength*2), "blue", 0, 5, 10)
equalShape(6, sideLength, "red", sideLength*(3/8), 5, 1)

# sideLength = int(input("Enter length of the side: "))

# equalShapeLeft(3, sideLength, "red", 0, 1, 1)
# equalShapeRight(4, sideLength, "red", 0, 1, 1)

# #draw a picture with a square and retangle
# equalShape(4, 40, "red", 25, 2, 1)
# rectangle(10, "blue", 0, 5, 10)
# rectangle(10, "blue", -30, 5, 10)
# #shape(5, 80, "green", 100)equalShape
  
  
screen.mainloop()

turtle.Screen().exitonclick()



# phrase = "Hello World"
# for letter in phrase:
#   t.write(letter, font=("Arial", 20, "normal"))
#   print (letter, end=" ")

# print(3)
# print("Done")
#size=20
