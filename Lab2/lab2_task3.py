class Product:

    def __init__(self, price, description, length, width, height):
        self.price = price
        self.description = description
        self.length = length
        self.width = width
        self.height = height

    @property
    def price(self):
        return self.__price

    @property
    def description(self):
        return self.__description

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @price.setter
    def price(self, price):
        if not isinstance(price, float):
            raise TypeError("Not float")
        if not price > 0:
            raise ValueError("Value Error")
        self.__price = price

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError("Not String")
        if not description:
            raise ValueError("Empty description")
        self.__description = description

    @length.setter
    def length(self, length):
        if not isinstance(length, float):
            raise TypeError("Not float")
        if not 0 <= length <= 20:
            raise ValueError("Wrong value")
        self.__length = length

    @width.setter
    def width(self, width):
        if not isinstance(width, float):
            raise TypeError("Not float")
        if not 0 <= width <= 20:
            raise ValueError("Wrong value")
        self.__width = width

    @height.setter
    def height(self, height):
        if not isinstance(height, float):
            raise TypeError("Not float")
        if not 0 <= height <= 20:
            raise ValueError("Wrong value")
        self.__width = height


class Customer:

    def __init__(self, name, surname, patronymic, mobile_number):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.mobile_number = mobile_number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Not String")
        if not name:
            raise ValueError("Empty name")
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Not String")
        if not surname:
            raise ValueError("Empty surname")
        self.__surname = surname

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        if not isinstance(patronymic, str):
            raise TypeError("Not String")
        if not patronymic:
            raise ValueError("Empty patronymic")
        self.__patronymic = patronymic

    @property
    def mobile_number(self):
        return self.__mobile_number

    @mobile_number.setter
    def mobile_number(self, mobile_number):
        if not isinstance(mobile_number, str):
            raise TypeError("Not String")
        if not mobile_number:
            raise ValueError("Empty mobile_number")
        self.__mobile_number = mobile_number


class Order:
    
    def __init__(self, customer, *args):
        self.customer = customer
        self.products = args

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

    @products.setter
    def products(self, products):
        if not all(isinstance(item, Product) for item in products):
            raise TypeError("Not Product")
        if not products:
            raise ValueError("Empty products")
        self.__products = products

    def calculate_price(self):
        return sum(item.price for item in self.products)


product1 = Product(125.0, "Apple", 10.0, 20.0, 5.0)
product2 = Product(5.0, "Cheese", 1.0, 15.0, 6.0)
customer1 = Customer("Dmytrii", "Hohlov", "Andriiovych", "+380950340447")
order1 = Order(customer1, product1, product2)
print(order1.calculate_price())
