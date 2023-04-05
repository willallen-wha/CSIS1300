'''
The file StatesANC.txt within this program's directory contains a list
of all 50 states, their abbreviations, thier nicknames, and their capitals.
This program utilizes that text file and performs two functions:

Displays the states (and their capitals) for which the name of the 
state and its capital begin with the same letter.

Requests the name of a state as input and displays the abbreviation, 
nickname, and capital of the state. 

Creative Element: Two forms of each method is implemented: one which assumes
the file has already been read and one which has not. The one which does
not assume has an optional parameter in the event the code is not being run
from the same level as the file is to allow for custom filepaths. In testing,
this is leveraged as my file structure is different from the github.
Additionally, error detection prevents the disp_ANC function from exiting
until a valid state is entered.
'''

# Will Allen
# CSIS 1300
# March 28, 2023


def disp_same_letter_read(path: str = "StatesANC.txt") -> list:
    '''
    Displays the list of states which have a capital that
    begins with the same letter as the state. A string is passed as
    an optional argument which contains the filepath/name for the
    StatesANC file if it is in a different directory than the code.
    This version does not assume the file has already been read.
    \n
    Input: path - A string which represents the path to the StatesANC.txt
    Output: A list of states which fulfill the requirements above in the format
    of the text file.
    '''
    # Reads the file in
    states_file = open(path, "r", encoding="utf-8")
    # Read the list of states in and close the file
    states = states_file.readlines()
    states_file.close()
    # Call the function which assumes the file has been read
    return disp_same_letter(states)


def disp_ANC_read(path: str = "StatesANC.txt") -> str:
    '''
    Displays the ANC of states which have the name requested by the user
    A string is passed as an optional argument which contains the filepath/name
    for the StatesANC file if it is in a different directory than the code.
    This version does not assume the file has already been read.
    Note the state name is not input, and instead is gathered during the function.
    \n
    Input: path - A string which represents the path to the StatesANC.txt
    Output: The string which contains ANC info for the state specified by the user.
    '''
    # Reads the file in
    states_file = open(path, "r", encoding="utf-8")
    # Read the list of states in and close the file
    states = states_file.readlines()
    states_file.close()
    # Call the function which assumes the file has been read
    return disp_ANC(states)


def disp_same_letter(states: list) -> list:
    '''
    Displays the list of states which have a capital that
    begins with the same letter as the state. A string is passed 
    which contains the contents of the StatesANC file, and is
    called by the version of this function that does not
    assume the file has already been read.
    \n
    Input: states - A list which contains each line of StatesANC.txt as a string
    Output: A list of states which fulfill the requirements above in the format
    of the text file.
    '''
    # Generate the list of states which meets the requirements
    states_satisfac = []
    for state in states:
        # Split on the commas
        state_ar = state.split(",")
        # Check if the first letter of index 0 (state name) and
        # index 3 (state capital) match
        if state_ar[0].lower()[0] == state_ar[3].lower()[0]:
            states_satisfac.append(state)
    return states_satisfac


def disp_ANC(states: list) -> str:
    '''
    Displays the ANC of states which have the name requested by the user
    A list of states read is passed as an argument usually from the stricter version
    of the function. This version assumes the file has already been read.
    Note the state name is not input, and instead is gathered during the function.
    \n
    Input: states - A list which contains each line of StatesANC.txt as a string
    Output: The string which contains ANC info for the state specified by the user.
    '''
    # Don't exist until a valid state is found
    while True:
        # Request a state
        req = input("Enter a state: ")
        # Search the states list for the requested state
        for state in states:
            # If this is it, epic return
            if state.split(",")[0].lower() == req.lower():
                return state
        # If all states are searched and no match is found, restart
        print("No matching state found. Check spelling and try again.")


# "Main" function
# Read in the states info
file = open("Coding 8 - States/StatesANC.txt", encoding="UTF-8")
states_list = file.readlines()
file.close()
# Display the states information that meet criteria
print("States with capitals beginning with the same letter as the state:")
for line in disp_same_letter(states_list):
    state_info = line.split(",")
    # Cut the newline
    state_info[3] = state_info[3][:len(state_info[3]) - 1]
    # The horrible printline is necessary to cut newlines
    print(state_info[0] + " with a capital of " + state_info[3])
# Repeatedly display state info
while True:
    ANC_info = disp_ANC(states_list).split(",")
    print(ANC_info[0] +"-\nAbreviation: " + ANC_info[1]
          + "\nNickname: " + ANC_info[2]
          + "\nCapital: " + ANC_info[3])
