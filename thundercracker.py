from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(0)
        self.spend_attack(0)
        self.spend_defence(100)
        self.add_move(High_voltage())
        self.add_move(Thunder_attack())
        self.add_move(Electrocute())
        self.add_move(Tesla_electricity())
        self.set_type(Type.FIRE)
        self.move = 0
        self.moves = ['High_voltage!!', "Thunder_attack!!", "Electrocute!!", "Tesla_electricity!!"]


    def get_name(self):
        return "Thundercracker"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class High_voltage(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "High_voltage"

class Thunder_attack(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Thunder_attack"


class Electrocute(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Electrocute!!"


class Tesla_electricity(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Tesla electricity!"