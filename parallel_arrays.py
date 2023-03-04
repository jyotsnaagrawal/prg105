alpha = ['a', 'A', 'b', 'B', 'c', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K']
code = ['%', 'm', '#', '=', '@', '!', '*', '.', '$', '^', '&', '(', ')', '_', '-', '+', '`', '~', '/', '|' ]

secret_phrase = input("Enter a phrase to encode: ")
encoded_message = []

for char in secret_phrase:
    if char in alpha:
        index = alpha.index(char)
        encoded_char = code[index]
        encoded_message.append(encoded_char)
    else:
        encoded_message.append(char)

print("Encoded message:")
print(encoded_message)

encoded_file = open("encoded.txt", "w")
for char in encoded_message:
    encoded_file.write(char + "\n")