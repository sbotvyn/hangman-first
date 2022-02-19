from rich.console import Console
import rich
from random import choice
import os

def Hangman():

    console = Console(width=110)

    pics = ['''
        +---+
        |   |
            |
            |
            |
            |
            |
            |
            |
      =========''', '''
        +---+
        |   |
        |   |
            |
            |
            |
            |
            |
            |
      =========''', '''
        +---+
        |   |
        |   |
        |   |
            |
            |
            |
            |
            |
      =========''', '''
        +---+
        |   |
        |   |
        |   |
        |   |
        O   |
            |
            |
            |
      =========''', '''
        +---+
        |   |
        |   |
        |   |
        |   |
        O   |
        |   |
            |
            |
      =========''', '''
        +---+
        |   |
        |   |
        |   |
        |   |
        O   |
        |\  |
            |
            |
      =========''', '''
        +---+
        |   |
        |   |
        |   |
        |   |
        O   |
       /|\  |
            |
            |
      =========''', '''
        +---+
        |   |
        |   |
        |   |
        |   |
        O   |
       /|\  |
       /    |
            |
      =========''', '''
        +---+
        |   |
        |   |
        |   |
        |   |
        O   |
       /|\  |
       / \  |
            |
      =========''', '''
        +---+
        |   |
        |   |
        |   |
        |   |
      (X_X) |
       /|\  |
       / \  |
            |
      ========='''
            ]

    list = ['jis', 'zine', 'alphonse', 'scottish', 'carolina', 'niv', 'microfiber', 'perfect', 'recordable', 'disperse',
            'modernize', 'drags', 'grapple', 'macedonia', 'milfs', 'brooding', 'maxxum', 'notified', 'preis',
            'enrolments', 'certs', 'blower', 'stroke', 'patriot', 'ucs', 'doors', 'inaction', 'sar', 'preferring',
            'reduced', 'annotations', 'werden', 'agenda', 'standardisation', 'sala', 'lingere', 'overlaps',
            'approached', 'officially', 'contention', 'insatiable', 'ocz', 'investigated', 'msrp', 'finisher',
            'tabernacle', 'coping', 'juices', 'rodgers', 'lsl', 'programmable', 'asymptotic', 'bike', 'attempted',
            'drinkware', 'scratch', 'exert', 'xtreme', 'marcella', 'kultur', 'berg', 'spanish', 'bedspread',
            'sessional', 'ancestral', 'nida', 'petite', 'swivel', 'agency', 'airs', 'raped', 'swedes', 'fixed',
            'famvir', 'multitasking', 'sanctified', 'moyen', 'dialing', 'pace', 'etudes', 'salvatore', 'backlash',
            'insulate', 'grunge', 'tonya', 'abn', 'vassar', 'protesting', 'ibb', 'joystick', 'tiff', 'adhd', 'usaid',
            'virtual', 'occupation', 'automobiles', 'merges', 'dicke', 'fenders', 'bearded', 'deb', 'oriented',
            'herod', 'natchez', 'bulletproof', 'bassoon', 'began', 'comedy', 'fh', 'anglo', 'renewed', 'petal',
            'savings', 'voyeurweb', 'assess', 'fraunhofer', 'futility', 'shoemaker', 'newswatch', 'quench', 'visite',
            'restrictive', 'undersea', 'telepharmacy', 'biscayne', 'subsidize', 'proto', 'septic', 'vanish', 'canvas',
            'rangers', 'sylvain', 'webchanges', 'entertained', 'relation', 'commons', 'openbsd', 'slu', 'executable',
            'rainfall', 'livelihoods', 'roux', 'proclamation', 'hyannis', 'fatboy', 'cranial', 'kea', 'bakker',
            'psigate', 'new', 'masala', 'chong', 'pavel', 'handyman']

    reversed_pics = pics[::-1]
    secret_word = choice(list)
    failure_count = 10
    guessed_letters = ""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']

    console.print(" __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __.", style="bold white on blue", justify="center")
    console.print("|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  |", style="bold white on blue", justify="center")
    console.print("|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  |", style="bold white on blue", justify="center")
    console.print("|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  |", style="bold white on blue", justify="center")
    console.print("|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   |", style="bold white on blue", justify="center")
    console.print("|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__|", style="bold white on blue", justify="center")

    for letter in secret_word:
        if letter in letters:
            console.print('_ ', end="", style="bold orange1" )
        elif not letter.isalpha():
            console.print(f"{letter} ", end="", style="bold orange1")

    while failure_count > 0:

        user_guess = console.input(f"\nGuess a letter [underline]{letters}[/underline]: ")

        os.system("clear")

        if len(user_guess) > 1:
            print("Please, enter only one letter!")
            continue

        if user_guess in secret_word:
            console.print(f"Correct! There is one or more [bold green3]{user_guess}[/bold green3] in the secret word.")
        else:
            failure_count -= 1
            console.print(f"Incorrect. There are no [bold red3]{user_guess}[/bold red3] in the secret word. You have [bold blue1]{failure_count}[/bold blue1] tries left.")
            console.print(reversed_pics[failure_count], style="bold red3", justify="center")

        for letter in letters:
            if user_guess == letter:
                index = letters.index(letter)
                letters[index] = "#"

        guessed_letters = guessed_letters + user_guess
        wrong_letter_count = 0

        for letter in secret_word:
            if letter in guessed_letters:
                console.print(f"{letter} ", end="", style="bold orange1")
            elif not letter.isalpha():
                console.print(f"{letter} ", end="", style="bold orange1")
            else:
                console.print("_ ", end="", style="bold orange1")
                wrong_letter_count += 1

        if wrong_letter_count == 0:
            console.print(f"\nYou win! The answer was {secret_word}.", style="green3", justify="center")
            break
    else:
        console.print(f"\nYou lost! The answer was {secret_word}.", style="red3", justify="center")

while True:
    Hangman()
    restart = input("Do you want to restart the game? [y/n] ")
    os.system("clear")
    if restart == "y":
        continue
    else:
        break
    