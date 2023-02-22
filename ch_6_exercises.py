"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""

# TODO 6.1 Introduction to File Input and Output
print("=" * 10, "Section 6.1 file input and output", "=" * 10)
# 1) Assign the variable file_variable to open states.txt in read mode


def main():
    file_variable = open("states.txt", "r")


# 2) Close the file
    file_variable.close()
# 3) Assign the variable state_capitals to open capitals.txt in write mode.
#    Please note, the file does not currently exist, and by opening it in
#    write mode you will create it
    state_capitals = open("capital.txt", "w")


# 4) Write three state capitals to the file with each capital and state pair on a separate line
#    There is a list of state capitals here: https://en.wikipedia.org/wiki/List_of_capitals_in_the_United_States
# Sample:
#   state_capitals.write("Alabama, Montgomery\n") - make sure to include the \n as a new line symbol

    state_capitals.write("Alabama,	Montgomery\n")
    state_capitals.write("Alaska ,	Juneau\n")
    state_capitals.write("Arizona,	Phoenix\n")

# 5) Close the file
    state_capitals.close()


main()

# TODO 6.1 reading data in from a file


print("=" * 10, "Section 6.1 reading data from a file", "=" * 10)
# 1) Assign the variable states_data to open states.txt in read mode


def main():
    infile = open("states.txt", "r")

# 2) Read in three lines from the file, assign one line to each variable below, Remove """   """ to test

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

 
# 3) Close the file
    infile.close()
# 4) Print the three variables
    print(line1)
    print(line2)
    print(line3)


main()
# TODO 6.2 Using loops to process files
print("=" * 10, "Section 6.2 use loops to process files", "=" * 10)
# Complete the program below to Read in and Count all entries in the states file
# Remove the """ """ before testing
# 1) Open the file in read mode using states_file as the file variable


def main():

    states_file = open("states.txt", "r")
    line = states_file.readline()
    counter = 0


# 2) Write a for loop to read in all the lines,
# -- print each line on the screen,
# -- also add 1 to counter for each line
    while line != '':
        counter += 1
        print(counter, line)
        line = states_file.readline()
    states_file.close()


main()

# 3) Close the file

# TODO 6.3 Processing records


print("=" * 10, "Section 6.3 processing records", "=" * 10)
# You are going to finish the program below to write book information to a file
books = 3      # use this as the number of books to enter

# 1) open the file books.txt for writing, using the variable books_file
# Remove the """ """ to test


def main():
    books_file = open("book.txt", "w")
# 2) Use a for loop to get a title and author from the user using a range of 1, books + 1
# -- get the data from the user in the loop
# -- write the data to the file as a record while in the loop,
#    make sure to include the \n at the end of the line
    for count in range(1, books + 1):
        print(f'Enter Title and Author for books:{count}')
        title = input('Title: ')
        author = input('Author: ')
        books_file.write(f'Title: {title}, \t Author: {author}\n')
# 3) Close the file
    books_file.close()


main()
# TODO 6.4 Exceptions
print("=" * 10, "Section 6.4 exceptions", "=" * 10)
# In this exercise you will try to open a file that does not exist,
# capture the error, and display a custom error message

# 1) Create a try statement
try:
    # 2) Open the file superheros.txt for READING (we are not writing, it would create the file)
    error_file = open("superheros.txt", "r")
    # 3) Close the file
    error_file.close()
# 4) Create an except IOError, that uses a print statement to tell the user that the file doesn't exist
except IOError:
    print(f"File superheros.txt doesn't exist!")