1. Started project of with creation of local repository and git
2. Created docs/work-log.md and README.md
3. Shared project on GitHub with initial commit containg docs/work-log.md and README.md
4. Created inputs.py
5. Created get_nickname and get_game_lvl functions in inputs.py
6. Created main.py
7. Implemented get_nickname and get_game_lvl to main.py
8. Created rules.py for explaining rules of every difficulty level to user.
9. Implemented rules to main program in main.py file.
10. Created gng_game.py for every gng game level code
11. Created code for every gng game level
12. Implemented gng_game.py module and its functions into main program code in main.py file
13. Created rankings.py for ranking creation after ending of the GNG game
14. Created code that takes in users nickname and game result, putting him into preexisting bez results ranking
    - I used ChatGPT help for problem with putting User in the first place in ranking
        - ChatGPT help consisted of a hint on how to solve this problem. The hint suggested using for... else: loop
15. Implemented ranking.py module to main program in main.py file
16. Changed gng_game.py name to gng_game_codes.py for readability
17. Put whole execution code in main.py in main() function, and added 'if __name__' condition
18. ALL tests for every program parts were done during coding.
    - !! Note for future !! - write down tests for every program part that you're testing
19. Whole program sent to ChatGPT for code review
20. All corrections from ChatGPT checked and implemented
21. Manual tests :
    1. Inputs :
      - nickname:
        - empty - works
        - spaces - works
        - valid - works
      - difficulty:
        - empty - works
        - invalid - works
        - 1 - works
        - 2 - works
        - 3 - works
      - guess:
        - empty - works
        - spaces - works
        - text - works
        - valid integer - works
    2. Easy :
        - 0   → rejected
        - 1   → accepted
        - 5   → accepted
        - 6   → rejected
    3. Medium :
        - 0   → rejected
        - 1   → accepted
        - 10  → accepted
        - 11  → rejected
    4. Hard :
       - 0   → rejected
       - 1   → accepted
       - 15  → accepted
       - 16  → rejected
    5. Attempts :
       - 5 correct inputs → game over
       - invalid input → does not count
    6. Ranking :
       - result > first place - works
       - tie - user takes higher place
       - result < last place - works
    7. double rankings() call out - does not change gng_ranking positions
        
        