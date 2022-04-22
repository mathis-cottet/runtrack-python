import re
val = int(input("Entrez un nombre entier: "))

folder = open("./data.txt", "r")
x = folder.read()

word = re.findall('\\b\\w{' + str(val) + '}\\b', x)

a = 0
i = 0

while i < len(word):
   if len(word[i]) == val :
       a += 1
   i += 1

print("Resultat", a)