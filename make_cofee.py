import sqlite3

# Connect to the database or create it if it doesn't exist
conn = sqlite3.connect('coffee.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the Coffee table if it doesn't already exist
cursor.execute('''CREATE TABLE IF NOT EXISTS Coffee
                  (ProductID INTEGER PRIMARY KEY NOT NULL,
                   Product TEXT,
                   Category TEXT,
                   Supplier TEXT);''')

# Read in the data from the CSV file
try:
    with open('coffeehouse_supplies.csv', 'r') as file:
        data = file.readlines()
except IOError:
    print("Error: Unable to open data file")
    conn.close()
    exit()

# Iterate through the lines in the file and insert the data into the database
count = 0
for line in data:
    fields = line.strip().split(',')
    if len(fields) != 3:
        print("Error: Invalid data format")
        conn.close()
        exit()
    try:
        cursor.execute("INSERT INTO Coffee (Product, Category, Supplier) VALUES (?, ?, ?)", fields)
        count += 1
    except sqlite3.Error:
        print("Error: Unable to insert data into database")
        conn.close()
        exit()

# Commit the changes and close the connection
conn.commit()
conn.close()

# Print the number of records successfully added
print(f"{count} records added ")
