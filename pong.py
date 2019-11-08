## Pong para Python
import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by @cassiolm")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(delay=0) #atraso para a bola não correr muito

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square") #forma
paddle_a.color("white") #cor
paddle_a.shapesize(stretch_wid=5, stretch_len=1) ## tamanho do paddle
paddle_a.penup()
paddle_a.goto(-350, 0)#posição inicial

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square") #forma
paddle_b.color("white") #cor
paddle_b.shapesize(stretch_wid=5, stretch_len=1) ## tamanho do paddle
paddle_b.penup()
paddle_b.goto(350, 0)#posição inicial

# Bola

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square") #forma
ball.color("white") #cor
ball.penup()
ball.goto(0, 0)#posição inicial
ball.dx = 2 ## deltax - toda vez que a bola mexe, mexe por 1 pixel
ball.dy = -2 ## deltay

# Score
score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(" Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)


# Chamada pelo teclado
wn.listen()
wn.onkeypress(paddle_a_up, "w") #quando apertar w, chama a função subir paddle_a
wn.onkeypress(paddle_a_down, "s") #quando apertar s, chama a função descer paddle_a
wn.onkeypress(paddle_b_up, "Up") #quando apertar w, chama a função subir paddle_b
wn.onkeypress(paddle_b_down, "Down") #quando apertar s, chama a função descer paddle_b

# Main game loop
while True:
	wn.update()
	# Move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Border Checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
		
	if ball.ycor() <- 290:
		ball.sety(-290)
		ball.dy *= -1
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
		
	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_a += 1
		pen.clear()
		pen.write(" Player A: {}  Player B: {} ".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
	
	if ball.xcor() < -390:
		score_b += 1
		ball.goto(0, 0)
		ball.dx *= -1
		pen.clear()
		pen.write(" Player A: {}  Player B: {} ".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

	# Paddle and ball collisions
	if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
		ball.setx(-340)
		ball.dx *= -1 
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
	elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
		ball.setx(340)
		ball.dx *= -1
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)