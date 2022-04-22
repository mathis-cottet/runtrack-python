import re

folder = open("./data.txt", "r")
x = folder.read()

list_word = re.findall("[\\W]+", x)
print(len(list_word))