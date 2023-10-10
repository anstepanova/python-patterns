class Pizza:
    def __init__(self):
        self.filling = []

    def __repr__(self):
        return ', '.join(self.filling)


class PizzaBuilder:
    def __init__(self):
        self._pizza = Pizza()

    @property
    def pizza(self):
        return self._pizza

    def add_cheese(self):
        pass

    def add_ketchup(self):
        pass

    def add_mozzarella(self):
        pass

    def add_tomatoes(self):
        pass

    def add_pepperoni(self):
        pass


class PepperoniPizzaBuilder(PizzaBuilder):
    def add_ketchup(self):
        self._pizza.filling.append('ketchup')

    def add_pepperoni(self):
        self._pizza.filling.append('pepperoni')

    def add_cheese(self):
        self._pizza.filling.append('cheese')


class MozzarellaPizzaBuilder(PizzaBuilder):
    def add_ketchup(self):
        self._pizza.filling.append('ketchup')

    def add_mozzarella(self):
        self._pizza.filling.append('mozzarella')

    def add_tomatoes(self):
        self._pizza.filling.append('tomatoes')

    def add_cheese(self):
        self._pizza.filling.append('cheese')


class CustomPizzaBuilder(PizzaBuilder):
    def add_cheese(self):
        self._pizza.filling.append('cheese')

    def add_ketchup(self):
        self._pizza.filling.append('ketchup')

    def add_mozzarella(self):
        self._pizza.filling.append('mozzarella')

    def add_tomatoes(self):
        self._pizza.filling.append('tomatoes')

    def add_pepperoni(self):
        self._pizza.filling.append('pepperoni')


def build_pizza(builder: PizzaBuilder):
    builder.add_ketchup()
    builder.add_pepperoni()
    builder.add_tomatoes()
    builder.add_mozzarella()
    builder.add_cheese()
    return builder.pizza


def build_custom_pizza():
    builder = CustomPizzaBuilder()
    builder.add_ketchup()
    builder.add_pepperoni()
    builder.add_tomatoes()
    builder.add_mozzarella()
    builder.add_cheese()
    return builder.pizza


if __name__ == '__main__':
    mozzarella_pizza = build_pizza(MozzarellaPizzaBuilder())
    print(f'Mozzarella pizza: {mozzarella_pizza}')
    pepperoni_pizza = build_pizza(PepperoniPizzaBuilder())
    print(f'Pepperoni pizza: {pepperoni_pizza}')
    custom_pizza = build_custom_pizza()
    print(f'Custom pizza: {custom_pizza}')
