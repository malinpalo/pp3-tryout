import random
import colorama
import words
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from graphics import welcome
from words import hidden_words


    
def welcome_screen():
    """
    Option where player kan choose to begin game, select difficulty
    or view the rules
    """
    print(welcome)
    print(" Press " + "1" + " to play game")
    print(" Press " + "2" + " to enter difficulty")
    print(" Press " + "3" + " to view rules")
    options = False
    while not options:
        settings = input("\n ")
        if settings == "1":
            options = True
            difficulty = "default"
            return difficulty

        elif settings == "2":
            options = True

        elif settings == "3":
            options = True
            rules()

        else:
            print(" Please select 1, 2 or 3 to make your"
                  " choice")

def choose_difficulty():
    """
    This is where the player gets to chose difficulty level
    """
    print("\n")
    print("Select Difficulty level\n")
    print(" Press " + "E" + " for Easy")
    print(" Press " + "N" + " for Normal")
    print(" Press " + "H" + " for Hard")

    level = False
    while not level:
        difficulty = input("\n").upper()
        if difficulty == "E":
            level = True
            total_lives = 10 
            return total_lives
        elif difficulty == "N":
            level = True
            total_lives = 7
            return total_lives
        elif difficulty == "H":
            level = True
            total_lives = 5
            return total_lives
        else:
            print("\n Please select E, N or H to make your choice")
        
        
def get_word():
    """
    Gets a word randomly from words.py for player to guess
    """
    random_words = random.choice(hidden_words).upper()
    print('The word has', len(random_words), 'letters')

def game_play(random_words, total_lives):
    """
    This is where the game is beeing played.
    The secret word is beeing displayed during the users turn as underscores.
    The underscores will be replaced with a letter when the correct letter is guessed. 
    
    """
    secret_word = "_" * len(random_words)
    game_over = False
    guesswork = []
    tries = total_lives
    print("\n")
    print("Lets play Hangman!\n")
    print(f" Lives: {tries}\n")
    print(f" The word to guess: " + " ".join(secret_word) + "\n")

    while not game_over and tries > 0:
        player_guess = input("Guess a letter:\n".upper())

        try:
            if len(player_guess) > 1:
                raise ValueError(
                    f" You can only guess 1 letter at a time, you guessed"
                    f" {len(player_guess)} characters"
                )
            
            elif not player_guess.isalpha():
                raise ValueError(
                    f" You can only guess letters, you guessed {(player_guess)}"
                    f" which is not a letter"
                )
            
            elif len(player_guess) == 1 and player_guess.isalpha():
                if player_guess in guesswork:
                    raise ValueError(
                        f" You have already guessed {(player_guess)}"
                    )

                elif player_guess not in random_words:
                    info = f" {(player_guess)} is not in"\
                              f" the word. You lose a life."

                    guesswork.append(player_guess)
                    tries -= 1

                else:
                    info = f" {player_guess} is in the"\
                              f" word. Well done!"

                    guesswork.append(player_guess)
                    secret_word_list = list(secret_word)
                    indi = [i for i, letter in enumerate(random_words)
                            if letter == player_guess]
                    for index in indi:
                        secret_word_list[index] = player_guess
                        secret_word = "".join(secret_word_list)
                    if "_" not in secret_word:
                        game_over = True
                                        
        except ValueError as e:
            print(f"{e}. Please try again.")
            continue

        print(hangman_tries(tries))

        if tries > 0:
            print(info)
            print(f" Lives: {tries}\n")
            print(" The word to guess: " + " ".join(secret_word) + "\n")
            print(" Letters guessed: " + ", ".join(sorted(guesswork)) + "\n")

    if game_over:
        print(f"Congratulations. {random_words} was the correct word!")
        player_win()

    else:
        print(f" The correct word was {random_words}")
        hangman_win()

    restart(total_lives)
    

def restart(total_lives):
    """
    The player gets an option to restart the game....
    """
    restart = False
    while not restart:
        restart_game = input(" Would you like to play again? \"Y/N\"").upper()

        try:
            if restart_game == "Y":
                restart = True
                hidden_words = get_word()

                game_play(hm_word, total_lives)

            elif restart_game == "N":
                restart = True
                print("\n")
                main()

            else:
                raise ValueError(
                    f" You must type in Y or N. You typed {(restart_game)}"
                )

        except ValueError as e:
            print(f"{e}.Please try again.")

def player_win():
    """
    Graphic that displays if the player win!
    """
    print(
        """
        __   __
        \\ \\ / /__  _   _
         \\ V / _ \\| | | |
          | | (_) | |_| |
          |_|\\___/_\\__,_| _
        __      _(_)_ __ | |
        \\ \\ /\\ / / | '_ \\| |
         \\ V  V /| | | | |_|
          \\_/\\_/ |_|_| |_(_)
        """ 
        )

def hangman_win():
    """
     Graphic that displays if the player loose!
    """
    print(
        """
          ____
         / ___| __ _ _ __ ___   ___
        | |  _ / _` | '_ ` _ \\ / _ \\
        | |_| | (_| | | | | | |  __/
         \\____|\\__,_|_| |_| |_|\\___|
         / _ \\__   _____ _ __| |
        | | | \\ \\ / / _ \\ '__| |
        | |_| |\\ V /  __/ |  |_|
         \\___/  \\_/ \\___|_|  (_)
        """ 
        )

def hangman_tries(tries):
    """
    Displays hangman graphic based on lives left
    """
    tries_left = [
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        / \\
        |\\
        ========
        """,
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        /
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |        /|\\
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |        /|
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |         |
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |
        |
        |
        |\\
        ========
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |\\
        ========
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |
        ========
        """,
        """
        |/
        |
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

def rules():
    """
    Game rules
    """
    print(
        """
        Guess the word by inputting letters.
        If you get a letter wrong you will lose a life
        and the hangman will begin building.
        When you reach 0 lives you will be hanged
        and it is game over!
        """
    )
    start_menu = input(" Press enter to return to the start" "menu\n")
    print("\n")
    start()

    

def start():
    """
    Runs the game
    """
    print(hangman_tries(0))
    level = welcome_screen()
    if level == "default":
        num_lives = 7
    else:
        num_lives = choose_difficulty()

    words = get_word()
    game_play(words, num_lives)


start()