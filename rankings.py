gng_ranking = [{"Position": 1, "Nickname": "Anna", "Result": 6},
               {"Position": 2, "Nickname": "Bartek", "Result": 4},
               {"Position": 3, "Nickname": "Ziuta", "Result": 2},
               ]

def rankings(nickname, result):

    new_ranking = [
        player
        for player in gng_ranking
    ]

    for player in new_ranking:

        if player["Result"] <= result:
            new_ranking.insert((player["Position"] - 1), {"Position": 0,
                                                          "Nickname": nickname,
                                                          "Result": result})
            break

    else:
        new_ranking.append({"Position": 0,
                            "Nickname": nickname,
                            "Result": result})

    for position, player in enumerate(new_ranking, start=1):
        player["Position"] = position

    return new_ranking
