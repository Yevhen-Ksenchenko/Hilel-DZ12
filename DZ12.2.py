class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}: {self.price}: {self.description}: {self.dimensions}"


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name}: {self.surname}: {self.numberphone}"


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        result = f"User: {self.user.name} {self.user.surname}\nItems:\n"
        for item, cnt in self.products.items():
            result += f"\t{item.name}: {cnt} pcs.\n"
        return result

    def get_total(self):
        return sum(item.price * cnt for item, cnt in self.products.items())


pinapple = Item("pinapple", "6", "yellow", "big")
lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
orange = Item('orange', 3, "orange", "large", )
print(pinapple)
print(lemon)
print(apple)
print(orange)

buyer = User("Ivan", "Ivanov", "02628162")
buyer_2 = User("Yevhen", "Ksenchenko", "555555555")
print(buyer)
print(buyer_2)

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40
print('ok')
