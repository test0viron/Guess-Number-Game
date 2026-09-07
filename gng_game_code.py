import random, inputs

def gng_game(difficulty):

    attempt_counter = 0
    points_counter = 0

    while attempt_counter < 5:

        chosen_number_int = inputs.get_guessed_number()

        if difficulty == "Easy":

            if not 1 <= chosen_number_int <= 5 :
                print("Please enter a number between 1 and 5.")
                continue

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

        if difficulty == "Medium":

            if not 1 <= chosen_number_int <= 10 :
                print("Please enter a number between 1 and 10.")
                continue

            random_number = random.randint(1, 10)

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

        if difficulty == "Hard":

            if not 1 <= chosen_number_int <= 15 :
                print("Please enter a number between 1 and 15.")
                continue

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

