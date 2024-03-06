#Week Three Assignment Solution

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        discounted_price = price - discount_amount
        return discounted_price
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Call the calculate_discount function
    final_price = calculate_discount(original_price, discount_percent)
    
    #final price after applying the discount, or the original price if no discount was applied
    print(f"Final price after applying the discount: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter valid numerical values.")
