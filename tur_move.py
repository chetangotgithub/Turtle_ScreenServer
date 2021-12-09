import turtle as t
import random as r

def limit():
    left=(-t.window_width()/2)+100
    right=(t.window_width()/2)-100
    top=(t.window_height()/2)-100
    bottom=(-t.window_height()/2)+100
    (x,y)=t.pos()
    inside=left<x<right and bottom<y<top
    return inside
def move():
    if limit():
        angle=r.randint(1,180)
        dist=r.randint(1,100)
        t.right(angle)
        t.forward(dist)
        move()
    else:
        t.backward(200)
        move()



t.bgcolor('black')
t.shape('turtle')
t.fillcolor('red')
t.speed('slow')
move()
