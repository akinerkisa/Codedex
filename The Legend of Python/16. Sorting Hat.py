gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print("""
Q1) Do you like Dawn or Dusk?
  1) Dawn
  2) Dusk
""")
answer = int(input("Enter your answer (1-2): "))

if answer == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer == 2:
  hufflepuff += 1
  slytherin +=1
else:
  print("Number not valid.")

print("""
Q2) When I'm dead, I want people to remember me as:

  1) The Good
  2) The Great
  3) The Wise
  4) The Bold
""")
answer = int(input("Enter your answer (1-4): "))

if answer == 1:
  hufflepuff += 2
elif answer == 2:
  slytherin += 2
elif answer == 3:
  ravenclaw += 2
elif answer == 4:
  gryffindor += 2
else:
  print('Number not valid.')

print("""
Q3) Which kind of instrument most pleases your ear?

  1) The violin
  2) The trumpet
  3) The piano
  4) The drum
""")
answer = int(input("Enter your answer (1-4): "))

if answer == 1:
  slytherin += 4
elif answer == 2:
  hufflepuff += 4
elif answer == 3:
  ravenclaw +=4
elif answer == 4:
  gryffindor += 4
else:
  print("Number not valid.")
  
print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)

most_points = max(gryffindor, ravenclaw, hufflepuff, slytherin)

if gryffindor == most_points:
  print("🦁 Gryffindor!")
elif ravenclaw == most_points:
  print("🦅 Ravenclaw!")
elif hufflepuff == most_points:
  print("🦡 Hufflepuff!")
else:
  print("🐍 Slytherin!")