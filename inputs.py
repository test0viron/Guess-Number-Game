def get_nickname():

    while True:

        nickname = input("Enter your ingame nickname: ").strip()

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
            game_lvl_name = "Easy"
        elif game_lvl == "2":
            game_lvl_name = "Medium"
        elif game_lvl == "3":
            game_lvl_name = "Hard"

        return game_lvl, game_lvl_name




