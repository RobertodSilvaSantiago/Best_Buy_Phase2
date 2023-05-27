from abc import ABC, abstractmethod


class Promotion(ABC):
    """Represent the promotion applied for a certain product."""
    name = "Promotion"

    # A method imposed in all the child class.
    @abstractmethod
    def apply_promotion(self, product, quantity):
        """Returns the discounted price after promotion was applied."""
        pass


class SecondHalfPrice(Promotion):
    """Represents the discount for the second quantity for half the price."""
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        # Calculate the discounted price for the second item at half price promotion
        # For every two items, one item will be at half price
        discounted_price = 0.0
        if quantity >= 2:
            full_price_quantity = quantity // 2  # Number of items at full price
            half_price_quantity = quantity - full_price_quantity  # Number of items at half price
            discounted_price = (full_price_quantity * product.price) + (half_price_quantity * product.price / 2)
        else:
            discounted_price = product.price * quantity

        return discounted_price


class ThirdOneFree(Promotion):
    """Represents the discount for the third quantity for free."""
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        # Calculate the discounted price for the buy 2, get 1 free promotion
        # For every three items, one item will be free
        full_price_quantity = quantity // 3  # Number of items at full price
        free_quantity = quantity - full_price_quantity  # Number of free items
        discounted_price = full_price_quantity * product.price

        return discounted_price


class PercentDiscount(Promotion):
    """Represents the discount indicated in the percent."""
    def __init__(self, name, percent):
        self.name = name
        self.percent = percent

    def apply_promotion(self, product, quantity):
        # Calculate the discounted price for the percentage discount promotion
        discount = self.percent / 100.0
        discounted_price = product.price * quantity * (1 - discount)

        return discounted_price