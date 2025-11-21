class Burger:
    def __init__(self):
        self.meat = False
        self.salad = False
        self.cheese = False

    def __str__(self):
        return f"Burger: meat={self.meat}, salad={self.salad}, cheese={self.cheese}"


class BurgerBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.burger = Burger()

    def add_meat(self):
        self.burger.meat = True

    def add_salad(self):
        self.burger.salad = True

    def add_cheese(self):
        self.burger.cheese = True

    def build(self):
        result = self.burger
        self.reset()
        return result


class Director:
    def __init__(self, builder: BurgerBuilder):
        self.builder = builder

    def make_classic_burger(self):
        self.builder.add_meat()
        self.builder.add_salad()
        self.builder.add_cheese()

    def make_simple_burger(self):
        self.builder.add_meat()
        self.builder.add_cheese()

    def make_vegan_burger(self):
        self.builder.add_salad()


burger_builder = BurgerBuilder()
director = Director(burger_builder)

director.make_classic_burger()
burger1 = burger_builder.build()
print(burger1)

director.make_simple_burger()
burger2 = burger_builder.build()
print(burger2)

director.make_vegan_burger()
burger3 = burger_builder.build()
print(burger3)