class Product:

    def __init__(self, price, description, length, width, height):
        self.price = price
        self.description = description
        self.length = length
        self.width = width
        self.height = height

    def __str__(self):
        return f"\nPrice:{self.price}\
                \nDescription: {self.description}\
                \nLength: {self.length} Width: {self.width} Height: {self.height}"

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, float):
            raise TypeError("Not float")
        if not price > 0:
            raise ValueError("Value Error")
        self.__price = price


class Customer:

    def __init__(self, name, surname, patronymic, mobile_number):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.mobile_number = mobile_number

    def __str__(self):
        return f"\n{self.name} {self.surname} {self.patronymic}:\
                \nMobile number: {self.mobile_number}"


class Order:
    
    def __init__(self, customer, *args):
        self.customer = customer
        self.__products = {}
        for product in args:
            self.add_product(product)

    def __str__(self):
        return f"\nOverall price of order: {sum(item.price*self.products[item] for item in self.__products)}"

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Not Customer")
        if not customer:
            raise ValueError("Empty customer")
        self.__customer = customer

    @property
    def products(self):
        return self.__products

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Not product")
        if product in self.__products.keys():
            self.__products[product] += 1
        else:
            self.__products[product] = 1
        return None

    def remove_product(self, product: Product):
        if product not in self.__products.keys():
            raise ValueError("No such product")
        if self.__products[product] > 1:
            self.__products[product] -= 1
        else:
            self.__products.pop(product)


product1 = Product(125.0, "Apple", 10.0, 20.0, 5.0)
product2 = Product(5.0, "Cheese", 1.0, 15.0, 6.0)
customer1 = Customer("Dmytrii", "Hohlov", "Andriiovych", "+380950340447")
order1 = Order(customer1, product1, product2)
order1.add_product(product1)
order1.remove_product(product1)
print(product1)
print(product2)
print(customer1)
print(order1)
