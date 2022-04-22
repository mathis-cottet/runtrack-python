x = input("Entrez un nombre entier positif: ")
x = int(x)

n = input("Entrez la puissance: ")
n = int(n)

def puissance(x,n):
    if n == 0:
        return 1
    
    x = x * puissance(x, n - 1)
    return x


print(puissance(x,n))