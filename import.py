#DEVELOP A PYTHON PROGRAMM  USING REGEX SUBSTITUTION TO REPLACE MULTIPLE CONSECUTIVE SPECES IN A TEXT FILE WITH SINGLE SPACING
import re

f = open("input.txt", "r")
data = f.read()
f.close()

data = re.sub(" +", " ", data)

f = open("output.txt", "w")
f.write(data)
f.close()

print("Consecutive spaces replaced successfully")