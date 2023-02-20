PI = 3.14


def menu():
    print("This program will find the area of a shape for you.")
    print("1. Rectangle ")
    print("2. Triangle ")
    print("3. Square ")
    print("4. Circle ")
    print("5. Quit ")


def validate():
    user_selection = int(input("Please enter the number of your selection:  "))
    while user_selection not in range(1, 6):
        print("This is not a valid number\n")
        menu()
        user_selection = int(input("Please enter the number of your selection:  "))

    return user_selection


def main():
    menu()
    user_selection = validate()

    continue_flag = True
    while continue_flag:
        if user_selection == 1:
            length = int(input('Enter the length of a rectangle in cm : '))
            width = int(input('Enter the width of a rectangle in cm : '))
            area = rectangle_area(length, width)
            print("Area of the Rectangle is ", area, "square cm. \n")
        elif user_selection == 2:
            base = float(input("Enter the base of the triangle in cm: "))
            height = float(input("Enter the height of the triangle in cm: "))
            area = triangle_area(base, height)
            print("The area of the triangle is", area, "square cm. \n")
        elif user_selection == 3:
            side = int(input("Enter the length of one side of the square in cm: "))
            area = square_area(side)
            print("Area of the square is ", area, "square cm. \n")
        elif user_selection == 4:
            radius = float(input('Enter radius of the Circle: '))
            area = circle_are(radius)
            print(f"The area of the circle is {area:.2f} square cm. \n")
        elif user_selection == 5:
            quit_program()

        menu()
        user_selection = validate()


def rectangle_area(length, width):
    return length * width


def triangle_area(base, height):
    return 0.5 * base * height


def square_area(side):
    return side * side


def circle_are(radius):
    return PI * radius * radius


def quit_program():
    print("This is not a valid number")
    print("Goodbye ")
    return quit()


main()










