import sqlite3

# Step 1: Create database and tables
connection = sqlite3.connect('pets.db')
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Owners (
        OwnerID INTEGER PRIMARY KEY NOT NULL,
        OwnerName TEXT,
        OwnerPhone TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Pets (
        PetID INTEGER PRIMARY KEY NOT NULL,
        PetName TEXT,
        PetType TEXT,
        PetBreed TEXT,
        OwnerID INTEGER,
        FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID)
    )
""")

# Step 2: Read in data from files and insert into tables
with open('Owners.txt') as f:
    for line in f:
        data = line.strip().split(',')
        cursor.execute("INSERT INTO Owners (OwnerName, OwnerPhone) VALUES (?, ?)", (data[0], data[1]))

with open('Pets.txt') as f:
    for line in f:
        data = line.strip().split(',')
        cursor.execute("INSERT INTO Pets (PetName, PetType, PetBreed, OwnerID) VALUES (?, ?, ?, ?)",
                       (data[0], data[1], data[2], data[3]))

# Step 3: Retrieve data and display report
query = """
    SELECT Owners.OwnerName, Owners.OwnerPhone, Pets.PetName, Pets.PetType, Pets.PetBreed
    FROM Owners
    LEFT JOIN Pets ON Owners.OwnerID = Pets.OwnerID
    ORDER BY Owners.OwnerName
"""

current_owner = None

for row in cursor.execute(query):
    owner_name = row[0]
    owner_phone = row[1]
    pet_name = row[2]
    pet_type = row[3]
    pet_breed = row[4]

    if owner_name != current_owner:
        current_owner = owner_name
        print(f"\nOwner: {owner_name}\nPhone: {owner_phone}")

    print(f"\t{pet_name} ({pet_type}, {pet_breed})")

# Step 4: Commit changes and close connection
connection.commit()
connection.close()
