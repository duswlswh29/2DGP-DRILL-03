from pico2d import *

open_canvas()

boy=load_image('character.png')
grass=load_image('grass.png')

def move_rectangle():
    print("Move rectangle")
    clear_canvas_now()
    pass


def move_triangle():
    print("Move triangle")
    clear_canvas_now()
    pass


def move_circle():
    print("Move circle")
    r=200
    for deg in range(0, 360):
        x=r*math.cos(math.radians(deg))+400
        y=r*math.sin(math.radians(deg))+300
        clear_canvas_now()
        boy.draw_now(x,y)
        delay(0.1)

    pass


while True:
    move_rectangle()
    move_triangle()
    move_circle()
    break
    pass




close_canvas()
