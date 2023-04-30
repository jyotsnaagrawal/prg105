import sqlite3

# Connect to the database
conn = sqlite3.connect('coffee.db')

# Retrieve data from the database
cursor = conn.execute('SELECT Category, Product, Supplier FROM Coffee ORDER BY Category, Product')

# Print the report header
print('CATEGORY'.ljust(15), 'PRODUCT'.ljust(35), 'SUPPLIER')
print("-" * 15, " " + "-" * 34, " " + "-" * 24)
# Print each row of data
for row in cursor:
    print(row[0].ljust(15), row[1].ljust(35), row[2])


# Close the database connection
conn.close()
