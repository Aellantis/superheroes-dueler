from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
  def __init__(self, name:str, starting_health:int=100):
    self.abilities = list()
    self.armors = list()
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health
    self.kills: int = 0
    self.deaths: int = 0

  def fight(self, opponent):
        while self.is_alive() == True and opponent.is_alive() == True:
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            print(f"{self.name} has {self.current_health} hp and {opponent.name} has {opponent.current_health} hp")

        if opponent.is_alive() == False:
            self.add_kill()
            opponent.add_death()
            print(f"{self.name} won!")

        if self.is_alive() == False:
            opponent.add_kill()
            self.add_death()
            print(f"{opponent.name} won!")
  
  def attack(self):
    total_damage = 0
    for ability in self.abilities:
        total_damage += ability.attack()
    return total_damage
  
  def add_armor(self, armor):
    self.armors.append(armor)

  def add_ability(self, ability):
    self.abilities.append(ability)

  def add_weapon(self, weapon):
    self.abilities.append(weapon)
  
  def defend (self):
    total_blocked = 0
    for blocked_damage in self.armors:
      total_blocked += blocked_damage.block()
    return total_blocked
  
  def take_damage(self, damage):
    damage_taken = damage - self.defend() 
    self.current_health -= max(damage_taken, 0)
    return self.current_health
  
  def is_alive(self):
    if self.current_health <= 0:
      return False
    else:
      return True
    
  def add_kill(self):
    self.kills += 1

  def add_death(self):
    self.deaths += 1

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)