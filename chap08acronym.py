def main():
    print("This program accepts a phrase and returns the acronym. ")
    phrase = input("Please enter a phrase to convert: ")
    words=phrase.split()
    acronym = ""
    for word in words:
        acronym += word[0]
        acronym = acronym.upper()
    print(acronym)


main()



