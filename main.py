# Snake Game Using Turtle.

from turtle import Screen
from snake import Snake     # importing Snake class from snake.py class.
from food import Food
from score_board import Scoreboard
import random
import time

screen = Screen()   # screen variable refering to the Screen() function.
screen.setup(600, 600)   # setting up the screen size to 650 x 650 pixels.
screen.bgcolor("black")   # for making the screen color black.
screen.title("Snake Game - Made by Koushik Sadhu")  # A string that is displayed/shown on the title bar of the turtle graphics window.
screen.tracer(0);   # This function is used to turn the turtle animation on and off and set a delay for update drawings. In order to turn it off we set the tracer value to zero.

# # Creating a snake body manually:
# snake = Turtle("square")
# snake.color('white', 'white')
# snake1 = Turtle("square")
# snake1.color("white", "white")
# snake1.goto(x = -20, y = 0)     # x = snake.xcor()-20 = -20.
# snake2 = Turtle("square")
# snake2.color("white", "white")
# snake2.goto(x = -40, y = 0)    # x = snake1.xcor()-20 = -40.

snake = Snake()     # Creating object of the class Snake.
food = Food()       # Creating object of the class Food.
scoreboard = Scoreboard()       # Creating object of the class Scoreboard. 

screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
    
game_is_on = True           # Making game_is_on variable True.
while game_is_on:           # Infinite loop.
    screen.update()         # Peforms a TurtleScreen update. It is used when tracer is turned off.
    time.sleep(0.1)         # It is used to add delay in the executuion of the program.
    snake.move()            # calling the move function from the class Snake.
    
    
    # Detect collision of snake with food.
    if snake.head.distance(food) < 15:
        food.random_location()
        snake.extend()
        scoreboard.score_update()
        
    # Detect collision of snake with wall.
    if snake.head.xcor() > 280:
        snake.head.goto(-280, snake.head.ycor()) 
    if snake.head.ycor() > 280:
        snake.head.goto(snake.head.xcor(), -280)
    if snake.head.xcor() < -280:
        snake.head.goto(280, snake.head.ycor()) 
    if snake.head.ycor() < -280:
        snake.head.goto(snake.head.xcor(), 280)
        
    # Detect collision of snake head with snake tail.
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.game_over()
            game_is_on = False
    
    
        

        
    


















screen.exitonclick()