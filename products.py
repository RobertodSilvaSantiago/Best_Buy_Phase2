class Product:
    """
    Represents the available type of product in the store

    Attributes:
        name(str): Name of the product.
        price(float): Price of the product.
        quantity(int): Number of stocks available in the store.
    """
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_promotion(self):
        """Getter function for promotion and returns the promotion variable."""
        return self.promotion

    def set_promotion(self, promotion):
        """Setter function for promotion."""
        self.promotion = promotion

    def get_quantity(self):
        """Getter function for quantity and returns the quantity variable in float"""
        return float(self.quantity)

    def set_quantity(self, quantity):
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""
        self.quantity = int(quantity)
        if self.quantity == 0:
            self.deactivate_product()

    def is_active(self):
        """Getter function for active. Returns True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate_product(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Returns a string that represents the product."""
        promotion_info = f"Promotion: {self.promotion.name}" if self.promotion else "No promotion"
        return f'{self.name}, Price: {self.price}, Quantity: {self.quantity}, {promotion_info}'

    def buy(self, quantity) -> float:
        """Buys the given quantity of the product."""
        if quantity <= 0:
            raise ValueError("Quantity to buy must be a positive number.")

        if not self.active:
            raise Exception("Cannot buy an inactive product.")

        if quantity > self.quantity:
            raise ValueError("Not enough quantity available.")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity  # Subtract the quantity ordered from the available quantity

        return total_price

    def __gt__(self, other):
        """Greater than comparison operator."""
        if isinstance(other, Product):
            return self.price > other.price
        else:
            return NotImplemented

    def __lt__(self, other):
        """Less than comparison operator."""
        if isinstance(other, Product):
            return self.price < other.price
        else:
            return NotImplemented



class NonStockedProduct(Product):
    """Represents the Non-Stocked Product that we don't need to keep track on its quantity."""
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def show(self):
        if self.quantity == 0:
            return f'{self.name}, Price: {self.price}, Quantity: Unlimited'
        else:
            return super().show()


class LimitedProduct(Product):
    """Represents the Limited Products which can only be purchased on the indicated maximum times of order."""
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        return f'{self.name}, Price: {self.price}, Limited to {self.maximum} per order'

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError("Quantity exceeds the maximum limit for this product.")

        if quantity > self.quantity:
            raise ValueError("Not enough quantity available.")

        self.quantity -= quantity
        total_price = self.price * quantity
        return total_price


if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()