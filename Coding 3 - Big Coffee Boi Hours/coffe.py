"""
This program gives information about how much caffine will be left in
a person's system after a certain amount of time. Multiple functions
are included, which include:

timeUntil - The amount of time (in whole hours) until the given start
    amount falls below the given end amount. No rounding occurs.

amountAtTime - The amount of given start caffine left in the system
    after given amount of time (in hours) has elapsed. Rounded to 2 decimals.

amountWithConsumption - The amount of caffine left in the system if
    starting with a given amount after a given amount of time (in hours)
    if more caffine is consumed at a given interval (in hours) of a 
    given amount.

All amounts are assumed to be 130 when the functions are called, but the 
decay rate of 13% is hard-coded.
"""

# Will Allen
# CSIS 1300
# Feb 9, 2023


# Returns the amount of time needed to have end mg
# of caffine left in system if start mg is ingested.
# Only checks at hour marks, so will give first hour
# under that amount.
#
# Start: The beginning amount of caffine, in mg
# End: The desired amount to end under, in mg
def timeUntil(start, end):
    # Begin at t = 0
    numHours = 0
    # Reduce the amount of caffine in the system by 13%,
    # then check to see if below the desired amount.
    while (start * (.87 ** numHours) > end):
        # If not, increase by another hour.
        numHours += 1
    # If so, return that many hours.
    return numHours


# Returns the amount of caffine left in the system after
# a certain amount of time if caffine started at start mg.
#
# Start: The beginning amount of caffine, in mg
# Time: The amount of time to let the caffine absorb, in hours
def amountAtTime(start, time):
    # This one is a pretty simple exponential function.
    return round(start * (0.87 ** time), 2)


# Returns the amount of caffine left in the system after
# a certain amount of time, if continued consumption occurs.
#
# Start: The beginning amount of caffine, in mg
# Time: The amount of time to let the caffine absorb, in hours
# Frequency: The amount of time between consuming more caffine, in hours
# Amount: The amount consumed during absorbtion, in mg
def amountWithConsumption(start, time, frequency, amount):
    # Begin with the proper amount of caffine at time = 0 hours
    currentCaffine = start
    currentTime = 0
    # Iterate through as time goes on
    while currentTime <= time - frequency:
        # Reduce the caffine by the appropriate amount
        currentCaffine *= (0.87 ** frequency)
        # Increase the time accordingly
        currentTime += frequency
        # Drink more caffine
        currentCaffine += amount
    # Do the last iteration of just the right amount
    currentCaffine *= (0.87 ** (time - currentTime))
    # Return how much caffine there is left
    return round(currentCaffine, 2)


# Do some test outputs
print("Assuming a person consumes an 8oz cup of coffee which contains 130mg of caffine:")
print("Less than 65mg remains after", timeUntil(130, 65), "hours.")
print("After 24 hours,", amountAtTime(130, 24), "mg of caffine will remain.")
print("If a person were to drink a new cup hourly,",
      amountWithConsumption(130, 24, 1, 130), "mg of caffine remain.")

# Test ouputs not required by the assignment
print()
print("Less than 1mg of caffine will remain after ", timeUntil(130, 1), "hours.")
print("After 5 hours,", amountAtTime(130, 5), "mg remains.")
print("If a new cup is drunk every half hour,", amountWithConsumption(130, 24, 0.5, 130),
      "mg will remain after 24 hours.")
