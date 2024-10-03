books = [
  'Zero to One',
  'The Lean Startup',
  'The Mom Test',
  'Make It Stick',
  'Life in Code'
]
print(books)
# ['Zero to One', 'The Lean Startup', 'The Mom Test', 'Make It Stick', 'Life in Code']

books.append('Zero to Sold')
print(books)
# ['Zero to One', 'The Lean Startup', 'The Mom Test', 'Make It Stick', 'Life in Code', 'Zero to Sold']

books.remove('Zero to One')
books.pop(0)
print(books)
# ['The Mom Test', 'Make It Stick', 'Life in Code', 'Zero to Sold']