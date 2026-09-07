import gng_game, inputs, rules

nickname = inputs.get_nickname()
print("")

print(f'!!! WELCOME TO GUESS NUMBER GAME {nickname}!!!')
print("")

print("To start a game please select difficulty level.")
print("1. Easy\n2. Medium\n3. Hard")
print("")

game_lvl, difficulty = inputs.get_game_lvl()
print("")

print(f'Selected difficulty level:\n{difficulty}')
print("")

rules.rules(difficulty)
print("")

if difficulty == "Easy":
    end_result = gng_game.gng_game_easy()
if difficulty == "Medium":
    end_result = gng_game.gng_game_medium()
if difficulty == "Hard":
    end_result = gng_game.gng_game_hard()

if end_result == 0:
    print("=== GAME OVER ===")
    print(f'Better luck next time {nickname}!')
else:
    print("=== GAME OVER ===")
    print(f'Congratulations, {nickname}! You score: {end_result} points')

