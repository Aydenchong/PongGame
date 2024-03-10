import turtle
from text import Score
from paddle import Paddle
from ball import Ball
import time

def setup():
    global screen, score, player1, player2, ball
    screen = turtle.Screen()
    screen.setup(900,600)
    screen.bgcolor("black")
    screen.title("Pong")
    score = Score()

    player1 = Paddle(1)
    player2 = Paddle(2)


    screen.listen()
    screen.onkeypress(player1.up, 'w')
    screen.onkeypress(player1.down, 's')
    screen.onkeypress(player2.up, 'Up')
    screen.onkeypress(player2.down, 'Down')

    ball = Ball()
    screen.tracer(0)

def game():
    global screen, score, player1, player2, ball

    gameover = False

    while gameover == False:
        time.sleep(0.03)
        screen.update()
        ball.setx(ball.xcor() + ball.speedx)
        ball.sety(ball.ycor() + ball.speedy)
        if abs(ball.ycor()) > 290:
            ball.speedy = -ball.speedy
        if ball.xcor() <= -420 and ball.ycor() < player1.ycor() + 50 and ball.ycor() > player1.ycor() - 50:
            ball.speedx = -ball.speedx
        if ball.xcor() >= 420 and ball.ycor() < player2.ycor() + 50 and ball.ycor() > player2.ycor() - 50:
            ball.speedx = -ball.speedx


def main():
    setup()
    game()
    screen.exitonclick()


if __name__ == "__main__":
    main()
