def get_item(item):
  if item == 1:
    return '🍔 Cheeseburger'
  elif item == 2:
    return '🍟 Fries'
  elif item == 3:
    return '🥤 Soda'
  elif item == 4:
    return '🍦 Ice Cream'
  elif item == 5:
    return '🍪 Cookie'
  else:
    return "invalid option"

def welcome():
  print('Welcome to Sonnyboy\'s Diner!')
  print('Here\'s the menu:')
  print('1. 🍔 Cheeseburger')
  print('2. 🍟 Fries')
  print('3. 🥤 Soda')
  print('4. 🍦 Ice Cream')
  print('5. 🍪 Cookie')

welcome()

option = int(input('What would you like to order? '))
print(get_item(option))