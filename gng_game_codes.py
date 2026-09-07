import random

def gng_game_easy():

    attempt_counter = 0
    points_counter = 0

    while attempt_counter < 5:

        while True:

            chosen_number = input("Enter your number: ").strip()

            if not chosen_number:
                print("Number cannot be empty.")
                continue

            try:
                chosen_number_int = int(chosen_number)

            except ValueError:
                print("Invalid format. Please enter a number.")
                continue

            if not 1 <= chosen_number_int <= 5:
                print("Number must be between 1 and 5.")
                continue

            break

        random_number = random.randint(1, 5)

        if chosen_number_int == random_number:
            points_counter += 1
            print("")
            print("!!! YOU GOT IT !!!")
            print("")
            print(f'Your points: {points_counter}')
        else:
            print("")
            print("=== BAD GUESS ===")
            print("")
            print(f'Your points: {points_counter}')

        attempt_counter += 1
        print(f'Attempts left: {5 - attempt_counter}')
        print("")

    return points_counter

def gng_game_medium():

    attempt_counter = 0
    points_counter = 0

    while attempt_counter < 5:

        while True:

            chosen_number = input("Enter your number: ").strip()

            if not chosen_number:
                print("Number cannot be empty.")
                continue

            try:
                chosen_number_int = int(chosen_number)

            except ValueError:
                print("Invalid format. Please enter a number.")
                continue

            if not 1 <= chosen_number_int <= 10:
                print("Number must be between 1 and 10.")
                continue

            break

        random_number = random.randint(1, 5)

        if chosen_number_int == random_number:
            points_counter += 2
            print("")
            print("!!! YOU GOT IT !!!")
            print("")
            print(f'Your points: {points_counter}')
        else:
            print("")
            print("=== BAD GUESS ===")
            print("")
            print(f'Your points: {points_counter}')

        attempt_counter += 1
        print(f'Attempts left: {5 - attempt_counter}')
        print("")

    return points_counter

def gng_game_hard():

    attempt_counter = 0
    points_counter = 0

    while attempt_counter < 5:

        while True:

            chosen_number = input("Enter your number: ").strip()

            if not chosen_number:
                print("Number cannot be empty.")
                continue

            try:
                chosen_number_int = int(chosen_number)

            except ValueError:
                print("Invalid format. Please enter a number.")
                continue

            if not 1 <= chosen_number_int <= 15:
                print("Number must be between 1 and 10.")
                continue

            break

        random_number = random.randint(1, 15)

        if chosen_number_int == random_number:
            points_counter += 3
            print("")
            print("!!! YOU GOT IT !!!")
            print("")
            print(f'Your points: {points_counter}')
        else:
            print("")
            print("=== BAD GUESS ===")
            print("")
            print(f'Your points: {points_counter}')

        attempt_counter += 1
        print(f'Attempts left: {5 - attempt_counter}')
        print("")

    return points_counter