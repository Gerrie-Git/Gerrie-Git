from enum import Enum
from random import random, randomint


class CharacterType(Enum):
    WARRIOR = 0
    MAGE = 1
    ROGUE = 2

class AttackType(Enum):
    PHYSICAL = 0
    MAGICAL = 1
    POISON = 2

class BattleStatus(Enum):
    ONGOING = 0
    HERO_WIN = 1
    MONSTER_WIN = 2

class Character:
    
    def __init__(self, name: str, hp:int , max_hp:int, attack_power:int):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.attack_power = attack_power

    def hp_bar(self):
        self.hp_bar = 100


    def take_damage():
        pass

    def is_alive():
        pass

    def __str__():
        pass

class Hero:

    def __init__(self, CharacterClass, special_abillity):
        self.CharacterClass = CharacterClass.value
        self.special_ability = special_abillity

class Monster:
    def __init__(self, MonsterType):
        self.MonsterType = MonsterType

    def rage_mechanic(self):
        pass

class Battle:
    def __init__(self, hero, monster):
        self.hero - hero
        self.monster = monster

    def hero_turn():
        pass

    def monster_turn():
        pass

    def check_status():
        pass

    def start():
        pass

        # 1: randomly select monster or hero to start
        # 2: selected hero or monster attacks
        #   -> randomly select an integer as the attack power 
        #   -> decrease the attack power from the other players total health
        # 3: Other player roles the dice to attack
        #    -> randomly select an integer as the attack power 
        #   -> decrease the attack power from the other players total health
