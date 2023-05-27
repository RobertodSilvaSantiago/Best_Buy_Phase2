import pytest
from products import Product


def test_normal_product():
    """Test that creating a normal product works."""
    assert Product("Meta-Quest 2 Advanced Virtual Reality Headset", price=430, quantity=50)


def test_invalid_details():
    """Test that creating a product with invalid details"""

    # Product name is empty
    with pytest.raises(ValueError, match="Name cannot be empty"):
        Product("", price=250, quantity=50)

    # Product price is negative
    with pytest.raises(ValueError, match="Price cannot be negative"):
        Product("Acer Predator Triton", price=-900, quantity=50)

    # Product quantity is negative
    with pytest.raises(ValueError, match="Quantity cannot be negative"):
        Product("Acer Predator Triton", price=900, quantity=-50)


def test_product_deactivate():
    """Test that when a product reaches 0 quantity, it becomes inactive."""
    # Create an instance of the Product class with a quantity of 1
    product = Product("Intel Core i7-12700KF", price=236, quantity=1)

    # Check if the product is initially active
    assert product.is_active() is True

    # Set the quantity of the product to 0
    product.set_quantity(0)

    # Check if the product is now inactive
    assert product.is_active() is False


def test_product_modifies():
    """Test that product purchase modifies the quantity and returns the right output."""
    product = Product("MSI PRO Z690-A", price=190, quantity=5)
    product.buy(3)
    assert product.get_quantity() == 2


def test_buy_large_quantity():
    """Test that buying a larger quantity than exists invokes exception."""
    product = Product("Kingston ValueRAM", price=27, quantity=2)
    with pytest.raises(ValueError, match="Not enough quantity available."):
        product.buy(50)


pytest.main()