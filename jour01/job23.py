def draw_triangle(height):
    
    a = " "
    b = "/"
    c = "\\"
    d = "_"

    for h in range(0, height-1): #boucle de construction
        print(a*(height-h)+b+2*h*a+c)
    print(b+d*(2*height-1)+c)


draw_triangle(6)