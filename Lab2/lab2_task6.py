class Product:
    
    def __init__(self, product_code: int, product_price: int):
        self.product_code = product_code
        self.product_price = product_price

    @property
    def product_code(self):
        return self.__product_code

    @product_code.setter
    def product_code(self, product_code):
        if not isinstance(product_code, int):
            raise TypeError("Product_code TypeError")
        if not product_code or product_code <= 0:
            raise ValueError("Product_code ValueError")
        self.__product_code = product_code
        
    @property
    def product_price(self):
        return self.__product_price
    
    @product_price.setter
    def product_price(self, product_price):
        if not isinstance(product_price, int):
            raise TypeError("Product_price TypeError")
        if not product_price or product_price <= 0:
            raise ValueError("Product_price ValueError")
        self.__product_price = product_price


class Node:

    def __init__(self, product: Product):
        self.left_node = None
        self.product = product
        self.right_node = None

    def __lt__(self, other) -> bool:
        return self.product.product_code < other.product.product_code

    def __gt__(self, other) -> bool:
        return self.product.product_code > other.product.product_code

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, product):
        if not isinstance(product, Product):
            raise TypeError("product TypeError")
        self.__product = product


class BinaryTree:

    def __init__(self):
        self.root_node = None

    def add_node(self, node: Node):
        if not isinstance(node, Node):
            raise TypeError("Node TypeError")
        if not self.root_node:
            self.root_node = node
        else:
            self.__place_node(node, self.root_node)
        return None

    def __place_node(self, new_node, current_node):
        if new_node > current_node:
            if not current_node.right_node:
                current_node.right_node = new_node
            else:
                self.__place_node(new_node, current_node.right_node)
        elif new_node < current_node:
            if not current_node.left_node:
                current_node.left_node = new_node
            else:
                self.__place_node(new_node, current_node.left_node)
        else:
            raise ValueError("Two products with the same code")
        return None

    def __search(self, code, current_node: Node) -> int:
        if code == current_node.product.product_code:
            return current_node.product.product_price
        elif code < current_node.product.product_code:
            return self.__search(code, current_node.left_node)
        else:
            return self.__search(code, current_node.right_node)

    def products_price(self, code: int, quantity: int) -> int:
        return self.__search(code, self.root_node)*quantity


product_list = BinaryTree()
number_of_products = int(input("Enter number of products: "))
for counter in range(number_of_products):
    print(f"Product number: {counter+1}")
    code, price = int(input("Enter product code: ")), int(input("Enter product price: "))
    product_list.add_node(Node(Product(code, price)))
print(product_list.products_price(3, 10))
