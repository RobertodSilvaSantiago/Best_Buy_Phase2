import products


class Store:
    """
    Represents a store that sells products.

    Attributes:
        products(list): List of the product that exist in the store.
    """
    def __init__(self, products_list):
        self.products = list(products_list)

    def add_product(self, product):
        """Adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self):
        """Returns the total quantity of items in the store."""
        total_quantity = int(0)
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        """Returns a list of all active products in the store."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    @staticmethod
    def order(shopping_list):
        """Buys the products based on the shopping list and returns the total price of the order."""
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price = product.buy(quantity)
        return float(total_price) 


if __name__ == "__main__":
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products[0], 1), (products[1], 2)]))