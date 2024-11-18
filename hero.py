class Hero:
  def __init__(self, name, starting_health=100):
    self.name = name
    self.current_health = starting_health

if __name__ == "__main__":
  my_hero = Hero("Grace Hopper", 200)
  print(my_hero.name)
  print(my_hero.current_health)