from menu import menu
from game import game

amount_won = 0
amount_lost = 0

def menu_loop(amount_won, amount_lost):
    while menu(amount_won, amount_lost) != "play":
        menu_loop(amount_won, amount_lost)
    else:
        game_loop(amount_won, amount_lost)

def game_loop(amount_won, amount_lost):
    if game() == "win":
        amount_won += 1
    else:
        amount_lost += 1
    menu_loop(amount_won, amount_lost)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu_loop(amount_won, amount_lost)


