from Pokemon_Proj.pokemon_general_class import Pokemon
import random


class YourPokemon(Pokemon):
    def __init__(self,name, level, type, gender, hp, exp, damage):
        super().__init__(name, level, type, gender, hp, damage)
        self.__exp = exp

    def display_info(self):
        print("Name:{}, Level:{}, Type:{}, Gender:{}, Hp:{}, Exp:{}, Damage:{}".format(self.name, self.get_level(), self.type, self.gender, self.hp, self.__exp, self.damage))

    def get_exp(self):
        return int(self.__exp)

    def add_exp(self):
        self.__exp =+ random.randint(1, 35)

    def add_damage(self):
        self.damage =+ random.randint(100, 1000)
