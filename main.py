import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("Snake game")
screen.tracer(0)
positions=[(0,0),(-20,0),(20,0)]
segments=[]
snake=Snake()
food=Food()
score=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.reset()
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scoreboard.reset()











screen.exitonclick()



