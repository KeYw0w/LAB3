
import re


with open("test.txt") as f:
    list=f.readlines()
for line in list:
    if re.search("([z][\w]{3}[z])", line) is not None:
        print(line)