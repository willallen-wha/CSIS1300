"""
This program checks to see if a word has three consecutive letters which are also
consecutive letters in the alphabet. An example of such a word is THIRSTY, which
has the substring RST, which features three consecutive alphabetical letters in
order in the word.
Creative Element: Instead of implementing the consecutive check by utilizing the
word function, I instead elected to compare the char codes of the letters after
casting to lowercase, as the lowercase letters have incresing numerical value
as they increase. Additionally, I implemented a generalized function which checks
to see if any number of consecutive letters appears, not just 3. Finally, I
implemented a function which counts the total number of consecutive letters.
"""

# Will Allen
# CSIS 1300
# March 14, 2023


def isThresholdConsecutive(word: str, thresh: int) -> bool:
    """
    A function which determines if the provided word has a satisfactory number of
    consecutive letters which are also consecutive letters alphabetically, as determined
    by the threshold given. Additionally, checks if the provided element is a valid
    letter and resets if not.
    \n
    Input: word - The string which is to be tested.
    Input: thresh - An int representing the desired number of consecutive letters
    Output: Whether or not the word has the three letter pattern desired, a boolean.
    """
    # Cast the string to lowercase for easier usage
    word = word.lower()

    # The number of consecutive letters
    consCount = 1
    # Iterate through the string, checking for consecutively larger charcodes
    # Don't check the last letter, as it has no 'next' letter
    for i in range(0, len(word) - 1):
        # Checks to make sure we are examining a letter
        if ord(word[i]) >= 97 and ord(word[i]) <= 122:
            # Check if the next letter is alphabetically one above the current
            if ord(word[i]) + 1 == ord(word[i + 1]):
                # If so, increment the counter
                consCount += 1
            # Otherwise, reset the counter
            else:
                consCount = 1
            # Check to see if the desired threshold has been reached
            if consCount == thresh:
                return True
        else:
            consCount = 0
    # If the end of the word has been reached and the threshold hasn't been,
    # then return false
    return False


def isTripleConsecutive(word: str) -> bool:
    """
    A function which determines if the provided word has three consecutive 
    letters which are also consecutive letters alphabetically. Utilizes the 
    isThresholdConsecutive function with hardcoded 3 threshold.
    \n
    Input: word - The string which is to be tested.
    Output: Whether or not the word has the three letter pattern desired, a boolean.
    """
    return isThresholdConsecutive(word, 3)


def countConsecutive(word: str) -> int:
    """
    A function which counts the number of consecutive letters which are 
    also consecutive letters alphabetically.
    \n
    Input: word - The string which is to be tested.
    Output: The highest number of consecutive letters in a row
    """
    # Cast the string to lowercase for easier usage
    word = word.lower()

    # The number of consecutive letters
    consCount = 1
    highestCons = 1
    # Iterate through the string, checking for consecutively larger charcodes
    # Don't check the last letter, as it has no 'next' letter
    for i in range(0, len(word) - 1):
        # Checks to make sure we are examining a letter
        if ord(word[i]) >= 97 and ord(word[i]) <= 122:
            # Check if the next letter is alphabetically one above the current
            if ord(word[i]) + 1 == ord(word[i + 1]):
                # If so, increment the counter
                consCount += 1
            # Otherwise, reset the counter
            else:
                consCount = 1
        else:
            consCount = 0

        # Check to see if a new 'high score' has been reached
        if consCount > highestCons:
            highestCons = consCount
    # If the end of the word has been reached and the threshold hasn't been,
    # then return false
    return highestCons


def getInput() -> None:
    """
    Gets input for the other functions. This function takes no input and
    returns nothing, and acts more as the main function.
    """
    # Request input from the user
    word = input("Enter a word: ")
    # First check for three consecutive letters
    if isTripleConsecutive(word):
        print(word, "contains three successive letters "
              "in consecutive alphabetical order.")
    else:
        print(word, "does not contain three successive letters "
              "in consecutive alphabetical order.")
    print("In fact,", word, "contains", str(countConsecutive(word)),
          "sucessive letters in consecutive alphabetical order.")


# Do some tests
while True:
    getInput()


# At first, I wasn't quite sure the proper way to approach this program.
# I first considered a 'dictionary' of three-letter consecutive phrases
# (ABC, BCD, CDE, etc.) but decided against that. I then considered doing
# if str[i] == a and str[i + 1] == b but decided against that as well, as
# it would have been far too long. I then realized the char codes were set
# up such that consecutive letters (as long as they are the same case) would
# also have consecutive keycodes, so I decided to take advantage of this fact
# since str[i] + 1 == str[i + 1] is a much easier check to make.
