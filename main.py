import difficulty_levels, inputs

nickname = inputs.get_nickname()

print(f'!!! WELCOME TO GUESS NUMBER GAME {nickname}!!!')

print("To start a game please select difficulty level.")
print("1. Easy\n2. Medium\n3. Hard")

game_lvl, game_lvl_name = inputs.get_game_lvl()

print(f'Selected difficulty level: {game_lvl}. {game_lvl_name}')


