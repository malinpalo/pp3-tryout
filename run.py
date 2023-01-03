import random
import colorama
from colorama import Fore, Back, Style
from graphics import welcome, win, loose, god_bye
from words import hidden_words
from time import sleep  # allows time delay for print statements
colorama.init(autoreset=True)

    
def welcome_screen():
    """
    Option where player kan choose to begin game, select difficulty
    or view the rules
    """
    print(Fore.YELLOW + welcome)
    print("Welcome dear player! It's time to stay alive...\n")
    sleep(1)
    print(
        "First, choose your dificulty level.\n"  
        "You have 10 tries at easy level and 5 tries at hard level.\n"
        )
    sleep(1)
    print(
        "Then try and guess the secret word one letter at a time\n"
        "before you're out of tries.\n"
    )
    sleep(1)
    print(
        "For each wrong guessed letter you lose one\n"
        "and your gallows gets built more until you dangle.\n"
    )
    sleep(1)
    print(
        "If you want to play again, simply restart the game\n"
        "by entering Y or N in the end of the game.\n"
    )
    print("Press " + "1" + " to start game")
    print("Press " + "2" + " to enter the difficulty level")
    opt = False
    while not opt:
        settings = input("\n ")
        if settings == "1":
            opt = True
            difficulty_l = "default"
            return difficulty_l

        elif settings == "2":
            opt = True

        else:
            print("Please enter 1 or 2 to make your choice")


def choose_difficulty():
    """
    This is where the player gets to chose difficulty level
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
            total_lives = 10 
            return total_lives
        elif difficulty == "H":
            level = True
            total_lives = 5
            return total_lives
        else:
            print("\n Please enter E or H to make your choice")
        
        
def get_word():
    """
    Gets a word randomly from words.py for player to guess
    """
    random_words = random.choice(hidden_words).upper()
    return random_words


def game_play(word, total_lives):   
    """
    This is where the game is beeing played.
    The secret word is beeing displayed during the users turn as underscores.
    The underscores will be replaced with a letter when the correct letter 
    is being guessed. 
    
    """
    secret_word = "_" * len(word)
    game_over = False
    guesswork = []
    tries = total_lives
    print("\n")
    print("Lets play!\n")
    print(f"Lives: {tries}\n")
    print("The word to guess: " + " ".join(secret_word) + "\n")
    print("\n")

    while not game_over and tries > 0:
        player_guess = input("Guess a letter:\n".upper())

        try:
            if len(player_guess) > 1:
                raise ValueError(
                    f"Aaa, sorry, you can only guess 1 letter at a time, you guessed"
                    f" {len(player_guess)} characters\n"
                )
            
            elif not player_guess.isalpha():
                raise ValueError(
                    f"Ohps, you can only guess letters, you guessed {(player_guess)}"
                    f" that is not a letter."
                )
            
            elif len(player_guess) == 1 and player_guess.isalpha():
                if player_guess in guesswork:
                    raise ValueError(
                        f"Oh, no! You have already guessed {(player_guess)} ")

                elif player_guess not in word:
                    info = f"{(player_guess)} is not in the word. You lose a life."\

                    guesswork.append(player_guess)
                    tries -= 1

                else:
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
            print(f"Tries: {tries}\n")
            print("The word to guess: " + " ".join(secret_word) + "\n")
            print("Letters guessed: " + ", ".join(sorted(guesswork)) + "\n")

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
                print(Fore.YELLOW + god_bye)

            else:
                raise ValueError(
                    f"You must enter Y or N. You entered {(restart_game)}"
                )

        except ValueError as e:
            print(f"{e}.Please try again.")


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
    Displays hangman graphic based on lives left
    """
    tries_left = [ 
        """
        ___________
        | /       |
        |/       (O)
        |       //|\\
        |         |
        |       // \\
        |\\
        ========
        """,
        """
        ___________
        | /       |
        |/       (O)
        |       //|\\
        |         |
        |       //
        |\\
        ========
        """,
        """
        __________
        | /      |
        |/      (O)
        |      //|\\
        |        |
        |
        |\\
        ========
        """,
        """
        __________
        | /      |
        |/      (O)
        |      //|
        |        |
        |
        |\\
        ========
        """,
        """
        __________
        | /      |
        |/      (O)
        |        |
        |        |
        |
        |\\
        ========
        """,
        """
        __________
        | /      |
        |/      (O)
        |
        |
        |
        |\\
        ========
        """,
        """
        __________
        | /
        |/
        |
        |
        |
        |\\
        ========
        """,
        """
        __________
        | /
        |/
        |
        |
        |
        |
        ========
        """,
        """
        | /
        |/
        |
        |
        |
        |
        ========
        """,
        """
        |
        |
        |
        |
        |
        ========
        """,
        """
        """
    ]
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