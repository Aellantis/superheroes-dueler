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
  
  def take_damage(self, damage):
    damage_taken = damage - self.defend() 
    self.current_health -= max(damage_taken,0)
    return self.current_health
  
  def is_alive(self):
    if self.current_health <= 0:
      return False
    else:
      return True
    
if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())