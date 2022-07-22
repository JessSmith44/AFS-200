# Prompt the user to enter a description for a product.

product = input('Please enter product description: ')
# Prompt the user to enter the quantity being purchased. 

quantity = int(input(f'Please enter the quantity of the {product} being purchased: '))
# Be sure to display the product to the user during the prompt.
# Store the value as an integer.

# Prompt the user to enter the regular price of the product. This value must be stored as a float.
price = float(input('Please enter the regular price of this item: '))

# All of the products over $19.99 are 15% OFF
# All of the products over $39.99 are 25% OFF
if price> 39.99:
    discountPrice = price * .75
    print('Great news! You get 25 percent off.')
elif price> 19.99:
    discountPrice = price * .85
    print('Great news! You get 15 percent off.')
else:
    discountPrice = price
    # below this line, something is going wrong. calculations are off for discount total
    # resolve discountTotal issue!!!!!!
discountTotal = quantity * discountPrice

# Calculate the sales tax on the total purchase.  
    # Assume a state sales tax rate of 6.5%.  
    # The rate should be calculated on the total price of the products after discount savings.
    # Store this value as float in a variable.  780 585
total = float(quantity * price)
savings = float(total - discountTotal)
# print(total)
# print(savings)

tax = float(discountTotal * .065)

finalTotal = float(discountPrice + tax)

# Display the total amount due from the customer.

print(f"Your Receipt \n {quantity} {product}s at ${discountPrice:,.2f} \n Sales Tax ${tax:,.2f} \n Total amount due ${discountTotal:,.2f} \n You Saved ${savings:,.2f} Today.")

# Format the output as a fixed point number with two-decimal places, a comma as a thousand separator and the dollar sign.
# Display the total amount saved. 780 - 195