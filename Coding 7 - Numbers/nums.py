'''
The file Numbers.txt within this program's directory contains a set
of integers. This program (without using lists) does the following:
Displays the number of numbers in the file
Displays the largest number in the file
Displays the smallest number in the file

Creative Element: Implementation of the helpful 'hasNextLine()' and
'getNextLine()' functions, similar to Java file IO for easier file
traversal. Additionally, instead of implementing seperate highest num
and lowest num functions, there is a findExtreme function from which
modes can be selected for either the highest or lowest value. Finally,
a 'master' class can be called which finds the number of numbers, as
well as the max and min and returns them in a tuple.
'''

# Will Allen
# CSIS 1300
# March 28, 2023


def getFile(fileName: str):
    '''
    Opens a given file, and returns its file object. Assumes a desired pure
    read mode, and begins the pointer at the begining of the file. The file
    opened using this method should be closed using the .close() function.
    It also assumes that the file is located in its own directory. It first
    tries accessin the file directly, then adding the folder it's in to grab
    the file correctly.
    \n
    Input: fileName - A string with the file's name, and path if necessary.\n
    Output: The file in a read-only state.
    '''
    # Attempt to open the file as-is
    try:
        return open(fileName, 'r')
    except:
        return open("Coding 7 - Numbers/" + fileName, 'r')


def hasNextLine(file) -> bool:
    '''
    For a given file, returns 'true' if there is a nextLine to read, 
    i.e. the file has not been fully read. Otherwise, return false.
    \n
    Input: file - a text file to check.\n
    Output: Wheter the file can continue to be read.
    '''
    # Get the original index of the file pointer
    initPos = file.tell()
    # Check to see if reading a new character returns anything
    moreChars = file.read(1) != file.read(0)
    # Return the pointer to the correct position
    file.seek(initPos, 0)
    # Return wheter there is more to read
    return moreChars


def nextLine(file) -> str:
    '''
    For a given file, returns all of the characters either up until the
    next newline, or until the end of the file.
    \n
    Input: file - The file to be read.\n
    Output: nextLine - A string of the characters until the next line.
    '''
    # Establish the return string
    line = ""
    # Iterate through the file until the next newline or EOF is reached
    while (True):
        # Get the next char
        char = file.read(1)
        # Check if we've reached the end of the line or file
        if char == "\n" or char == "":
            # If so, return
            return line
        else:
            line += char


def numberOfNumbers(file) -> int:
    '''
    For the given file, returns the number of numbers it contains. For our
    purposes, this is the same as the number of lines it contains, as each
    line contains a number. Though it scans the whole file, it does not change
    the file's pointer location.
    \n
    Input: file - The file to be scanned.\n
    Output: The number of numbers as an integer.
    '''
    # Store the initial file pointer location
    initPos = file.tell()
    # Reset and read through for the number of numbers
    file.seek(0, 0)
    numNums = 0
    while (hasNextLine(file)):
        # Check to make sure the line isn't empty
        if nextLine(file) != "":
            numNums += 1
    # Reset to the initial position
    file.seek(initPos, 0)
    # Return the found number
    return numNums


def extremeNum(file, mode: int) -> int:
    '''
    Finds the number at either the highest extreme or lowest extreme,
    depending on what mode is selected (either 1 or -1). The mode is
    multiplied by the numbers, since the largest negative number is
    also the smallest positive number.
    \n
    Input: file - The file to be read.\n
    Input: mode - An int representing the desired operation: 1 for largest,
    and -1 for smallest.\n
    Ouput: Either the highest/lowest number, by mode, or None if an error was
    encountered parsing the data.
    '''
    # Store the initial file pointer location
    initPos = file.tell()
    # Reset and read through for the number of numbers
    file.seek(0, 0)
    # Assume the first item is the extreme
    try:
        extreme = int(nextLine(file))
    except:
        # An error was encountered, return nothing
        return None
    while (hasNextLine(file)):
        # Check to make sure the line isn't empty
        next = nextLine(file)
        if next != "":
            # Modify the values by the mode
            try:
                next = int(next)
            except:
                return None
            # Store the new extreme value
            if next * mode > extreme * mode:
                extreme = next
    # Reset to the initial position
    file.seek(initPos, 0)
    # Return the found number
    return extreme


def numMaxMin(file) -> tuple[int, int, int]:
    '''
    Finds the number, maximum, and minimum of the numbers in the
    provided file. May return none if an error is encountered.
    \n
    Input: file - The file to be read.\n
    Output: [Number of numbers, maximum number, minimum number] as a tuple.
    '''
    # Store the initial file pointer location
    initPos = file.tell()
    # Reset and read through for the number of numbers
    file.seek(0, 0)
    numNums, max, min = 1, 0, 0
    try:
        max = int(nextLine(file))
        min = max
    except:
        return None
    while (hasNextLine(file)):
        next = nextLine(file)
        # Check to make sure the line isn't empty
        if next != "":
            # There's one more number
            numNums += 1
            # Parse the string from nextLine
            try:
                next = int(next)
            except:
                return None
            # Check for new max
            if max < next:
                max = next
            # Check for new min
            if min > next:
                min = next
    # Reset to the initial position
    file.seek(initPos, 0)
    # Return the found number
    return (numNums, max, min)


# Run some tests
fileName = "Numbers.txt"
file = getFile(fileName)
print("The number of numbers in", fileName, "is", numberOfNumbers(file))
print("The highest number in", fileName, "is", extremeNum(file, 1))
print("The lowest number in", fileName, "is", extremeNum(file, -1))

fullInfo = numMaxMin(file)
print("Gathered all at once, there are", fullInfo[0], "numbers, with a maximum "
      "value of", fullInfo[1], "and a minimum value of", fullInfo[2])


'''
Thoughts:
The prevention of using lists was probably the most informative part of this
assignment, if for no other reason than reminding me how nice working with
lists is. Even with the nextLine helper functions, I feel as though the solution
I came up with was not nearly as elegant or efficient as simply reading the file
as a list of lines would have been.
'''
