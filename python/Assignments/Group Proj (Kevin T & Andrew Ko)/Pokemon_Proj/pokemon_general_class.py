class Pokemon:
    def __init__(self, name, level, type, gender, hp, damage):
        self.name = name
        self.__level = level
        self.type = type
        self.gender = gender
        self.hp = hp
        self.damage = damage

    def display_info(self):
        print("Name:{}, Level:{}, Type:{}, Gender:{}, Hp:{}, Damage:{}".format(self.name, self.get_level(), self.type, self.gender, self.hp, self.damage))

    def display_name(self):
        return self.name

    def add_level(self):
        self.__level += 1

    def get_level(self):
        return int(self.__level)

    def get_hp(self):
        return int(self.hp)
