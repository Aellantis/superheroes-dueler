import random
from hero import Hero


class Team():
  def __init__(self, name: str):
    self.name = name
    self.heroes = []

  def add_hero(self, hero):
    self.heroes.append(hero)

  def remove_hero(self, name):
    foundHero = False
    for hero in self.heroes:
      if hero.name == name:
        self.heroes.remove(hero)
        foundHero = True
    if not foundHero:
        return 0
    
  def view_all_heroes(self):
    if len(self.heroes) > 0:
      for hero in self.heroes:
        print(hero.name)
    else:
      return "No heroes Found"
        
  def stats(self):
    for hero in self.heroes:
      if hero.deaths == 0:
        kd = hero.kills
      else:
        kd = hero.kills / hero.deaths
        print(f"{hero.name} Kill/Deaths:{kd}")

  def revive_heroes(self, health=100):
    for hero in self.heroes:
      hero.current_health = hero.starting_health

  def attack(self, other_team):
    living_heroes = []
    living_opponents = []

    for hero in self.heroes:
      living_heroes.append(hero)

    for hero in other_team.heroes:
      living_opponents.append(hero)

    while len(living_heroes) > 0 and len(living_opponents) > 0:
      fighting_hero = random.choice(living_heroes)
      fighting_opponent = random.choice(living_opponents)

      fighting_hero.fight(fighting_opponent)

      if fighting_hero.current_health < 0:
        living_heroes.remove(fighting_hero)

      elif fighting_opponent.current_health < 0:
        living_opponents.remove(fighting_opponent)
        
      else:
        pass

      self.stats()
      other_team.stats()

      if len(living_heroes) >= 0:
        print(f"{self.name} won!!")

      elif len(living_opponents) >= 0:
        print(f"{other_team.name} won!!")