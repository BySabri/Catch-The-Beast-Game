import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Catch Beast")
screen.addshape("redbeast.gif")

timer_height = screen.window_height() / 2 * 0.9
score_height = screen.window_height() / 2 * 0.8

timer = turtle.Turtle()
timer.hideturtle()
timer.penup()
timer.goto(0,timer_height)
timer.color("red")

score = turtle.Turtle()
score.hideturtle()
score.penup()
score.goto(0,score_height)
score.color("red")


beast = turtle.Turtle()
beast.color("red")
beast.width(100)
beast.shape("redbeast.gif")

score_counter = 0
saniye_left = 30
stopper = False
FONT = "Arial", 24, "normal"
def hide_beast():
        beast.hideturtle()
        beast.penup()
        beast.teleport(random.randint(-400,400),random.randint(-400,400))
        beast.showturtle()

def tıkla(x, y):
    global score_counter
    if beast.distance(x, y) < 50:
        score_counter += 1
        score.clear()
        score.write(f"Skor: {score_counter}", align="center", font=(FONT))
        hide_beast()

def geri_say(saniye, stopper_p):
    global stopper
    stopper = stopper_p
    if saniye < 0 :
        timer.clear()
        timer.write("OYUN BİTTİ", align="center", font=(FONT))
        screen.onclick(None)
    elif saniye<45 and stopper == True :
        timer.clear()
        timer.write("Tekrar başlatmak istediğinize emin misiniz? y/n ",align="center", font=(FONT))
        screen.onkey(lambda: geri_say(30,False), "y")
        screen.onkey(lambda: geri_say(30,True), "n")
    else :
        timer.clear()
        timer.write(f"{saniye} saniye", align="center", font=(FONT))
        screen.ontimer(lambda: geri_say(saniye - 1,False), 1000 )

def restart_game():
    global score_counter, saniye_left , stopper
    stopper = False
    score_counter = 0
    saniye_left = 30
    score.clear()
    score.write(f"Skor: {score_counter}", align="center", font=(FONT))
    screen.onclick(tıkla)
    geri_say(saniye_left,True)

screen.listen()
screen.onclick(tıkla)
screen.onkey(restart_game,"r")

geri_say(saniye_left,False)
turtle.mainloop()
