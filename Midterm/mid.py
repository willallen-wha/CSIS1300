"""
This program has two functions, both of which fulfill one of the requirements for the midterm.

errorDetection takes as input a number or string, which it then performs the described algorithm on.

findPalindrome takes an optional string as input, and then returns whether the provided string is a palendrome.

Creative aspect: Input validation on credit card to ensure only numbers are entered. Spaces are also
cleared since many places normalize putitng spaces between each 4 digits. Additionally, the palindrome
function can accept either the string as a parameter, or no parameter and ask the user for the input string.
Finally, there is a main loop which allows iterating through both functions by user's requirements.
"""

# Will Allen
# CSIS 1300
# February 25, 2023


def errorDetection(cardNumber):
    """
    A fucntion which checks for errors in typing a credit card number.\n
    It takes as input the card number in either string or int form. It then strips any
    spaces and performs the following algorigm:\n
    -Take every even indexed number and double it, subtracting 9 if the result is two digits. Sum these numbers.\n
    -Take every odd indexed number and sum them directly.\n
    -Add these two sums and check if they are divisible by 10. If so, the number is valid.\n
    \n
    Input: cardNumber (String, int)\n
    Output: Boolean\n
    """
    # Cast card number to a string for consistent code execution.
    cardNumber = str(cardNumber)
    # Clear spaces and check for any letters, misc. punct, ect
    cardNumber = cardNumber.replace(" ", "")
    try:
        int(cardNumber)
    except:
        print("Error parsing the card info. Likely this means there are ",
              "letters or punctuation. Please re-enter.")
        return False

    # The first and second digit sums
    firstDig, secondDig = 0, 0

    # Sum the numbers into their respective digit sums
    for i in range(len(cardNumber)):
        dig = int(cardNumber[i])
        # If the number is the leftmost or every other after
        if i % 2 == 0:
            # Double that number
            dig *= 2
            # If it's two digits, subtract 9
            if dig >= 10:
                dig -= 9
            # Add into the first digit sum
            firstDig += dig
        else:
            secondDig += dig

    # Now that the sums are made, add them together and check division
    totalSum = firstDig + secondDig
    if totalSum % 10 == 0:
        print("The card number is valid.")
        return True
    else:
        print("The card number is not valid.")
        return False


def findPalindrome(str=None):
    """
    A function which checks if the provided string is a palendome. It strips
    all punctuation, spaces, etc., then casts to uppercase to compare only the letters/digits.\n
    If no string is passed, it will ask the user for input.\n
    Input: str(String) - the string to be check.\n
    Output: Boolean (Is the string a palindrome).\n
    Example:\n
    >>>findPalindrome("Alabama")
     false
    >>>findPalindrome("Rac!e?c   a!!r")
     true
    """
    # Get user input for the palindrome if necessary
    if str == None:
        str = input("Enter a word or phrase: ")
    orgStr = str
    # Clean up the string
    replaceChars = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
                    "-", "_", "=", "+", "[", "]", "{", "}", "\\", "|", ";", ":",
                    "'", "\"", ",", "<", ".", ">", "/", "?", " "]
    for char in replaceChars:
        str = str.replace(char, "")
    # Cast it all to capitals
    str = str.upper()
    # Check if the same forward and backwards
    if str == str[::-1]:
        print(orgStr, "is a palindrome.")
    else:
        print(orgStr, "is not a palindrom.")
    return str == str[::-1]


# Initial tests
errorDetection(2246)
findPalindrome("Racecar")

# Main loop
while True:
    print("Please select a function: ")
    print("1: Credit card number validation")
    print("2: Palindrom selection")
    choice = input("Selection (1 or 2): ")
    if choice == "1":
        errorDetection(input("Please enter a credit card number: "))
    elif choice == "2":
        findPalindrome()
    elif choice == "q":
        exit()
    else:
        print("Invalid input, please enter either 1, 2, or q to quit.")
