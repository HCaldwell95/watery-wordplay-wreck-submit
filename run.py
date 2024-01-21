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


def game_rules():
    """
    Introduces the game and provides the user with the game rules.
    """
    print(ascii_art.RULES)

    print("\nRules of the Game:")
    print(styles.GREEN + "1. Suggest one letter at a time to guess the word." +
          styles.FIN)
    print(styles.GREEN + "2. Suggest a word if you think you've got it!\n" +
          styles.FIN)

    print("\nChoose your difficulty by selecting the number of lives.")
    print("The ship will begin to sink after each incorrect guess.")
    print("I suggest we guess the word and save the ship before it sinks!")

    start_game()


def choose_num_of_lives():
    """
    Prompts the user to choose the number of lives for gameplay,
    enabling them to set the difficulty level.
    This loop persists until a valid input is submitted.

    This function serves to customise the difficulty level of the game by
    allowing the user to choose the number of lives. It presents a menu of
    options, each representing a difficulty level, and prompts the user to
    input their choice.

    The function enters a loop, ensuring that the user provides a valid input.
    The loop displays the available difficulty options and prompts the user
    until a valid selection is made.
    """
    options = {"8": "Easy", "6": "Medium", "4": "Hard"}

    while True:
        print("\nSelect the difficulty level by choosing the number of lives:")
        for option, difficulty in options.items():
            print(f'Enter "{option}" for {difficulty}')

        choice = input().strip()
        if choice in options:
            return int(choice)
        else:
            print(styles.YELLOW + 'Invalid input: "' + choice +
                  '" is not a valid option. Please try again.' + styles.FIN)


def get_random_word():
    """
    Pulls a random word from words.py for the user to guess.
    """
    return random.choice(sea_themed_words).upper()


def print_game_state(secret_word, used_letters, used_words, num_of_lives):
    """
    Prints the current state of the game.

    This function displays crucial information about the current state of
    the game to aid the player in their progress. It includes the number
    of attempts remaining (num_of_lives), the representation of the word
    to guess (secret_word), and the lists of attempted letters and words.
    """
    if num_of_lives > 0:
        print(f"You have {num_of_lives} attempts left.\n")
    else:
        print("Game Over")

    print("\nYour " + styles.BOLD + str(len(secret_word)) +
          " LETTER " + styles.FIN + "word to guess is: " +
          secret_word)

    print(styles.BLUE + "Attempted letters: ",
          ", ".join(sorted(used_letters)) + styles.FIN)
    print(styles.BLUE + "Attempted words: ",
          ", ".join(sorted(used_words)) + styles.FIN)


def determine_game_outcome(secret_word, actual_word, num_of_lives):
    """
    Determines the game outcome and displays the appropriate message.

    This function compares the player's guessed word (secret_word) with the
    actual word (actual_word) to determine the outcome of the game. If the
    guessed word matches the actual word, it congratulates the player and
    displays a victory message along with an animated depiction of a winning
    scenario using draw_game_winner(). If there is no match, it acknowledges
    the player's effort, reveals the correct word, and displays a game over
    message using draw_game_over().

    The function also clears the terminal before presenting the outcome.
    """
    clear_terminal()

    if secret_word == actual_word:
        print("Congratulations!")
        print(f'"{actual_word}" was the correct answer!\n\n')
        draw_game_winner()
    else:
        print("Good effort! The correct word was " +
              f'"{actual_word}".')
        print("Thank you for playing our Watery Wordplay Wreck!\n")
        draw_game_over()


def restart_game():
    """
    Asks the user if they would like to play the game again.

    This function presents the user with the option to restart the game.
    It provides visual prompts for the user to enter 'Y' for 'Yes'
    or 'N' for 'No'. Depending on the user's choice, it either restarts the
    game with new settings or returns to the main title page.

    The function uses a loop to handle invalid inputs and ensures the user
    provides a valid response before proceeding.
    """

    while True:
        print("\nWould you like to play again? Enter " + styles.GRN_Y +
              " for " + styles.GRN_YES + " and  " + styles.RED_N +
              " for " + styles.RED_NO + "\n")

        restart_options = {"Y": game_rules, "N": welcome_page}

        restart = input("Please enter " + styles.GREEN + "Y " + styles.FIN +
                        "or " + styles.RED + "N" + styles.FIN + ":\n").upper()

        if restart in restart_options:
            clear_terminal()
            restart_options[restart]()
            break
        else:
            print(styles.YELLOW + 'Invalid Input: Please enter "Y" or "N".\n' +
                  styles.FIN)


