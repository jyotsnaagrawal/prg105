alpha = ['a', 'A', 'b', 'B', 'c', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K']
code = ['%', 'm', '#', '=', '@', '!', '*', '.', '$', '^', '&', '(', ')', '_', '-', '+', '`', '~', '/', '|' ]

print("This program will decode a coded text file. ")
file_name = input("What is the name of file to decode? ")
decoded_message =''
lines = []
try:
    decode_file = open(file_name, "r")
    lines = decode_file.readlines()
    decode_file.close()

    for line in lines:
        char = line.rstrip('\n')
        if char in code:
            index = code.index(char)
            decoded_char = alpha[index]
            decoded_message += decoded_char
        else:
            decoded_message += char

    print(decoded_message)
except IOError:
    print(f"Unable to access the file name: {file_name}")




