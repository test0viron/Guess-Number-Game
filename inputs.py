def get_nickname():

    while True:

        nickname = input("Enter your in game nickname: ").strip()

        if not nickname:
            print("Nickname cannot be empty")
            continue

        return nickname

def get_game_lvl():

    game_lvl_numbers = ["1", "2", "3"]

    while True:

        game_lvl = input("Enter selected difficulty level (number): ").strip()

        if not game_lvl:
            print("Difficulty level cannot be empty")
            continue

        if game_lvl not in game_lvl_numbers:
            print("Invalid difficulty level\nChoose from 1, 2 or 3")
            continue

        if game_lvl == "1":
            difficulty = "Easy"
        elif game_lvl == "2":
            difficulty = "Medium"
        elif game_lvl == "3":
            difficulty = "Hard"

        return difficulty

def get_guessed_number():
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

        return chosen_number_int
