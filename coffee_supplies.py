"""Using the coffee database created in the previous assignment as your data source, generate a report showing coffee
supplies by category similar to the one below. Each category name should appear only once and categories should be in
alphabetical order. (NOTE: Alphabetizing the products in each category is optional.)"""

import sqlite3


def main():
    coffee_db = None
    # connect to coffee database
    try:
        coffee_db = sqlite3.connect("coffee.db")
        coffee_cursor = coffee_db.cursor()
        coffee_cursor.execute("""SELECT Category FROM Coffee""")
        category_list = coffee_cursor.fetchall()

        # initialize list
        unique_category = []
        for category in category_list:
            if category[0] not in unique_category:
                unique_category.append(category[0])

        print("CATEGORY         PRODUCT         SUPPLIER")
        print("========   ===================  =============")

        # sort the categories and loop through them
        unique_category.sort()
        for category in unique_category:
            print(category)
            coffee_cursor.execute("""SELECT * FROM Coffee WHERE Category == ?""", (category,))
            product_list = coffee_cursor.fetchall()
            # display details for each product in the category
            for product in product_list:
                print(f"         {product[1]:20}  {product[3]}")

    except sqlite3.Error:
        print("%SQL error encountered.")
    finally:
        if coffee_db is not None:
            coffee_db.close()


main()
