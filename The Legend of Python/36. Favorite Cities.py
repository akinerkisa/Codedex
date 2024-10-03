class City:
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

ankara = City('Ankara', 'Turkey', 5445000, ['Anitkabir', 'Kocatepe Mosque', 'Ataturk Forest Farm'])

istanbul = City('Istanbul', 'Turkey', 15519267, ['Hagia Sophia', 'Topkapi Palace', 'Galata Tower'])

print(vars(ankara))

print(vars(istanbul))