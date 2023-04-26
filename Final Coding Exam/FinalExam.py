'''
This program randomly selects a number between 1 and 100, and then requests
the user guess the generated number. This process is repeated indefinitely until
the user guesses the correct number, at which point the code terminates and the
total number of guesses is displayed. Additionally, at each guess, robust input
validation occurs, notifying the program not only of what issue arose, but also
ensuring the user is notified of the proper input to give. Once a game is complete,
the user is presented with the option to restart. If restarting is not desired,
the program may be exited.

CREATIVE ELEMENT:
I decided to implement tkinter and the GUI elements discussed in the most recent chapter.
I have worked with GUI elements in Java before, and attempted to overall replicate the
general same idea, with some benefits and some detriments. Overall, I've come up with a
GUI with an output field, input field, and button, all centered and displaying nicely.
The GUI can be moved and scaled and things remain looking nice. My only concern is that
it may not work on MacOS, since I tested and ran the program on Windows, but I believe
it should work. The only real issue beyond that is that since it is my first use of
tkinter, there are some parts where the code flow becomes a bit muddled and the full
scope of what is being done can be confusing.
'''

import random
from tkinter import Tk, Label, CENTER, Entry, Button, END

# Will Allen
# CSIS 1300
# April 25, 2023


def genRandNum() -> int:
    '''
    Generate a random number between 1 and 100 (inclusive) that
    may be used by the computer as the metric for whether or not
    the guess is correct.
    \n
    Input: None
    Output: A random int between 1 and 100 inclusive.
    '''
    # Generate the number between 1 an 100 and return it
    return random.randint(1, 100)


def getValidInput(inp: str) -> tuple[int, int]:
    '''
    Attempts to recieve validated input from the user. The input is expected to
    only be integers, and any other items will marked as errors. The function returns
    a tuple, with the first item holding the "exit code" of the method, which
    represents the validity of the input recieved, and the second item holding
    the validated input.
    \n
    Input: The input to be validated
    Output: Tuple of the form [int, int]\n
    The first item is the exit code. Exit code 0 means there was no error, and the input
    is validated.
    - Exit code 1 means the value entered is not a number.
    - Exit code 2 means the value entered is not a whole number.
    - Exit code 3 means the item entered was outside the expected range of 1 to 100.
    - Exit code -1 means an unexpected error occurred.
    The second item is the validated input (if applicable).
    '''
    # First, make sure the input is a whole number
    if "." in inp:
        # If there's a period, it's not
        return (2, None)
    # Now, remove any commas which may have been added and try parsing to int
    try:
        inp.replace(",", "")
        asIntInp = int(inp)
        # If conversion is sucessful, then we now check if the range is satisfied
        if asIntInp > 100 or asIntInp < 1:
            # Return appropriate exit code for out of range
            return (3, None)
        else:
            return (0, asIntInp)
    # If there's a value error, then the input is not a number
    except ValueError:
        return (1, None)
    # If an unexpected error occurs, return the proper exit code.
    # This disable block is required to ignore a general pylint exception catch error.
    # This is intentional, as a truly robust program should be able to recover from ALL
    # error, which requires a general exception block.
    except:  # pylint: disable=W0702
        return (-1, None)


def checkNumber(guess: tuple[int, int], value: int) -> int:
    '''
    Compares two numbers to see if the guess is correct. Will return 0 if the
    number is correct, or -1 if the guess is too low or +1 if the guess is too
    high.
    \n
    Input: guess - A tuple containing the the exit code of input validation and the input.
    Input: value - The value attempting to be guessed.
    Output: An int, either -1 if the guess is too low, 1 if the guess is too high, or 0 if the
    guess is correct.
    '''
    # Check if the guess is correct
    if guess[1] == value:
        return 0
    # Otherwise, return the proper signed 1
    else:
        dif = guess[1] - value
        return dif / abs(dif)


# Create root object
root = Tk()
# Set the title
root.title("Python Final Program")
# Set the size
root.geometry('350x200')
# Add a text field that outputs information
outField = Label(root, text="I have generated a number between 1 and 100.")
outField.place(relx=0.5, rely=0.25, anchor=CENTER)
# Add an entry field to enter the guess
guessField = Entry(root, width=10)
guessField.place(relx=0.5, rely=0.5, anchor=CENTER)

# Define some constant window functions
# Define the CurrentGame object


