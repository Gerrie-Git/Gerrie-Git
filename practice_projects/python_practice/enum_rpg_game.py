from enum import Enum
from random import random, randint


class CharacterType(Enum):
    WARRIOR = "Warrior"
    MAGE = "Mage"
    ROGUE = "Rogue"

class Enemy(Enum):
    MONSTER = "Monster"
    ZOMBIE = "Zombie"
    WEREWOLF = "Werewolf"

class Item(Enum):
    WEAPON = 0
    POTION = 1
    ARMOR = 2

class GameState(Enum):
    EXPLORING = 0
    COMBAT = 1
    GAMEOVER = 2


class hero:
    def __init__(self, name, type: CharacterType, health=100, attackpower=20):
        self.name = name
        self.health = health
        self.type = type
        self.attackpower = attackpower

    def use_item(self):
        rand = randint(0,2)
        print(rand)
        if rand== Item.WEAPON.value:
            self.attackpower += 20
            print(f"The hero drank up a potion and has a new attackpower of {self.attackpower}")
        elif rand == Item.POTION.value:
            self.health += 25
            print(f"The hero drank a potion and his health is now {self.health}")
        elif rand == Item.ARMOR.value:
            self.health += 10
            print(f"The hero picked up the armor and has a higher health of {self.health}")



class enemy:
    def __init__(self, name, type: Enemy, health=100, attackpower=20):
        self.name = name
        self.type = type
        self.health = health
        self.attackpower = attackpower


# combat loop

def combat(hero, enemy):
    
    while hero.health > 0 and enemy.health > 0:

        # player rolls the dice
        playerattack = randint(0, hero.attackpower)
        # player one attacks
        print(f"{hero.name} hits {enemy.name} for {playerattack} points")
        enemy.health -= playerattack
        print(f"{enemy.name} has {enemy.health} points left")

        # player rolls the dice
        enemyattack = randint(0, enemy.attackpower)
        #enemy attackes
        print(f"{enemy.name} hits {hero.name} for {enemyattack} points")
        hero.health -= enemyattack
        print(f"{hero.name} has {hero.health} points left")

        hero.use_item()

        if hero.health <= 0:
            print(f"The enemy {enemy.name} has won the match")
            break
        elif enemy.health <= 0:
            print(f"The hero {hero.name} has won the match")
            break
        else:
            print(f"The match carries on!")

#print(CharacterType.WARRIOR.value)
Hero1 = hero("Batman", CharacterType.WARRIOR.value, 100, 20)
Enemy1 = enemy("The Joker", Enemy.ZOMBIE.value, 100, 15)

combat(Hero1, Enemy1)