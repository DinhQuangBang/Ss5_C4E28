from turtle import *
speed (0)

def draw_square(length,colorr):
     color(colorr)
     for i in range(4):
         forward(length)
         left(90)
draw_square(200,"black")

mainloop ()