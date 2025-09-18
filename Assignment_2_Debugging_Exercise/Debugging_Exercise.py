# Joe Botelle COP 2373
# Programming Exercise 2: Debugging Exercise

# This program loops through product list, applies discounts, and displays product and discounted price

def calculate_discount(price, discount_rate):

    #Calculate the discount amount based on the price and discount rate.
    discount_amount = price * discount_rate
    return discount_amount

def apply_discount(price, discount_amount):

    #Apply the discount amount to the original price and return the new price.
    new_price = price - discount_amount
    return new_price

def main():

    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": 500, "discount_rate": 0.2}, # Fixed "500" string error
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    for product in products:

        # Add try and except block for error handling

        try:
            price = product["price"]
            discount_rate = product["discount_rate"]

            # Check for correct type

            if type(price) not in [int, float] or type(discount_rate) not in [int, float]:
                print(f"Invalid data type: {product}")
                continue

            # Calculate and apply discount

            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount_amount)

            # Display results

            print(f"Product: {product['name']}")
            print(f"Original Price: ${price:.2f}") # Fixed formatting
            print(f"Discount Amount: ${discount_amount:.2f}") # Fixed formatting
            print(f"Final Price: ${final_price:.2f}\n") # Fixed formatting

        # Error Handling
        except KeyError as e:
            print(f"Missing key: {e} in product: {product}\n")
        except Exception as e:
            print(f"Unexpected error: {product.get('name', 'Unknown')}: {e}\n")


if __name__ == "__main__":
    main()



