def main():
    total = 0
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    steps_per_days = {}
    print('You will be entering the number of steps taken for each day in a week. ')
    for day in days:
        numbers_steps = int(input(f'Please enter the number of steps taken on {day} :'))
        steps_per_days[day] = numbers_steps
        total += numbers_steps
    print(f'\nYou walked a total of {total:,} steps during the week. ')
    print(f'That was an average of {int(total / len(days)) :,}')
    min_day = []
    max_day = []
    max_steps = max(steps_per_days.values())
    min_steps = min(steps_per_days.values())
    for day in steps_per_days:
        if min_steps == steps_per_days.get(day):
            min_day.append(day)

        if max_steps == steps_per_days.get(day):
            max_day.append(day)

    print(f'The maximum steps you took were {max_steps} on:')
    for day in max_day:
        print(f'----{day}')

    print(f'The minimum steps you took were {min_steps} on:')
    for day in min_day:
        print(f'----{day}')


main()