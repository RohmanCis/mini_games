import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

emojis = {ROCK: '👊', SCISSORS: '✌️', PAPER: '✋'}
choices = tuple(emojis.keys())


def get_player_choice():
    while True:
        player_choices = input('Choose (r)ock, (s)cissors, (p)aper: ').lower()
        if player_choices in choices:
            return player_choices
        else:
            print('Invalid choice. Please try again.')
            
            
def display_choices(player_choices, computer_choices):            
    print(f'Your chose: {emojis[player_choices]}')
    print(f'Computer chose: {emojis[computer_choices]}')

def determine_winner(player_choices, computer_choices):
    if player_choices == computer_choices:
        return 'It\'s a tie!'
    elif (
        (player_choices == ROCK and computer_choices == SCISSORS) or 
        (player_choices == SCISSORS and computer_choices == PAPER) or 
        (player_choices == PAPER and computer_choices == ROCK)):
        print('You win!')
    else:
        print('Computer wins!')

def play_games():
    while True:
        player_choices = get_player_choice()
        computer_choices = random.choice(choices)
        display_choices(player_choices, computer_choices)
        determine_winner(player_choices, computer_choices)
        
        play_again = input('Do you want to play again? (y/n): ').lower()
        if play_again != 'y':
            print('Thanks for playing!')
            break
    
if __name__ == "__main__":
    play_games()