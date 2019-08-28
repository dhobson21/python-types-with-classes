#Create a Pizza type for representing pizzas in Python. Think about some basic properties that would define a pizza's values; things like size, crust type, and toppings would help. Define those in the __init__ method so each instance can have its own specific values for those properties.

class Pizza:

    def __init__(self):
        self.size = 0,
        self.style = "",
        self.crust_type = "",
        self.toppings = list()
        self.sauce = ""

    def add_toppings(self, topping):
        self.toppings.append(topping)




    def print_order(self):
        s = " and "
        print(f"I would like a {self.size}-inch, {self.style} pizza with {self.crust_type} crust, {self.sauce} sauce, {s.join(self.toppings)}")

meat_lovers =Pizza()
meat_lovers.sauce = "marinara"
meat_lovers.size = 16
meat_lovers.crust_type = "thick"
meat_lovers.style = "deep-dish"
meat_lovers.add_toppings("onions")
meat_lovers.add_toppings("pepperoni")
meat_lovers.print_order()
