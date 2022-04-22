import re

folder = open("./domains.xml", "r")

x = folder.read()

print(str(len(re.findall('([.][a-z]{2,4})\W', x))))