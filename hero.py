import random

class Hero:
  def __init__(self, name, starting_health=100):
    self.name = name
    self.current_health = starting_health

  def fight(self, opponent):
    winner = random.choice([self, opponent])
    return f"{winner.name} wins!"
    
if __name__ == "__main__":
    hero1 = Hero("Wonder Woman", 300)
    hero2 = Hero("Dumbledore", 250)

    print(hero1.fight(hero2))

# if __name__ == "__main__":
#   my_hero = Hero("Grace Hopper", 200)
#   print(my_hero.name)
#   print(my_hero.current_health)