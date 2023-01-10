import turtle
import random 

#Creating the game frame 

window = turtle.Screen()
window.setup(0.6, 0,6)
window.title("The Lunar Landing Game")
window.bgcolor("black")

height = turtle.window_height()
width = turtle.window_width()

#Setting game parameters
num_of_stars = random.randint(80,140)
stars = turtle.Turtle()
stars.hideturtle()
stars.penup()
stars.color("white")

for _ in range(num_of_stars):
    x_position = random(-width//2 , width//2)
    y_position = random(-height//2,height//2 )
    stars.setposition(x_position,y_position)
    stars.dot(random(2,6))
    
moon = turtle.Turtle()
moon.penuppenup()
moon.color("slate gray")
moon.sety(-height * 2.8)
moon.dot(height * 5)

turtle.done()