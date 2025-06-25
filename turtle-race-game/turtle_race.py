# head
from turtle import Turtle, Screen
import random
fast = [1,2,3,4,5,6,7,8,9,10]
hmody = Turtle()
nu2 = Turtle()
nu3 = Turtle()
nu4 = Turtle()
draw_win = Turtle()
draw_win.hideturtle()

# screen setup
windows = Screen()
windows.bgcolor("dim gray")
windows.setup(1200, 700)
windows.title("⬛⬜⬛⬜Turtle race⬜⬛⬜⬛")



# engine's

# join
def members():
    # 1
    hmody.shape("turtle")
    hmody.color("white smoke")
    hmody.pensize(5)
    hmody.penup()
    hmody.speed(3)
    # 2
    nu2.shape("turtle")
    nu2.color("red")
    nu2.pensize(5)
    nu2.penup()
    nu2.speed(3)
    # 3
    nu3.shape("turtle")
    nu3.color("dark blue")
    nu3.pensize(5)
    nu3.penup()
    nu3.speed(3)
    # 4
    nu4.shape("turtle")
    nu4.color("dark orange")
    nu4.pensize(5)
    nu4.penup()
    nu4.speed(3)

    # position
    hmody.goto(-560, 160)
    hmody.write("Hmody!", font=("arial", 15, "normal"), align="center")
    hmody.goto(-590, 150)
    nu2.goto(-590, 55)
    nu3.goto(-590, -55)
    nu4.goto(-590, -150)
    

# finish line
def end_line():
    finish_line = Turtle()
    finish_line.hideturtle()
    finish_line.color("white")
    finish_line.pensize(30)
    finish_line.penup()
    finish_line.goto(420, 300)
    finish_line.pendown()
    finish_line.goto(420, -250)
    finish_line.color("black")
    finish_line.left(90)
    i = -200

    for _ in range(6):
        finish_line.pendown()
        finish_line.forward(50)
        finish_line.penup()
        finish_line.forward(50)
        i += 50

# selector
def player_turtle(choice):
    choice = choice.lower() 
    if choice == "hmody" or choice == "white":
        return hmody
    if choice == "red":
        return nu2
    if choice == "blue":
        return nu3
    if choice == "orange":
        return nu4

# game status
def check_winner(check):
    
    # check
    if check.xcor() >= 420:
        draw_win.color("green")
        draw_win.write(f"You Won （￣︶￣）↗　",font=("arial",40),align="center")
        return True
    if hmody.xcor() >= 420:
        draw_win.goto(0,40)
        draw_win.color("black")
        draw_win.write(f"U lose Coz,",font=("arial",20),align="center")
        draw_win.penup()
        draw_win.goto(0,0)
        draw_win.pendown()
        draw_win.color("white")
        draw_win.write(f"Hmody always win (⌐■_■)",font=("arial",30),align="center")
        return True
    if (nu2.xcor() >= 420) :
        draw_win.color("red")
        draw_win.write(f"you losed ＞﹏＜",font=("arial",40),align="center")
        return True 
    if (nu3.xcor() >= 420) :
        draw_win.color("blue")
        draw_win.write(f"you losed ＞﹏＜",font=("arial",40),align="center")
        return True 
    if (nu4.xcor() >= 420) :
        draw_win.color("orange")
        draw_win.write(f"you losed ＞﹏＜",font=("arial",40),align="center")
        return True 

# start race
def race(player):
    for _ in range(180):
        hmody.forward(random.choice(fast))
        nu2.forward(random.choice(fast))
        nu3.forward(random.choice(fast))
        nu4.forward(random.choice(fast))
        if check_winner(player): 
            break

# clear road
def clear():
    draw_win.pencolor("dim gray")
    draw_win.speed("fastest")
    draw_win.pensize(65)
    draw_win.goto(-450, 35)
    draw_win.goto(370, 35)
    draw_win.goto(0,0)
    


# Run area

# show
members()
player_choise = windows.textinput("Always made by H (>_<)", "Pick a Member [Hmody - Red - Blue - Orange]")
player = player_turtle(player_choise) 
end_line()

while True:
    race(player)
    members()
    player_choise = windows.textinput("Pick a Member", "[Hmody(white) - Red - Blue - Orange]")
    if not player_choise or player_choise.lower() not in ["hmody", "white", "red", "blue", "orange"] :
        clear()
        draw_win.goto(0,0)
        draw_win.penup()
        draw_win.color("red")
        draw_win.write("Wrong input (¬_¬)", font=("arial", 30), align="center")
        break
    player = player_turtle(player_choise) 
    clear()


# end show
windows.exitonclick()



#?       Follow us  ฅ⁠^⁠•⁠ﻌ⁠•⁠^⁠ฅ
#!    Youtube ->   @ZU Informatics 
#*     GitHub  ->  @HmodyCode999
