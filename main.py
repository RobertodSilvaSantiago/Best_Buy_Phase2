import sys
import products
import store
import promotions


class SantiagoStore:
    def __init__(self):
        self.product_list = [
            products.Product("MacBook Air M2", price=1450, quantity=100),
            products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
            products.Product("Google Pixel 7", price=500, quantity=250),
            products.NonStockedProduct("Windows License", price=125),
            products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
        ]

        second_half_price = promotions.SecondHalfPrice("Second Half price!")
        third_one_free = promotions.ThirdOneFree("Third One Free!")
        thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

        self.product_list[0].set_promotion(second_half_price)
        self.product_list[1].set_promotion(third_one_free)
        self.product_list[3].set_promotion(thirty_percent)

        self.best_buy = store.Store(self.product_list)

    def display_product_list(self):
        print("---------- Product List ----------")
        for index, product in enumerate(self.best_buy.products, start=1):
            print(f"Product #{index}: {product.show()}")
        print("----------------------------------")

    def display_total_quantity(self):
        total_quantity = self.best_buy.get_total_quantity()
        print(f"Total items in store: {int(total_quantity)}")

    def make_order(self):
        order_list = []
        self.display_product_list()
        print("Enter an empty text to finish the order.")

        while True:
            product_num = input("Select the product number: ")
            if not product_num:
                break

            try:
                product_num = int(product_num)
                if product_num < 1 or product_num > len(self.best_buy.products):
                    raise ValueError("Invalid product number. Please try again.")
            except ValueError as error:
                print(f"Error: {str(error)}")
                continue

            quantity = input("Enter the quantity: ")
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    raise ValueError("Invalid quantity. Please enter a positive quantity.")
            except ValueError as error:
                print(f"Error: {str(error)}")
                continue

            product = self.best_buy.products[product_num - 1]
            if quantity > product.quantity:
                print("Insufficient quantity available.")
                continue

            order_list.append((product, quantity))
            print("Product added to the order list!")

        try:
            total_price = sum(product.buy(quantity) for product, quantity in order_list)
            formatted_price = f"{total_price:.2f}"
            print(f"Order successfully made! Total payment: ${formatted_price}")
        except ValueError as error:
            print(f"Error: {str(error)}")

    def check_product_exists(self):
        product_name = input("Enter the product name to check: ")
        exists = any(product.name.lower() == product_name.lower() for product in self.best_buy.products)
        if exists:
            print(f"The product '{product_name}' exists in the store.")
        else:
            print(f"The product '{product_name}' does not exist in the store.")

    @staticmethod
    def exit_program():
        print("Thank you for visiting our store")
        sys.exit()

    def start(self):
        print("Welcome to Santiago Store!")
        while True:
            try:
                print("  Store Menu\n  ------- \n1. List all products in store\n"
                    "2. Show total amount in store\n3. Make an order\n4. Check if a product exists\n5. Quit")

                functions = {
                    1: self.display_product_list,
                    2: self.display_total_quantity,
                    3: self.make_order,
                    4: self.check_product_exists,
                    5: self.exit_program,
                    6: self.combine_stores
                }

                user_choice = input("Please choose a number: ")
                if user_choice.isdigit():
                    user_choice = int(user_choice)
                    if user_choice in functions:
                        functions[user_choice]()
                    else:
                        print("Invalid choice. Please select a number from the menu.")
                else:
                    print("Invalid input. Please enter a number.")

            except ValueError:
                print("\033[31m" + "Error! Please choose from numbers 1 to 5." + "\033[0m")

            # Add exception handling for unexpected errors
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")
                
    def combine_stores(self):
        print("Combining two stores")
        second_store = SantiagoStore()
        combined_products = self.best_buy.products + second_store.best_buy.products
        combined_store = store.Store(combined_products)
        print("Stores combined successfully!")

        print("Displaying combined product list:")
        for index, product in enumerate(combined_store.products, start=1):
            print(f"Product #{index}: {product.show()}")

        print("Displaying total quantity in combined store:")
        total_quantity = combined_store.get_total_quantity()
        print(f"Total items in combined store: {int(total_quantity)}")

        print("Displaying total price in combined store:")
        total_price = combined_store.get_total_price()
        formatted_price = f"{total_price:.2f}"
        print(f"Total price in combined store: ${formatted_price}")

        print("Sorting the combined store based on price:")
        combined_store.sort_products_by_price()
        self.display_product_list()

    def __gt__(self, other):
        return self.best_buy.total_price > other.best_buy.total_price

    def __lt__(self, other):
        return self.best_buy.total_price < other.best_buy.total_price


if __name__ == "__main__":
    tech_store = SantiagoStore()
    tech_store.start()

