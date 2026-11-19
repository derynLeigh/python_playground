import random
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text
from rps_module import rock, paper, scissors, lizard, spock

HAND_IMAGES = {
    "Rock": rock,
    "Paper": paper,
    "Scissors": scissors,
    "Lizard": lizard,
    "Spock": spock,
}
CHOICES = list(HAND_IMAGES.keys())
EXIT_OPTION = "Exit"

console = Console()

SCORE_MAP = {
    "Rock": {"Rock": 0, "Paper": -1, "Scissors": 1, "Lizard": 1, "Spock": -1},
    "Paper": {"Rock": 1, "Paper": 0, "Scissors": -1, "Lizard": -1, "Spock": 1},
    "Scissors": {"Rock": -1, "Paper": 1, "Scissors": 0, "Lizard": 1, "Spock": -1},
    "Lizard": {"Rock": -1, "Paper": 1, "Scissors": -1, "Lizard": 0, "Spock": 1},
    "Spock": {"Rock": 1, "Paper": -1, "Scissors": 1, "Lizard": -1, "Spock": 0},
}


def get_game_result(player_choice, computer_choice):
    score = SCORE_MAP[player_choice][computer_choice]
    if score == 1:
        return "You won"
    elif score == -1:
        return "You lost"
    return "It's a tie"


def show_hands(player_choice, computer_choice):
    table = Table(show_header=True, show_lines=False, box=None)
    table.add_column(f"You: {player_choice}", no_wrap=True)
    table.add_column(f"Computer: {computer_choice}", no_wrap=True)
    table.add_row(
        Text(HAND_IMAGES[player_choice].strip("\n")),
        Text(HAND_IMAGES[computer_choice].strip("\n")),
    )
    console.print(table)


def get_player_choice():
    return Prompt.ask("Choose your hand", choices=CHOICES + [EXIT_OPTION], case_sensitive=False)


def play_round():
    computer_choice = random.choice(CHOICES)
    player_choice = get_player_choice()

    if player_choice == EXIT_OPTION:
        return False

    show_hands(player_choice, computer_choice)
    print(get_game_result(player_choice, computer_choice))
    return True


def main():
    while play_round():
        pass
    print("Thanks for playing. Goodbye!")


if __name__ == "__main__":
    main()
