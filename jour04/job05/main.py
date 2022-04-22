import re
import matplotlib.pyplot as plot


f = open("./data.txt", "r")
folder = re.findall("[\w']", f.read().lower())


letters = {}
countL = 0

for word in folder:
    for lettre in word:
        if lettre in letters.keys():
            letters[lettre] += 1
        else:
            letters[lettre] = 1

        countL = countL + 1
 

for l in letters:
    letters[l] = (letters[l] * 100) / countL


x = letters.keys()
y = letters.values()

plot.bar(x,y)
plot.savefig("./diag.png")