import sys

def exit():
    sys.exit("Thanks for playing!")

def menu(amount_won, amount_lost):
    print("H A N G M A N")

    # Makes play put in valid input choice
    player_menu_choice = input('Please enter "Play" to start, "Exit" to leave the game, or "Result" to see the amount of win/losses: ').lower()
    while player_menu_choice != "play" and player_menu_choice != "exit" and player_menu_choice != "result":
        player_menu_choice = input('Sorry, invalid input. Please enter "Play" to start, "Exit" to leave the game, or "Result" to see the amount of win/losses: ')

    if player_menu_choice == "exit":
        exit()
    elif player_menu_choice == "result":
        print("You have won {} game[s] and lost {} game[s]!".format(amount_won, amount_lost))
        print("\n")
        return "result"
    else:
        return "play"
