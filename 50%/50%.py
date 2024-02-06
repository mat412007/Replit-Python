# libraries random, os, time -
# random.randint() random.choice() -
# os.system("clear") -
# time.sleep(2) -
# print(, end="" sep="") -
# format strings -
# (f"{title:^35}") left <, right >, center ^ -
# lists -
# in  not in -
# len() .append() .remove() .sort() -
# .lower() .upper() .title() .capitalize() .strip() -
# myString[0:6:2] -
# split() -
# '\033[?25l' '\033[?25h' -
"""
all = input("Enter your first name, last name, Mum's maiden name and the city you were born in").split()
first = all[0].strip()  
last = all[1].strip() 
maiden = all[2].strip() 
city = all[3].strip() 
"""
# dictionaries -
# .values() .keys() .items() -
# list() -
# 2D Lists -
# global -
# 2D Dictionaries -
# Files
"""
for key, value in clue.items():
    print(key, end=": ")
    for subKey, subValue in value.items():
      print(subKey, subValue, end=" | ")
"""
"""
f = open("savedFile.txt", "w")
f.write("Hello there")
f.close()
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

import random, os, time
os.system("cls")
while True:
  print()
  print("Welcome to the summary of the 50% of the course!!!\n")
  go = input("Do you wanna access? (y / n)\n")
  if go[0].strip().lower() != "y":
    break
  time.sleep(1)
  os.system("cls")
  print()
  name = input("What's your name? ")
  age = input("How old are you? ")
  home = input("Where are you from? ")
  print(f"\nOk, so you are {name}, you are {age} years old, and you live in {home}", end="")
  time.sleep(2)
  os.system("cls")
  print("")
  print("Let's test your luck\nWe are gonna play Lotto!\n")
  while True:
    print(f"{'Lotto!':>30}")
    lottery = ["Regular", "Good", "Very Good", "Excellent"]
    lottery1 = lottery[random.randint(0,3)]
    lottery2 = random.choice(lottery)
    lottery3 = random.choice("Regular,Good,Very Good,Excellent".split(","))
    print(f"{lottery1} | {lottery2} | {lottery3}\n")
    if lottery1 == lottery2 and lottery2 == lottery3:
      print("Looks like luck is on your side")
    elif lottery1 == lottery2 and lottery2 != lottery3 or lottery2 == lottery3 and lottery1 != lottery2 or lottery1 == lottery3 and lottery2 != lottery3:
      print("Not bad, not bad at all")
    else:
      print("What a terrible luck you have")
    print()
    answer = input("Wanna go again? ")
    if answer.strip().lower() == "y":
      os.system("cls")
      continue
    else:
      break
  os.system("cls")
  print()
  print("Now let's try with a To Do List")
  while True:
    print()
    print(f"{'ToDoList':>30}")
    ToDoList = []
    while True:
      procedure = input("Would you like to add, remove, edit or delete the list? ")
      if procedure.strip().lower() == "a":
        toDo = input("What would you like to add?\n")
        if toDo not in ToDoList:
          ToDoList.append(toDo)
          print("Added")
        elif toDo in ToDoList:
          print("This is already on the list")
      elif procedure.strip().lower() == "r":
        toDo = input("What would you like to remove?\n")
        if toDo not in ToDoList:
          print("Unfortunately this is not on the list")
        elif toDo in ToDoList:
          ToDoList.remove(toDo)
          print("Removed")
      elif procedure.strip().lower() == "d":
          ToDoList = []
          print("All cleared")
      elif procedure.strip().lower() == "e":
        toDo = input("What would you like to change?\n")
        print()
        change = input("What would you like to insert instead?\n")
        for index in range(len(ToDoList)):
          if ToDoList[index] == toDo:
            ToDoList[index] = change
        print("All done")
      print()
      for item in ToDoList:
        print(f"- {item}")
      print()
      answer = input("Wanna go again? ")
      if answer.strip().lower() == "y":
        continue
      else:
        break
    break
  print()
  os.system("cls")
  print("It's time to do a mini test")
  while True:
    print()
    print(f"{'Test':>30}")
    print("Let's name some men to become policemen")
    info = []
    while True:
      name = input("What's your name?\n")
      age = input("How old are you?\n")
      home = input("Where are you from?\n")
      experience = input("What's your level of experience?\n")
      candidate = {"name": name, "age": age, "home": home, "experience": experience}
      info.append(candidate)
      print()
      for item in info:
          for key, value in item.items():
            print(f"{key}: {value}")
          print("---------------")
      answer = input("Wanna add another candidate? ")
      if answer.strip().lower() == "y":
        continue
      else:
        break
    break
  print()
  os.system("cls")
  print("Now let's do a little Mokebeast game")
  while True:
    print()
    print(f"{'Mokebeast':>30}")
    ListBeast = {}
    opponents = []
    for i in range(2):
      name = input("The name of your beast is: ")
      type = input("What type is your beast? ")
      power = random.randint(1,100)
      print(f"The power of {name} is {power}")
      ListBeast[name] = {"name":name, "type":type, "power":power}
      opponents.append(name)
      time.sleep(1)
      print()
    if ListBeast[opponents[0]]["power"] < ListBeast[opponents[1]]["power"]:
      print(f"{ListBeast[opponents[1]]["name"]} is the winner")
    elif ListBeast[opponents[0]]["power"] > ListBeast[opponents[1]]["power"]:
      print(f"{ListBeast[opponents[0]]["name"]} is the winner")
    print()
    answer = input("Wanna go again? ")
    if answer.strip().lower() == "y":
      continue
    else:
      break
  print()
  again = input("Do you wanna go again? (y / n)\n")
  if again[0].strip().lower() == "y":
    os.system("cls")
    continue
