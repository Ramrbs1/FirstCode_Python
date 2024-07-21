#Write a Turtle program to draw a square
#IDE is https://pythonsandbox.com/turtle

import turtle

t = turtle.Turtle()
t.speed(5)  # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

#Write a Turtle program to draw a square Using for loop
import turtle

t = turtle.Turtle()
for k in range(4):
  t.forward(100)
  t.right(90)

# Write a turtle program to draw a pentagon.
# [Hint : turn the turtle by 72 degrees this time]
import turtle

t = turtle.Turtle()
for k in range(5):
  t.forward(100)
  t.left(72)

#How to draw a circle using Turtle?
import turtle

t = turtle.Turtle()
t.pensize(2)
t.pencolor("red")
t.circle(50)

#How to draw three circle using Turtle?
import turtle

t = turtle.Turtle()
t.pensize(5)

t.pencolor("green")
t.circle(30)
t.penup()

t.goto(100, 0)
t.pendown()
t.pencolor("red")
t.circle(30)
t.penup()

t.goto(200, 0)
t.pendown()
t.pencolor("blue")
t.circle(30)

#36 circle
import turtle

t = turtle.Turtle()
t.pensize(2)
t.speed(50)

for i in range(36):
  t.circle(100)
  t.right(10)

#draw 40 ractangles

import turtle

t = turtle.Turtle()
t.pensize(2)
t.speed(20)

line = 10
for i in range(40):
  t.forward(line)
  t.right(90)
  line = line + 10
