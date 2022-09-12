print('Ifeanyi Virtual assistant robot v2.7.9\n\n')
#name input
Name = input("What is your Name: ")
username = input("Please enter a username:")
password = input("Please enter a password:")
#login
username1 = 'username' 
password_user = 'password'

userInput = input("What is your username?\n")
if userInput == username:
    a=input("Password?\n")
    if password == 'password_user':
        print("Correct password, Welcome "+Name+"")
     #activity area
activity_user = input("\nWhat would you like to do:\nGames\nCalculator\nGoogle\nSettings\nYoutube:\n")
#settings is being worked on
if activity_user == 'Games':
  print("Loading Games...")
  game=input("Snake(1):\nEgg Catcher(2):\n")
  if game=='1':
      import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0



# Creating a window screen
wn = turtle.Screen()
wn.title("Ifeanyi PYDER Snake Game")
wn.bgcolor("black")
# the width and height can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score : 0", align="center",
		font=("candara", 24, "bold"))



# assigning key directions
def group():
	if head.direction != "down":
		head.direction = "up"


def godown():
	if head.direction != "up":
		head.direction = "down"


def goleft():
	if head.direction != "right":
		head.direction = "left"


def goright():
	if head.direction != "left":
		head.direction = "right"


def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y+20)
	if head.direction == "down":
		y = head.ycor()
		head.sety(y-20)
	if head.direction == "left":
		x = head.xcor()
		head.setx(x-20)
	if head.direction == "right":
		x = head.xcor()
		head.setx(x+20)


		
wn.listen()
wn.onkeypress(group, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

segments = []



# Main Gameplay
while True:
	wn.update()
	if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
		time.sleep(1)
		head.goto(0, 0)
		head.direction = "Stop"
		colors = random.choice(['red', 'blue', 'green'])
		shapes = random.choice(['square', 'circle'])
		for segment in segments:
			segment.goto(1000, 1000)
		segments.clear()
		score = 0
		delay = 0.1
		pen.clear()
		pen.write("Score : {} High Score : {} ".format(
			score, high_score), align="center", font=("candara", 24, "bold"))
	if head.distance(food) < 20:
		x = random.randint(-270, 270)
		y = random.randint(-270, 270)
		food.goto(x, y)

		# Adding segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("orange") # tail colour
		new_segment.penup()
		segments.append(new_segment)
		delay -= 0.001
		score += 10
		if score > high_score:
			high_score = score
		pen.clear()
		pen.write("Score : {} High Score : {} ".format(
			score, high_score), align="center", font=("candara", 24, "bold"))
	# Checking for head collisions with body segments
	for index in range(len(segments)-1, 0, -1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x, y)
	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)
	move()
	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(1)
			head.goto(0, 0)
			head.direction = "stop"
			colors = random.choice(['red', 'blue', 'green'])
			shapes = random.choice(['square', 'circle'])
			for segment in segments:
				segment.goto(1000, 1000)
			segment.clear()

			score = 0
			delay = 0.1
			pen.clear()
			pen.write("Score : {} High Score : {} ".format(
				score, high_score), align="center", font=("candara", 24, "bold"))
	time.sleep(delay)

wn.mainloop()
      

if activity_user == 'Calculator':
  print("Loading Caluculator\n")
  # Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
if activity_user == 'Google':
  print("\nPlease click the following link:\nwww.google.com/")

if activity_user == 'Youtube':
  print("\nPlease click the following link:\nwww.youtube.com/?gl=GB&hl=en-GB")

