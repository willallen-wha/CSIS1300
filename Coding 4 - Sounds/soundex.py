"""
This program returns the soundex code for a given word. It encodes a
word into a single letter followed by three numbers which gives
a rough guide on how to pronounce it. The algorithm is as follows:
Retain the first letter, then remove all instances of a, e, i, o, u, h, y, and w.
The following letters are encoded as follows:

b, f, p, and v become 1
c, g, j, k, q, s, x, and z become 2
d and t both become 3
l becomes 4
m and n become 5
r becomes 6

If multiple letters are encoded to the same number in a row, keep only the first.
Finally, truncate the resulting code to 4 characters long, or fill with 0s
to get to a length of 4 if necessary.
"""

# Will Allen
# CSIS 1300
# Feb 16, 2023


# Returns the soundex code for a given string.
# Relies on helper functions
#
# Str: The string to be turned into a soundex code
def getCode(str):
    # Retain the first letter
    code = str[0]
    # Transform the rest of the letters into the soundex code
    code += transformLetters(str[1:])

    # Ethier truncate the string or add onto it for proper formatting
    while (len(code) < 4):
        code += "0"
    return code[0:4]


# Drops letters we don't need and translates them into numbers
# the valid soundex codes
def transformLetters(str):
    # Some helpful variables
    strRemove, strOne, strTwo = "aeiouhyw", "bfpv", "cgjkqsxz"
    strThree, strFour, strFive, strSix = "dt", "l", "mn", "r"
    strReturn = "a"
    # Iterate through the string, replacing all letters
    for i in range(len(str)):
        # Check if that character needs removed
        if strRemove.count(str[i]) != 0:
            continue
        # Add the appropriate number, making sure not to repeat numbers
        if strOne.count(str[i]) != 0 and strReturn[len(strReturn) - 1] != "1":
            strReturn += "1"
            continue
        if strTwo.count(str[i]) != 0 and strReturn[len(strReturn) - 1] != "2":
            strReturn += "2"
            continue
        if strThree.count(str[i]) != 0 and strReturn[len(strReturn) - 1] != "3":
            strReturn += "3"
            continue
        if strFour.count(str[i]) != 0 and strReturn[len(strReturn) - 1] != "4":
            strReturn += "4"
            continue
        if strFive.count(str[i]) != 0 and strReturn[len(strReturn) - 1] != "5":
            strReturn += "5"
            continue
        if strSix.count(str[i]) != 0 and strReturn[len(strReturn) - 1] != "6":
            strReturn += "6"
            continue
    return strReturn[1:]


# Do some test outputs
print(getCode("Robert"))
print(getCode("Test"))
print(getCode("Carrot"))
print(getCode("Caret"))
print(getCode("Incredible"))
print(getCode("Uncredible"))
print(getCode("Heheheheheheheheh"))
print(getCode("Zimbabwe"))
print(getCode("Marimba"))
