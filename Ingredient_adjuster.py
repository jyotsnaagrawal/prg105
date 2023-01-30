#  Chocolate Chip Cookies Recipe
# First tell the users what recipe this is and ask for desired servings.
print("This program will calculate the ingredients required to", "Chocolate Chip Cookies" )


# input from user desired_servings
desired_servings = int(input('How many Cookies would you like to make: '))

# these are the given ingredient amounts
creamy_peanut_butter = 1  # cup
granulated_sugar = 1  # cup
large_eggs = 2
semi_sweet_chocolate_chips = 2  # cups
servings = 8  # large cookies

# calculate the needed amounts
creamy_peanut_butter = (creamy_peanut_butter/ servings) * desired_servings
granulated_sugar = (granulated_sugar/servings) * desired_servings
large_eggs = (large_eggs/servings) * desired_servings
semi_sweet_chocolate_chips = (semi_sweet_chocolate_chips/servings) * desired_servings
# display results
print(f"{creamy_peanut_butter:.1f} = cups of creamy peanut butter " )
print(f"{granulated_sugar:.1f} = cups of granulated sugar =")
print(f"{large_eggs:.1f} = Quantity of eggs ")
print(f"{semi_sweet_chocolate_chips:.1f} = cups of semi-sweet chocolate chips")

