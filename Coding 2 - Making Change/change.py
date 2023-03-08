"""
A program to make change and split money for an amount of money.

The program's input is the amount to make change for as a string in the format XX.YY
with XX being the dollar amount and YY being the cents.

The program outputs the number of each denomination of coins and bills 
needed to make accurate change.
"""

# Will Allen
# 30 Jan, 2023
# CSIS 1300 Section 1

# Creative Section: Input validation to ensure only valid values are entered, #
# as well support for splitting dollar amounts into 1, 5, 10, 20, 50, and 100 bills#

amount = input("Enter the amount to make change for: $")

try:
    amount = float(amount)
    centString = str(amount)[str(amount).index('.')+1:]
    if len(centString) > 2:
        print("Please enter valid change (No more than two digits for cents).")
except TypeError:
    print("Please enter your value in the format XX.XX")
    exit()

# Establish some variables
numHunds, numFifts, numTwens, numTens, numFives, numOnes = 0, 0, 0, 0, 0, 0
numPens, numNicks, numDimes, numQuarts = 0, 0, 0, 0

# Cast the values into seperate dollar amounts and cent amounts
dolAmount = int(amount)
# This very gross line is necessary to not lose accuracy
centAmount = int(centString)
print("Input amount: ", dolAmount, ".", centAmount)
print("In oder to give change for $" + str(amount) + ", you would need:")
print("----------------------------------------------------------------")

# Number of hundred dollar bills is the dollar amount divided by 100, rounded down.
numHunds = int(dolAmount / 100)
dolAmount -= numHunds * 100
# Remove the hundreds and do similar math
# Note that this is necessary as simple modular arithmetic leads to errors
# when computing change for $70 or 35 cents.
numFifts = int(dolAmount / 50)
dolAmount -= numFifts * 50
numTwens = int(dolAmount / 20)
dolAmount -= numTwens * 20
numTens = int(dolAmount / 10)
dolAmount -= numTens * 10
numFives = int(dolAmount / 5)
dolAmount -= numFives * 5
# The number of dollar bills needed is all the remaining dollar amount that
# cannot be represented by larger bills.
numOnes = dolAmount

# Print each bill type and the amount of them it would take
print(str(numHunds) + " hundred dollar bills")
print(str(numFifts) + " fifty dollar bills")
print(str(numTwens) + " twenty dollar bills")
print(str(numTens) + " ten dollar bills")
print(str(numFives) + " five dollar bills")
print(str(numOnes) + " one dollar bills")

# The number of quarters is the amount given divided by 25 then truncated.
numQuarts = int(centAmount / 25)
centAmount -= numQuarts * 25
# The number of dimes is the amount left after removing all quarters,
# then similarly divided by 10 and truncating.
numDimes = int(centAmount / 10)
centAmount -= numDimes * 10
# Similar logic applies here, with the number of nickels being the amount
# left after removing dimes and dividing by 5.
numNicks = int(centAmount / 5)
centAmount -= numNicks * 5
# Finally, pennies are the amount remaining
numPens = centAmount

# Print each coin type and the amount of them it would take
print(str(numQuarts) + " quarters")
print(str(numDimes) + " dimes")
print(str(numNicks) + " nickles")
print(str(numPens) + " pennies")

print("----------------------------------------------------------------")