def play_game(word, num_of_lives):
    """
    Initiates and manages a round of the game
    """

    # Initialises variables for the current game round
    secret_word = "_" * len(word)
    used_letters = []
    used_words = []

    clear_terminal()

    # Displays the game introduction and secret word information
    print("\nLet's play the Watery Wordplay Wreck! Good Luck.")
    print("\nThis word has " + styles.BLUE_BOLD + str(len(word)) +
          styles.FIN + " letters.")
    print("Good Luck!")

    draw_sinking_ship(num_of_lives)

    # Main game loop
    while num_of_lives > 0:

        # Gets user input for a letter or word and converts it to uppercase
        guess = input(f"Please enter a {styles.BOLD}LETTER{styles.FIN} "
                      f"or a {styles.BOLD}WORD{styles.FIN}:\n").upper()
        clear_terminal()

        try:
            # Checks if the input is not in the alphabet
            if not guess.isalpha():
                print(styles.YELLOW +
                      f'Invalid input: "{guess}" is not a valid letter.')
                print("Please enter a letter." + styles.FIN)

            # Checks if the user input is a word of the correct length
            elif len(guess) == len(word) and guess.isalpha():
                if guess in used_letters:
                    print(styles.YELLOW +
                          f"Invalid input: you have entered {len(guess)}" +
                          " letters.")
                    print("Please enter a letter " +
                          f"or word containing {len(word)} letters." +
                          styles.FIN)

                # Decrement lives, updates used letters and provides feedback
                elif guess != word:
                    if guess not in used_words:
                        num_of_lives -= 1
                        used_words.append(guess)
                        print(styles.RED +
                              f'Sorry, "{guess}" is not the word.' +
                              styles.FIN)

                    # Checks if input has already been used and alerts user
                    else:
                        print(styles.YELLOW +
                              f'You have already tried "{guess}".')
                        print("Please try again!" + styles.FIN)

                # Assigns the correct word to secret_word and exits loop
                else:
                    secret_word = word
                    break

            # Check if the user input is not a single letter or alphabetic
            elif len(guess) != 1 or not guess.isalpha():
                print(styles.YELLOW +
                      f"Invalid input: you have entered {len(guess)} letters.")
                print("Please enter a letter " +
                      f"or word containing {len(word)} letters." + styles.FIN)

            # Checks if input has already been used and alerts user
            elif guess in used_letters:
                print(styles.YELLOW + f'You have already tried "{guess}".')
                print("Please try again!" + styles.FIN)

            # Decrement lives, updates used letters and provides feedback
            elif guess not in word:
                num_of_lives -= 1
                used_letters.append(guess)
                print(styles.RED +
                      f'Sorry, "{guess}" is not in the word.' + styles.FIN)

            # Checks if the input letter is in the word and provides feedback
            else:
                used_letters.append(guess)
                print(styles.GREEN + f'"{guess}" IS in the word!')
                print("Good job!" + styles.FIN)

                # Updates the secret word with the correct letters
                word_as_list = list(secret_word)
                indices = [
                        i for i, letter in enumerate(word) if letter == guess]

                # Replaces underscores with correct letters in the word
                for index in indices:
                    word_as_list[index] = guess
                secret_word = "".join(word_as_list)

                # Exits loop if all letters have been guessed
                if "_" not in secret_word:
                    break

        # Handles invalid data input
        except ValueError as error:
            print(styles.YELLOW +
                  f'Invalid data: {error}, please try again.\n"' +
                  styles.FIN)
            continue

        # Displays the current state of the game
        print_game_state(secret_word, used_letters, used_words, num_of_lives)

        # Draws the sinking ship based on the user's remaining lives
        draw_sinking_ship(num_of_lives)

    # Determines and displays the game outcome
    determine_game_outcome(secret_word, word, num_of_lives)

    # Asks the user if they want to play again
    restart_game()