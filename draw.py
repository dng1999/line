from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y
    B = x - x1
    d = (2*A) + B
    while (x < x1):
        plot(screen,color,x,y)
        if (d > 0):
            y += 1
            d += (2*B)
        x += 1
        d += (2*A)
    pass
