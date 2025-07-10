import random

ALL_CHOICES = ['rock', 'paper', 'scissors','spock','lizard']

CHOICE_MAPPING = {
    'r'       : 'rock',
    'rock'    : 'rock',
    'p'       : 'paper',
    'paper'   : 'paper',
    'sc'      : 'scissors',
    'scissors':'scissors',
    'sp'      : 'spock',
    'spock'   : 'spock',
    'l'       : 'lizard',
    'lizard'  : 'lizard',
}

WINNING_COMBOS = {
    'rock':      ['scissors', 'lizard'],
    'paper':     ['rock', 'spock'],
    'scissors':  ['paper', 'lizard'],
    'spock':     ['rock', 'scissors'],
    'lizard':    ['rock', 'spock'],
}

def prompt(message):
    print(f'==> {message}')

def get_player_choice():
    prompt(f'Choose one: (r)ock, (p)aper, (sc)issors, (sp)ock, (l)izard')
    while True:
        player_choice = input().casefold()

        if player_choice == 's':
            prompt("Please enter 'sp' for spock or 'sc' for scissors")
            continue

        if player_choice in CHOICE_MAPPING:
            return CHOICE_MAPPING[player_choice]

        prompt("Thats not a valid choice, Please try again")

def decide_winner(player_choice, computer_choice):
    if computer_choice in WINNING_COMBOS[player_choice]:
        return 'win'
    if player_choice in WINNING_COMBOS[computer_choice]:
        return 'lose'
    return 'tie'

def quit_application():
    prompt("Would you like to play again (y/n)")
    answer = input().casefold()
    while answer not in ['y', 'n']:
        prompt("That is not a valid response. Please enter 'y' or 'n' ")
        answer = input().casefold()
    return answer == 'n'


while True:
    player_score = 0
    computer_score = 0

    while player_score < 3 and computer_score < 3:
        player_choice = get_player_choice()

        computer_choice = random.choice(ALL_CHOICES)

        game_result = decide_winner(player_choice, computer_choice)

        prompt(f"You chose {player_choice}, and computer chose {computer_choice}")

        if game_result == 'win':
            player_score += 1

        elif game_result == 'lose':
            computer_score += 1

        elif game_result == 'tie':
            prompt('Thats a tie')

        prompt(f"player:{player_score} | computer: {computer_score}")

    if player_score == 3:
        prompt("Congratulations! YOU'VE WON!")
        if quit_application():
            prompt("Thanks for playing!!")
            break

    elif computer_score == 3:
        prompt("Better luck next time")
        if quit_application():
            prompt("Thanks for playing!!")
            break