class CurrentGame:
    '''
    Class CurrentGame is designed to keep track of the current game, and help avoid
    accessing global variables and some other nasties.
    '''
    going = True
    rand = genRandNum()
    numGuess = 0


curGame = CurrentGame()


# Define some functions on the window
# Update the display based on a button clicked
def updateDisp(text: str, cur: CurrentGame) -> None:
    '''
    Updates the display according to the input text.
    \n
    Input: text - The text currently in the input field.
    Input: cur - The CurrentGame object tracking the current game.
    Output: None
    '''
    # Get input
    guessed = getValidInput(text)
    # Is the input valid?
    if guessed[0] != 0:
        # Ouput the proper error
        if guessed[0] == 1:
            outField.config(text="Please enter a number.")
        elif guessed[0] == 2:
            outField.config(text="Please enter a whole number.")
        elif guessed[0] == 3:
            outField.config(text="The number must be between 1 and 100.")
        else:
            outField.config(
                text="An unexpected error occurred. Please try again.")
    # If so, is it right?
    else:
        delta = checkNumber(guessed, cur.rand)
        # Too high
        if delta == 1:
            outField.config(text="Too high, try again.")
        # Too low
        elif delta == -1:
            outField.config(text="Too low. Try again.")
        else:
            # Goldilocks, we win
            gameWon(cur)
            return
    # Incremeent guesses
    cur.numGuess += 1


# Define a button and its functions
# On click, either restart or udpate the display
def clicked() -> None:
    '''
    This function is called on each button click. It allows the
    program to update each part of the GUI appropraitely.
    \n
    Input: None
    Output: None
    '''
    # We want to access the current game
    global curGame  # pylint: disable=W0602
    if not curGame.going:
        restart(curGame)
    else:
        updateDisp(guessField.get(), curGame)


# Add the button
but = Button(root, text="Guess", command=clicked)
but.place(relx=0.5, rely=0.75, anchor=CENTER)


# Restart the game by adjusting relevant items
def restart(cur: CurrentGame) -> None:
    '''
    Restarts the game. Set current guesses to 0, sets going to True,
    and generates a new Random number. Requires the CurrentGame object
    to manipulate.
    \n
    Input: cur - The CurrentGame object tracking the current game.
    Output: None'''
    cur.going = True
    cur.rand = genRandNum()
    cur.numGuess = 0
    outField.configure(text="I have generated a number between 1 and 100.")
    but.configure(text="Guess")


# Mark the game as having been won
def gameWon(cur: CurrentGame) -> None:
    '''
    Marks the current game as won. This prevents further guesses from counting,
    as well as allows the game to be reset.
    \n
    Input: cur - The CurrentGame Object tracking this game.
    Output: None'''
    # Update variables
    cur.going = False
    # Output results
    outField.config(text="Correct! You took " +
                    str(cur.numGuess) + " guesses.")
    # Clear the text input
    guessField.delete(0, END)
    but.config(text="Restart")


# Begin the output function
root.mainloop()


#
# Program Thoughts:
# Overall, tkinter (my creative element) was a very easy library to work with.
# I had worked with the JFrame library in Java before to generate UIs, and
# tkinter was somewhat easier, especially to pick up. I also initally
# wrote the program for CLI before switching to GUI, and the compartmentaliztion
# and of each method and function made the transition SIGNIFICANTLY easier, so
# I am incredibly happy I decided to implement most features that way. Additionally,
# I tested and ran this code on a windows machine. I hope that it works as well on
# Mac, but I simply don't have the machine necessary to test it on that OS so I can't
# assure that the formatting or functionality appears there as well. If it doesn't work,
# please let me know and I can try updating what needs updated so it runs on Mac.
#

#
# Class Thoughts:
# I enjoyed this class as an entry-level view at Python. As a senior this year,
# I would've appreciated a more in-depth approach, and I certainly would've preferred
# taking a deeper look at the object-parts of Python, but I understand such an
# approach isn't really realistic for a beginner, 1000 level class. The biggest thing
# I would change about the course is removing the use of linting, especially pylint.
# Pylint consistently made my code harder to read and more difficult to understand due
# to raising complaints about a number of minor details (using the global keyword,
# not using snake case, etc.) or sometimes creating warnings about intended behavior
# (referencing global variables in methods, overwriting values, doing a complete catch,
# etc.) and I often found myself looking into how to stop the errors as opposed to
# actually creating "better" code.
#
