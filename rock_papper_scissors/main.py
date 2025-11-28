import random

ROCK = "r"
SCISSORS = "s"
PAPER = "p"

emojis = {ROCK: "👊", SCISSORS: "✌️", PAPER: "✋"}
choices = tuple(emojis.keys())


def get_player_name(prompt="Gimme Your Name Betch : "):
    name = input(prompt).strip().title()
    return name if name else "Player"


def get_player_choice(player_name):
    while True:
        player_choices = input(
            f"OK! betch {player_name} (r)ock, (s)cissors, (p)aper: "
        ).strip().lower()
        if player_choices in choices:
            return player_choices
        else:
            print("Invalid choice. Please try again.")


def display_choices(player_choices, computer_choices):
    print(f"You chose: {emojis[player_choices]}")
    print(f"Computer chose: {emojis[computer_choices]}")


def determine_winner(player_choices, computer_choices):
    if player_choices == computer_choices:
        print("It's a tie!")
    elif (
        (player_choices == ROCK and computer_choices == SCISSORS)
        or (player_choices == SCISSORS and computer_choices == PAPER)
        or (player_choices == PAPER and computer_choices == ROCK)
    ):
        print("You win !")
    else:
        print("Computer wins!")


def play_games():

    print("=" * 25)
    print("WELCOME")
    print("=" * 25)

    player_name = get_player_name()
    while True:
        player_choices = get_player_choice(player_name)
        computer_choices = random.choice(choices)
        display_choices(player_choices, computer_choices)
        determine_winner(player_choices, computer_choices)

        play_again = input(f"Wanna play again Betch? {player_name} (y/n): ").strip().lower()
        if play_again != "y":
            print(f"Thanks for playing Doggo {player_name}!")
            break


if __name__ == "__main__":
    play_games()
