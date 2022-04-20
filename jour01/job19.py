def draw_rectangle():
     
     width = int(input("Largeur"))
     height = int(input("Hauteur"))

     a = '-'*width
     b = ' '*width
    
     print('|{}|'.format(a)) 
    
     for i in range(0, height): 
            
         print('|{}|'.format(b)) 
         print('|{}|'.format(a))


draw_rectangle()