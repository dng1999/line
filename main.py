from display import *
from draw import *

screen = new_screen()
color = [ 0, 0, 0 ]

for i in range(0,500):
    color[0] = (i^2 + i + 20)  % 256
    color[2] = (i * 7 - 10)  % 256
    draw_line(0,0,500,i,screen,color)

display(screen)
clear_screen(screen)

for i in range(0,500):
    color[0] = (i^2 + i + 20)  % 256
    color[2] = (i * 7 - 10)  % 256
    draw_line(0,0,500,i,screen,color)

display(screen)
save_extension(screen, 'img.png')
