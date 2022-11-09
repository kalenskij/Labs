from datetime import datetime
import json


class Pizza:

    def __init__(self):
        self.possible_extra_ingredients = {
                                  "tomatoes": 10,
                                  "mushrooms": 15,
                                  "pickles": 5,
                                  "sausages": 20,
                                  "souse": 3,
                                  "pineapples": 10,
                                  "meat": 10
                                  }
        self.ingredients = []
        self.extra_ingredients = []
        self.price = 0
        self.name = ""

    def __str__(self):
        if not self.extra_ingredients:
            return f"{self.name}:\
                    \ningredients: {', '.join(map(str, self.ingredients))}\
                    \nPrice: {self.final_price()}"
        else:
            return f"{self.name}:\
            \nIngredients: {', '.join(map(str, self.ingredients)) +', ' + ', '.join(map(str, self.extra_ingredients))}\
            \nPrice: {self.final_price()}"

    def add_ingredient(self, *args):
        for ingredient in args:
            if not isinstance(ingredient, str):
                raise TypeError("Wrong extra ingredient type")
            if ingredient not in self.possible_extra_ingredients.keys():
                raise ValueError("No such extra ingredient")
            self.extra_ingredients.append(ingredient)

    def final_price(self):
        return self.price + sum(self.possible_extra_ingredients[ingredient] for ingredient in self.extra_ingredients)


class ChicagoPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = "Chicago Pizza"
        self.ingredients = ["mushrooms", "meat"]
        self.price = 100


class PeperoniPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = "Peperoni Pizza"
        self.ingredients = ["peperoni", "meat"]
        self.price = 110


class HavaiiPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = "Havaii Pizza"
        self.ingredients = ["pineapples", "meat"]
        self.price = 120


class MargarittaPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = "Margaritta Pizza"
        self.ingredients = ["tomatoes", "meat"]
        self.price = 90


class MeatPizza(Pizza):
    title = "Meat pizza"

    def __init__(self):
        super().__init__()
        self.name = "Meat Pizza"
        self.ingredients = ["meat"]
        self.price = 100


class MexicanoPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = "Mexicano Pizza"
        self.ingredients = ["sausages", "meat"]
        self.price = 105


class BavarPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = "Bavar Pizza"
        self.ingredients = ["pickles", "meat"]
        self.price = 95


class Order:

    def __init__(self, *args):
        self.__pizzas = []
        for pizza in args:
            self.add_pizza(pizza)

    def __str__(self):
        pizza_list = '\n\n'.join(map(str, self.__pizzas))
        return f"Order:\n\
                \n{pizza_list}\n\
                \nOverall price: {self.order_price()}"

    def add_pizza(self, pizza):
        if not isinstance(pizza, Pizza):
            raise TypeError("Not pizza in order")
        self.__pizzas.append(pizza)

    def order_price(self):
        return sum(pizza.final_price() for pizza in self.__pizzas)


def pizza_of_the_day():
    with open("pizzaoftheday.json", "r", encoding="utf-8") as file:
        list = json.load(file)
    return eval(list[datetime.today().strftime("%A")])()


b = pizza_of_the_day()
b.add_ingredient("tomatoes")
d = ChicagoPizza()
d.add_ingredient("mushrooms")
o1 = Order(b, d)
print(o1)