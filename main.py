import gng_game_code, inputs, rules, rankings


def main():
    nickname = inputs.get_nickname()
    print("")

    print(f'!!! WELCOME TO GUESS NUMBER GAME {nickname}!!!')
    print("")

    print("To start a game please select difficulty level by its number.")
    print("1. Easy\n2. Medium\n3. Hard")
    print("")

    difficulty = inputs.get_game_lvl()
    print("")

    print(f'Selected difficulty level:\n=== {difficulty} ===')
    print("")

    rules.display(difficulty)
    print("")

    if difficulty == "Easy":
        end_result = gng_game_code.gng_game("Easy")
    elif difficulty == "Medium":
        end_result = gng_game_code.gng_game("Medium")
    elif difficulty == "Hard":
        end_result = gng_game_code.gng_game("Hard")

    if end_result == 0:
        print("=== GAME OVER ===")
        print(f'Better luck next time {nickname}!')
    else:
        print("=== GAME OVER ===")
        print("")
        print(f'Congratulations, {nickname}! Your score: {end_result} {"point" if end_result == 1 else "points"}')

    ranking = rankings.rankings(nickname, end_result)
    print("")

    print("Your place in ranking:")

    for rank in ranking:

        print(f'{rank["Position"]}. {rank["Nickname"]} - {rank["Result"]} {"point" if rank["Result"] == 1 else "points"}')

if __name__ == '__main__':
    main()