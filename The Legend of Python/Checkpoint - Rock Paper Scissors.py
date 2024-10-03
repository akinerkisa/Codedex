import random

choices = {1: "✊", 2: "✋", 3: "✌️"}

print("""
===================
Rock Paper Scissors
===================
""")

for number, symbol in choices.items():

  print(f"{number}) {symbol}")
  
while True:
  try:
      player = int(input("Pick a number: "))
      if player not in [1, 2, 3]:
          raise ValueError
      break
  except ValueError:
      print("Invalid input. Please enter 1, 2, or 3.")

computer = random.randint(1, 3)

print(f"\nYou chose: {choices[player]}")
print(f"CPU chose: {choices[computer]}")

if player == computer:
  result = "It's a tie!"
elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
  result = "The player won!"
else:
  result = "The CPU won!"
  
print(result)