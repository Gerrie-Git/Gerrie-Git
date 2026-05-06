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
    def __init__(self, name, type: CharacterType, health=100, attackpower=50):
        self.name = name
        self.health = health
        self.type = type
        self.attackpower = attackpower

class enemy:
    def __init__(self, name, type: Enemy, health=100, attackpower=50):
        self.name = name
        self.type = type
        self.health = health
        self.attackpower = attackpower


# combat loop

def combat(hero, enemy):
    
    while hero.health >= 0 and enemy.health >= 0:

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

        if hero.health == 0:
            print(f"The enemy {enemy.name} has won the match")
        else:
            print(f"The hero {hero.name} has won the match")

#print(CharacterType.WARRIOR.value)
Hero1 = hero("Batman", CharacterType.WARRIOR.value, 100, 20)
Enemy1 = enemy("The Joker", Enemy.ZOMBIE.value, 100, 15)

combat(Hero1, Enemy1)