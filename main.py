from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Elliott's Snake Game")
screen.tracer(0) #allows the snake to move smoothly

#1. CREATING THE BODY OF THE SNAKE
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#2. MOVING THE SNAKE
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True
while game_on:
    screen.update() #updates the movement of the whole snake
    time.sleep(0.1) #fixes the speed of the snake
    snake.move()

#3. CONTROL THE SNAKE - in snake.py file

#4. COLLECTING THE FOOD
    if snake.head.distance(food) < 15: #if the snake comes within 15 pixels of the food
        food.refresh()
        snake.extend()
        scoreboard.increase()

#5. CREATING SCOREBOARD - in scoreboard.py

#6. DETECTING COLLISION WITH THE WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()
        
#7. DETECTING COLLISION WITH THE TAIL
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
screen.exitonclick()