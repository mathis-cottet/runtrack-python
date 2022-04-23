import re
import matplotlib.pyplot as plot

f = open("./data.txt", "r")
folder = re.findall("[\w']+", f.read().lower())

wordsL = {}
countW = 0

for word in folder:
    if len(word) in wordsL.keys():
        wordsL[len(word)] += 1
    else:
        wordsL[len(word)] = 1

    countW = countW + 1

for l in wordsL:
    wordsL[l] = (wordsL[l] * 100) / countW

x = wordsL.keys()
y = wordsL.values()

plot.bar(x,y)
plot.savefig("./diag.png")
