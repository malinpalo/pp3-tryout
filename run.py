"""
Libraries and imports
"""

import random,colorama,os
from colorama import Fore
from graphics import welcome, win, loose, tries_left, god_bye
from words import hidden_words
from time import sleep

colorama.init(autoreset=True)


def welcome_screen():
    """
    Logo, rules and options for player to begin the game
    or select the difficulty level.
    """
    print(Fore.YELLOW + welcome)
    print("Welcome dear player! It's time to try to stay alive...\n")
    sleep(1)
    print(
        "Please read the following instructions\n"
        "to find your way to and trough the game.\n"
    )
    sleep(1)
    print(
        "You can choose your difficulty level before entering the game.\n"
        "Easy level has 10 lives and hard level has 5 lives.\n"
        )
    sleep(1)
    print(
        "Then try and guess the secret word one letter at a time\n"
        "before you're out of lives.\n"
    )
    sleep(1)
    print(
        "For each wrong guessed letter you lose one life\n"
        "and your gallows gets built more until you dangle.\n"
    )
    sleep(1)
    print(
        "If you want to play again, simply restart the game\n"
        "by entering Y or enter N to exit the game.\n"
    )
    print("Press " + "1" + " to start game")
    print("Press " + "2" + " to enter the difficulty level")
    opt = False
    while not opt:
        settings = input("\n")
        if settings == "1":
            opt = True
            clean_screen()
            difficulty_l = "default"
            return difficulty_l

        elif settings == "2":
            opt = True
            clean_screen()

        else:
            print("\n")
            print(f"{Fore.RED}Please enter 1 or 2 to make your choice")
            clean_screen()

def choose_difficulty():
    """
    This is where the player gets to chose difficulty level.
    """
    print("\n")
    print("Select Difficulty level\n")
    print("Press " + "E" + " for Easy")
    print("Press " + "H" + " for Hard")

    level = False
    while not level:
        difficulty = input("\n").upper()
        if difficulty == "E":
            level = True
            clean_screen()
            total_lives = 10
            return total_lives
        elif difficulty == "H":
            level = True
            clean_screen()
            total_lives = 5
            return total_lives
        else:
            print("\n Please enter E or H to make your choice")
            

def get_word():
    """
    Gets a word randomly from words.py for player to guess.
    """
    random_words = random.choice(hidden_words).upper()
    return random_words


def game_play(word, total_lives):
    """
    The game play.
    Initial lives are beeing set, the secret word is
    beeing displayed as underscores, correct letter
    replaces the underscore. GameOver returns the player
    to the welcomescreen or restarts the game.
    """
    secret_word = "_" * len(word)
    game_over = False
    guesswork = []
    tries = total_lives
    print("\n")
    print("Lets play!\n")
    print(f"Lives: {tries}\n")
    print("The secret word: " + " ".join(secret_word) + "\n")

    while not game_over and tries > 0:
        player_guess = input("Guess a letter:\n".upper())
        try:
            if len(player_guess) > 1:
                raise ValueError(
                    f"Aaa, sorry, you can only guess 1 letter at a time."
                    f"You picked {len(player_guess)} letters."
                )

            elif not player_guess.isalpha():
                raise ValueError(
                    f"Ohps, you can only guess letters,\n"
                    f"you guessed {(player_guess)} that is not a letter."
                )

            elif len(player_guess) == 1 and player_guess.isalpha():
                if player_guess in guesswork:
                    raise ValueError(
                        f"Oh, no! You have already guessed {(player_guess)}")

                elif player_guess not in word:
                    clean_screen()
                    info = f"{Fore.RED}{(player_guess)} is not in the word."
                    print("You lost a life, please try again!")

                    guesswork.append(player_guess)
                    tries -= 1

                else:
                    clean_screen()
                    info = f"{player_guess} is in the word. Good job"\

                    guesswork.append(player_guess)
                    secret_word_list = list(secret_word)
                    indi = [i for i, letter in enumerate(word)
                            if letter == player_guess]
                    for index in indi:
                        secret_word_list[index] = player_guess
                        secret_word = "".join(secret_word_list)
                    if "_" not in secret_word:
                        game_over = True

        except ValueError as e:
            print(f"{e}. Please try again.")
            print("\n")
            continue

        print(hangman_tries(tries))

        if tries > 0:
            print(info)
            print("\n")
            print(f"Lives: {tries}\n")
            print("The word to be guessed: " + " ".join(secret_word) + "\n")
            print("These are the letters that you have guessed:\
                " + ", ".join(sorted(guesswork))
                    + "\n")

    if game_over:
        print(f"YEAY! {word} was the correct word!\n")
        player_win()

    else:
        print(f"Sorry, the correct word was {word}")
        hangman_win()

    restart(total_lives)


def restart(total_lives):
    """
    The player gets an option to restart the game....
    """
    restart = False
    while not restart:
        restart_game = input("Play again? \"Y/N\"").upper()

        try:
            if restart_game == "Y":
                restart = True
                hm_word = get_word()

                game_play(hm_word, total_lives)

            elif restart_game == "N":
                restart = True
                print("\n")
                print(Fore.LIGHTGREEN_EX + god_bye)
                sleep(3)
                clean_screen()
                start()

            else:
                raise ValueError(
                    f"You must enter Y or N. You entered {(restart_game)}"
                )

        except ValueError as e:
            print(f"{e}.Please try again.")

def clean_screen():
    """
    To clear Terminal screen
    """
    os.system("clear")


def player_win():
    """
    Graphic that displays if the player win!
    """
    print(Fore.YELLOW + win)


def hangman_win():
    """
     Graphic that displays if the player loose!
    """
    print(Fore.RED + loose)


def hangman_tries(tries):
    """
    Graphics for the hangman that are beeing displayed
    based on lives left.
    """
    for _ in tries_left:
        return tries_left[tries]


def start():
    """
    Runs the game
    """
    level = welcome_screen()
    if level == "default":
        total_lives = 7
    else:
        total_lives = choose_difficulty()

    word = get_word()
    game_play(word, total_lives)


start()
