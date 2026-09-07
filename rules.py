def rules(difficulty):

    if difficulty == "Easy":
        print("Easy level game rules:")
        print("1. You will need to chose one number form 1 to 5 range")
        print("2. For every guess your attempt counter will rise by 1")
        print("3. Every correct guess in Medium level gives you 1 point in ranking")
        print("4. Every wrong answer just wastes one attempt")
        print("5. After 5 attempts your game is over")

    elif difficulty == "Medium":
        print("Medium level game rules:")
        print("1. You will need to chose one number form 1 to 10 range")
        print("2. For every guess your attempt counter will rise by 1")
        print("3. Every correct guess in Medium level gives you 2 points in ranking")
        print("4. Every wrong answer just wastes one attempt")
        print("5. After 5 attempts your game is over")

    elif difficulty == "Hard":
        print("Hard level game rules:")
        print("1. You will need to chose one number form 1 to 20 range")
        print("2. For every guess your attempt counter will rise by 1")
        print("3. Every correct guess in Medium level gives you 3 points in ranking")
        print("4. Every wrong answer just wastes one attempt")
        print("5. After 5 attempts your game is over")
