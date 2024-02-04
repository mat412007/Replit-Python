# libraries random, os, time
# random.randint() random.choice()
# os.system("clear")
# time.sleep(2)
# print(, end="" sep="")
# '\033[?25l' '\033[?25h'
# format strings
# (f"{title:^35}") left <, right >, center ^
# lists  
# in  not in
# len() .append() .remove() .sort()
# .lower() .upper() .title() .capitalize() .strip()
# myString[0:6:2]
# split()
"""
all = input("Enter your first name, last name, Mum's maiden name and the city you were born in").split()
first = all[0].strip()  
last = all[1].strip() 
maiden = all[2].strip() 
city = all[3].strip() 
"""
# dictionaries
# .values() .keys() .items() 
# list()
# 2D Lists
# global
# 2D Dictionaries
# Files
"""
for key, value in clue.items():
    print(key, end=": ")
    for subKey, subValue in value.items():
      print(subKey, subValue, end=" | ")
"""
"""
open("savedFile.txt", "w")
f.write("Hello there")
"""
"""
f = open("savedFile.txt", "a+")
whatText = input("> ")
f.write(f"{whatText}\n")
f.close()
"""
"""
f = open("filenames.list", "r")
contents = f.read()
contents = contents.split()
print(contents)
contents = f.readline().strip()
print(contents)
f.close()
"""


