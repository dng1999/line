from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if (x0 > x1):
        draw_line(x1,y1,x0,y0,screen,color)
    else:
        
        x = x0
        y = y0
        
        A = y1 - y
        B = x - x1

        if (abs(B)>abs(A)): #oct 1 or 8
            if (A > 0): #oct 1
                d = (2*A) + B
                while (x <= x1):
                    plot(screen,color,x,y)
                    if (d > 0):
                        y += 1
                        d += (2*B)
                    x += 1
                    d += (2*A)
            else: #oct 8
                d = (2*A) - B
                while (x <= x1):
                    plot(screen,color,x,y)
                    if (d < 0):
                        y -= 1
                        d -= (2*B)
                    x += 1
                    d += (2*A)
        else: #oct 2 or 7
            if (A > 0): #oct 2
                d = A + (2*B)
                while (y <= y1):
                    plot(screen,color,x,y)
                    if (d < 0):
                        x += 1
                        d += (2*A)
                    y += 1
                    d += (2*B)    
            else: #oct 7
                d = A - (2*B)
                while (y >= y1):
                    plot(screen,color,x,y)
                    if (d > 0):
                        x += 1
                        d += (2*A)
                    y -= 1
                    d -= (2*B)
