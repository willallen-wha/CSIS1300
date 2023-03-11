"""
This program provides information on the height of a ball with given initial
velocity and height. Specifically, the program supports two functions: finding
the maximum height of the ball, and finding the time at which the ball hits the
ground.
Creative Element: Instead of estimating by checking the ball's position every
0.1 seconds, the program instead oscilates between positive and negative height
values at increasingly smaller intervals to ensure that an answer that is
accurate to at least 3 decimal places is found, and it is also found at optimal
efficiency.
"""

# Will Allen
# CSIS 1300
# March 8, 2023


def maxHeight(initHeight: float, initVeloc: float) -> float:
    """
    A function which returns the maximum height reached of a ball thrown straight in the air.
    The ball reaches its maximum height after v/32 seconds, which is then passed to the
    function for getting the height at a given time.
    \n
    Input: initHeight - A float representing the initial height
    Input: initVeloc - A float representing the initial velocity
    Output: The maximum height reached, a float
    """
    # Calculate the max height reached, which occurs at v/32
    timeAtMax = initVeloc / 32
    # The max height is the initial height plus max height
    return heightAtTime(initHeight, initVeloc, timeAtMax)


def heightAtTime(initHeight: float, initVeloc: float, time: float) -> float:
    """
    A function for getting the height of a ball at given time which has been thrown straight up 
    in the air. The function follows the motion equation h = initHeight + initVeloc*time - 16*time^2.
    \n
    Input: initHeight- The initial height of the ball, a float
    Input: initVeloc - The initial velocity of the ball, a float
    Input: time - The time at which to find the height, a float
    Output: The height of the ball at the given time, a float
    """
    # Square time
    timeSq = time * time
    # Return result of the formula
    return initHeight + initVeloc * time - 16 * timeSq


def timeForGround(initHeight: float, initVeloc: float) -> float:
    """
    A function which determines the approximate time at which a ball hits the ground if
    thrown straight up in the air. The function oscillates between incresingly smaller
    time increments to brute-force find the time. It assumes height begins as a positive
    number.
    Input: initHeight - The initial height of the ball, a float
    Input: initVeloc - The initial velocity of the ball, a float
    Output: The approximate time at which the ball hits the ground, a float
    """
    # Begin at t = 0, where we know the height is positive.
    # Then, increment t by 1 second until we find where it becomes negative
    time = 0
    while heightAtTime(initHeight, initVeloc, time) > 0:
        time += 1
    # Oscillate the other way to get closer
    while heightAtTime(initHeight, initVeloc, time) < 0:
        time -= 0.1
    # Oscillate the other way to get even closer
    while heightAtTime(initHeight, initVeloc, time) > 0:
        time += 0.01
    # One final, closer oscillation
    while heightAtTime(initHeight, initVeloc, time) < 0:
        time -= 0.001
    # Round the number to the accuracy of 3 decimals and return
    return round(time, 3)


def getInput() -> None:
    """
    Gets input for the other functions, then checks the inputs
    for validity using isValid. This function takes no input and
    returns nothing, and acts more as the main function.
    """
    # Request input from the user
    height = input("Enter the inital height of the ball: ")
    # Check for input validity, and request again if not
    while not isValid(height):
        print("Please enter valid input. The input must be a positive number.")
        height = input("Enter the inital height of the ball: ")
    # Once validity has been confirmed, force it to float
    height = float(height)
    
    velocity = input("Enter the initial velocity of the ball: ")
    # Check for input validity, and request again if not
    while not isValid(velocity):
        print("Please enter valid input. The input must be a positive number.")
        velocity = input("Enter the initial velocity of the ball: ")
    # Once validity has been confirmed, force it to float
    velocity = float(velocity)

    # Get the max height and the ground time
    print("The maximum height of the ball is ", maxHeight(height, velocity), " feet.")
    print("The ball will hit the ground after approximately ", \
          timeForGround(height, velocity), " seconds.")
    

def isValid(inp) -> bool:
    """
    Determine if provided input is valid. Validity is determined by
    wether or not the input is a positive number.
    \n
    Input: inp - The input provided, any type.
    Output: Whether the input is valid, a boolean.
    """
    # Attempt to cast the input to a float
    try:
        float(inp)
    except:
        return False
    # If it can be cast, ensure it is positive
    inp = float(inp)
    return inp > 0

# Do some test outputs
getInput()