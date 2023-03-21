def main():

    try:
        cities_dict = {}
        my_file = open("tale_of_two_cities.txt", "r")
        cities_list = [line.rstrip('\n') for line in my_file]
        my_file.close()

        for city in cities_list:
            count = cities_dict.get(city)
            if count is None:
                cities_dict[city] = 1
            else:
                cities_dict.update({city: count + 1})

        for key, value in cities_dict.items():
            if value == 1:
                print(key)

    except IOError:
        print(f'Unable to access the file.')


main()