print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1337:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1337:
  print('PIN accepted!')