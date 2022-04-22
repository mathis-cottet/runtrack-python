n = input("Entrez un nombre entier positif: ")
n = int(n)

def factorielle(n):

    if n == 0:
        return 1 
    
    else:
        return n * factorielle(n - 1)


print(factorielle(n))
