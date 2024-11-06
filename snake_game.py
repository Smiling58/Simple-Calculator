import turtle
import time
import random


delay = 0.1

#set up the screen
wn = turtle.Screen()
wn.title("Snake game by Smarica Chaulagain")
wn.bgcolor("#CFF7A2")
wn.setup(width=600, height=600)
wn.tracer(0)      #turn off the animation on the screen

#Snake head (turtle object)
head = turtle.Turtle()
#animation speed of turtle head motion speed(0)
head.speed(0)     
head.shape("square")
head.shapesize(stretch_wid=0.75, stretch_len=0.75)
head.color("black")
head.penup()    #make sure it doesn't draw anything
head.goto(0,0)  #head, when it starts will be on the center of the screen
head.direction = "stop"  

#Snake food
food = turtle.Turtle()
food.speed(0)     
food.shape("circle")
food.shapesize(stretch_wid=0.75, stretch_len=0.75)
food.color("red")
food.penup()    
food.goto(0,100)  

segments = []

#use the turtle as pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("#746AF7")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0   High score: 0", align="center", font=("Courier", 24, "normal"))

#Score
score = 0
high_score = 0



#Functions 
#for the blink screen function
def blink_screen():
    for _ in range(3):  # Blink 3 times
        wn.bgcolor("#B0F7A1")  # Change to red for the blink effect
        time.sleep(0.1)
        wn.bgcolor("#F0A1F7")  # Change back to the original color
        time.sleep(0.1)
        wn.bgcolor("#CFF7A2")

def go_up():
    if head.direction != "down":
         head.direction = "up"

def go_down():
    if head.direction != "up":
         head.direction = "down"

def go_right():
    if head.direction != "left":
         head.direction = "right"

def go_left():
    if head.direction != "right":
         head.direction = "left"

#move function to move the snakehead 20px in each direction
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Keyboard bindings    (connects a keypress to a particular function)
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


#Main game loop
while True:
    wn.update()

    #check for collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        blink_screen()  # Blink the screen when the game is over
        time.sleep(1)   
        head.goto(0,0)
        head.direction = "stop"
        
        #Reset the score
        score = 0

        #reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    #hide the segments after they have collided with the border
        for segment in segments:
            segment.goto(1000, 1000)

    #clear the segments list
        segments.clear()
    #check for the collision with the food 

    #each of the basic turtle shape is 20px (wide/tall)
     #center of one pixel to the outer edge is 10 if that happens, we say that it has collided
     
    if head.distance(food) < 20: 
    #move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #add a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.shapesize(stretch_wid=0.75, stretch_len=0.75)
        new_segment.penup()

        #shorten the delay after food is met
        delay -= 0.001
        segments.append(new_segment)

        #Increase score at the increment of each segment
        score += 10

        if score> high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    #move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #check for head collisions
    for segment in segments:
        if segment.distance(head) < 20:
            blink_screen()  # Blink the screen 
            time.sleep(1)
            head.goto(0, 0)
            head.direction= " stop"  
            #hide the segments after they have collided
            for segment in segments:
                segment.goto(1000, 1000)
            
            #clear the segments 
            segments.clear()

             #Reset the score
            score = 0

            #reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            

    time.sleep(delay)       #stops the program for about one tenth of a second

wn.mainloop()
