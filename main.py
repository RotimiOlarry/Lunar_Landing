import turtle
import random 

#Creating the game frame 
window = turtle.Screen()
window.tracer(0)
window.setup(0.6, 0.6)
window.title("The Lunar Landing Game")
window.bgcolor("black")

height = window.window_height()
width = window.window_width()

#Setting game parameters
num_of_stars = 140

#Setting the lunar model parameters 
branch_size = width // 16
num_of_discs = 5
disc_color = "light gray"
centre_color = "gold"
gear_color = "red"


stars = turtle.Turtle()
stars.hideturtle()
stars.penup()
stars.color("white")

for _ in range(num_of_stars):
    x_position = random.randint(-width//2 , width//2)
    y_position = random.randint(-height//2,height//2 )
    stars.setposition(x_position,y_position)
    stars.dot(random.randint(2,6))
    
moon = turtle.Turtle()
moon.penup()
moon.color("slate gray")
moon.sety(-height * 2.8)
moon.dot(height * 5)

#Creating the lunar model 
lunar_model = turtle.Turtle()
lunar_model.penup()
lunar_model.hideturtle()
lunar_model.setposition(-width/3 , height/3)

def draw_lunar_model():
    lunar_model.pendown()
    lunar_model.pensize(5)
    
    #Landing Gear
    lunar_model.color(gear_color)
    lunar_model.forward(branch_size)
    lunar_model.left(90)
    lunar_model.forward(branch_size/2)
    lunar_model.forward(-branch_size)
    lunar_model.forward(branch_size/2)
    lunar_model.right(90)
    lunar_model.forward(-branch_size)
    lunar_model.pensize(1)
    
    #The pods around around the edge of the module
    
    for _ in range(num_of_discs -1):
        lunar_model.right(360/num_of_discs)
        lunar_model.forward(branch_size)
        lunar_model.dot(branch_size/2)
        
    #The center part of the module
    lunar_model.color(centre_color)
    lunar_model.dot(branch_size)
    lunar_model.penup()
    
draw_lunar_model()

window.update()
turtle.done()