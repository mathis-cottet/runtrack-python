# tabl = [
#     [0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0],
# ]

# def dame(tabl):

def valide(L,ligne, col) :
    ok=True
    for d in range(1,ligne+1) :
        if L[ligne-d]==col or L[ligne-d]==col-d or L[ligne-d]==col+d :
            ok=False
            break
    return ok


def dame() :
    L=[-1]*4
    for a in range(4) :
        L[0]=a
        for b in range(4) :
            if valide(L,1,b) : L[1]=b
            else : continue
            for c in range(4) :
                if valide(L,2,c) : L[2]=c
                else : continue
                for d in range(4) :
                    if valide(L,3,d) :
                        L[3]=d
                        print(L)
                    else :continue
dame()
