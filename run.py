# Import random to allow words to be chosen randomly from words.py
import random
# Import os to interact with the native operating system to clear the terminal
import os

# Import necessary local modules
import ascii_art
from words import sea_themed_words
from sinking_ship import draw_sinking_ship
from game_over import draw_game_over
from game_winner import draw_game_winner
from font_styles import styles


def clear_terminal():
    """
    Clears the terminal ready for new content
    """
    os.system("cls" if os.name == "nt" else "clear")


def welcome_page():
    """
    Displays the main title page
    Prompts the user to press ENTER to begin the game
    Clears terminal before proceeding to next page
    """
    clear_terminal()

    print(ascii_art.GAME_TITLE)
    print(styles.BLUE_BOLD + "\nWelcome to the Watery Wordplay Wreck!" +
          styles.FIN)

    input("Please press ENTER to begin!\n")
    clear_terminal()
    game_rules()