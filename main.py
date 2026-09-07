import difficulty_levels, inputs, rules

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

