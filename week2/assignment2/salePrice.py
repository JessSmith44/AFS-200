# Prompt the user to enter a description for a product.

product = input('Please enter product description: ')
# Prompt the user to enter the quantity being purchased. 

quantity = int(input('Please enter the quantity of the product being purchased: '))
# Be sure to display the product to the user during the prompt.


# Store the value as an integer.

# Prompt the user to enter the regular price of the product. This value must be stored as a float.
price = float(input('Please enter the regular price of this item: '))

total = float((quantity * price))
# All of the products over $19.99 are 15% OFF
# All of the products over $39.99 are 25% OFF
if total > 39.99:
    discount = float(( 25 / 100 ) * total)
    discountPrice = float(total - discount)
    print('Great news! You get 25 percent off.')
elif total > 19.99:
    discount = float(( 15 / 100 ) * total)
    discountPrice = float(total - discount)
    print('Great news! You get 15 percent off.')

# Calculate the sales tax on the total purchase.  
    # Assume a state sales tax rate of 6.5%.  
    # The rate should be calculated on the total price of the products after discount savings.
    # Store this value as float in a variable.
savings = float(total - discountPrice)

tax = float(total * .065)

finalTotal = float(discountPrice + tax)

# Display the total amount due from the customer.

print(f"Your Receipt \n {quantity} {product}s at {price:,.2f} \n Sales Tax ${tax:,.2f} \n Total amount due ${finalTotal:,.2f} \n You Saved ${savings:,.2f} Today.")

# Format the output as a fixed point number with two-decimal places, a comma as a thousand separator and the dollar sign.
# Display the total amount saved.