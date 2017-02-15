from display import *
from draw import *

screen = new_screen()
color = [ 255, 255, 255 ]

"""
for i in range(0,500):
    color[0] = (i^2 + i + 20)  % 256
    color[2] = (i * 7 - 10)  % 256
    draw_line(0,0,500,i,screen,color)
"""

#oct 1
draw_line(0,250,500,500,screen,color)
#oct 2
draw_line(0,250,100,500,screen,color)
#oct 3
draw_line(500,250,400,0,screen,color)
#oct 4
draw_line(500,250,0,0,screen,color)
#oct 5
draw_line(500,250,0,500,screen,color)
#oct 6
draw_line(500,250,400,500,screen,color)
#oct 7
draw_line(0,250,100,0,screen,color)
#oct 8
draw_line(0,250,500,0,screen,color)
#vertical up
draw_line(250,250,250,500,screen,color)
#vertical down
draw_line(250,250,250,0,screen,color)
#horizontal left
draw_line(250,250,0,250,screen,color)
#horizontal right
draw_line(250,250,500,250,screen,color)

#display(screen)
#clear_screen(screen)

"""
for i in range(0,500):
    color[0] = (i^2 + i + 20)  % 256
    color[2] = (i * 7 - 10)  % 256
    draw_line(0,0,500,i,screen,color)
"""

display(screen)
save_extension(screen, 'img.png')
