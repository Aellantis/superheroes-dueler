from ability import Ability
from armor import Armor
import random

class Hero:
  def __init__(self, name:str, starting_health:int):
    self.abilities = list()
    self.armors = list()
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

  def fight(self, opponent):
    winner = random.choice([self, opponent])
    return f"{winner.name} wins!"
  
  def add_ability(self, ability):
    self.abilities.append(ability)
  
  def attack(self):
    total_damage = 0
    for ability in self.abilities:
        total_damage += ability.attack()
    return total_damage
  
  def add_armor(self, armor):
    self.armors.append(armor)
  
  def defend (self):
     total_blocked = 0
     for blocked_damage in self.armors:
        total_blocked += blocked_damage.block()
        if self.starting_health == 0:
           print("Your hero is dead. It can't defend!")
     return total_blocked

if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    armor = Armor("Debugging Armor", 70)
    another_armor = Armor ("Coding Armor", 80)
    hero = Hero("Grace Hopper", 200)
    hero.add_armor(armor)
    hero.add_armor(another_armor)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())
    print(hero.defend())
  
# if __name__ == "__main__":
#     hero1 = Hero("Wonder Woman", 300)
#     hero2 = Hero("Dumbledore", 250)

#     print(hero1.fight(hero2))

# # if __name__ == "__main__":
# #   my_hero = Hero("Grace Hopper", 200)
# #   print(my_hero.name)
# #   print(my_hero.current_health)