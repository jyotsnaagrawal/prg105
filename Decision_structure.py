# You are writing a program to sell tickets to the school play. If the person buying the tickets is a student,
# their price is $5.00 per ticket. If the person buying the tickets is a veteran, their price is $7.00 per ticket.
# If the person buying the ticket is a sponsor of the play, the price is $2.00 per ticket.
# If the person buying the ticket is a part of the general public,
# the price is $10.00. Seniors (Retiree) price is $6.00.
# In addition, quantity discounts apply.
# Prices by who is purchasing the tickets:
# Student: $5.00
# Veteran: $7.00
# Show Sponsor: $2.00
# Retiree: $6.00
# General public: $10.00
# Quantity Discounts:
# People buying 4 - 8 tickets get a 10% discount.
# People buying 9-15 tickets get a 15% discount.
# People buying more than 15 tickets get a 20% discount.

print("PLAY PRICES PER TICKET")
print(" 1. Student $ 5.00")
print(" 2. Veteran $7.00")
print(" 3. Show Sponsor $2.00")
print(" 4. Retiree $6.00")
print(" 5. General public $10.00")

buyers_category = int(input("\nPlease enter the number of the category you fit purchasing ticket: "))
quantity = int(input("How many tickets would you like to buy? "))

price = 0.00
if buyers_category == 1:
    price = 5.00
elif buyers_category == 2:
    price = 7.00
elif buyers_category == 3:
    price = 2.00
elif buyers_category == 4:
    price = 6.00
elif buyers_category == 5:
    price = 10.00
# calculating cost
cost = price * quantity
print(f"\nCost before any discounts were applied: ${cost:.2f}")
discount = 0
if quantity in range(4, 8):
    discount = 10
elif quantity in range(9, 15):
    discount = 15
elif quantity > 15:
    discount = 20

cost_after_discount = cost * (100 - discount) / 100

print(f"Your cost after all discounts were applied: ${cost_after_discount:.2f}")
print(f"Your price is ${cost_after_discount / quantity:.2f} per ticket")
