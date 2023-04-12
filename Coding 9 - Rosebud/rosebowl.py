'''
The file Rosebowl.txt within this program's directory contains the
list of Rosebowl winning schools every year, by year of Rosebowl,
since the first Rose Bowl in 1902. Additionally, the file has been
updated as requested to contain the winners from 2014 to 2022. Using
this file, and with exception handling, the following functions are
performed:

- Display the name of teams which have won the Rose Bowl four or more
  times, as well as the number of wins for each of those teams.
- Display the name of every team, as well as the number of wins they
  have, ordered by the number of times they have won.

Creative Element: Firstly, I used a dictionary to hold the winners of the rose bowl.
This is because the dictionary is the closest object to a hashmap in most
other languages, which felt like the best way to contain the winners succinctly.
Additionally, hashmaps support constant time lookup, leading to a more effecient program.
I also added a function which sorts the dictionary based on number of wins, allowing
for more for more effecient searchnig and displaying. I also adjusted the file I/O
for better error management, as my home repo is set up different than the GitHub, which
should ensure better file I/O. Finally, I added the functionality of showing any
number of winners by the number of games they had won. This way, in order to display
all winners, it only needs to request anyone who was won more than 0 times. This
allows for a more dynamic and complete program.
'''

# Will Allen
# CSIS 1300
# April 11, 2023


def attempt_get_file(filename: str):
    '''
    Attempts to open a file with provided name, and if sucessessful, returns
    the file. If not sucessful, returns None.
    \n
    Input: fileName - A string with the file's name, and path if necessary.\n
    Output: The file in a read-only state, or null if an error is encountered.
    '''
    # Attempt to open the file as a read-only item
    try:
        # First attempt directly
        try:
            return open(filename, 'r', encoding="UTF-8")
        # Then attempt using the filepath adjusted for personal computer
        except FileNotFoundError:
            return open("Coding 9 - Rosebud/" + filename, 'r', encoding="UTF-8")
    # If neither works, the file is not found.
    except FileNotFoundError:
        print("No such file could be found at " + filename
              +". Please double check the path and attempt again.")
        return None


def generate_winners_list(file) -> dict:
    '''
    Generates a dictionary of the winners of the Rose Bowl
    using a file passed in. The file is assumed to be in read only
    mode, and to have the reader pointer at the beginning of the file.
    It iterates through the file, and increment's each team's entry
    in the dict on each read.
    \n
    Input: file - The file to be read.
    Output: A dictionary of all the winners which maps to the number of times
    they have won.
    '''
    # Generate the dictionary
    winners = {}
    # Iterate through the file
    for line in file.readlines():
        # Cut the newline character
        if "\n" in line:
            line = line[:-1]
        # If that team is already in, add it at value 0
        if line not in winners:
            winners[line] = 0
        # Now increment it
        winners[line] = winners[line] + 1
    # Return the dictionary
    return winners


def sort_by_wins(winners: dict) -> dict:
    '''
    Sorts a provided dictionary by order of number of wins, from the most
    to the least. In the case that there are ties, it is sorted by the
    team that won a Rose Bowl first.
    \n
    Input: winners - A dictionary containing the list of winners mapped
    to how many times they've won.
    Output: A sorted dictionary object.
    '''
    sorted_dict = dict()
    # Get the highest number of wins
    most_wins = 0
    # Iterate through the winners
    for team in winners:
        # If a new best is found, store it
        if winners[team] > most_wins:
            most_wins = winners[team]
    # Now, add to the new dictionary
    # Start at the max wins, and then go down
    for i in range(most_wins, 0, -1):
        for team in winners:
            # If this team has that many wins, add it to the new dictionary
            if winners[team] == i:
                sorted_dict[team] = i
    # Now the new dictionary is sorted, return it
    return sorted_dict


def four_plus(teams: dict) -> None:
    '''
    Outputs the list of teams which have won the rose bowl four
    or more times. To help with this, it assumes the dictionary
    not sorted, and sorts it using the sort_by_wins function.
    It them iterates through the dictionary until a non-four
    winning team is found, and exits.
    \n
    Input: teams - An unsorted dictionary containing all teams that
    have won mapped to the number of times they've won.
    '''
    # Initial output
    print("Teams which have won four or more times: ")
    # Sort the dictionary
    sorted_teams = sort_by_wins(teams)
    # Iterate through the list
    for team in sorted_teams.items():
        if team[1] > 3:
            # Cut the newline character from the end
            print(str(team[0]) + " has won " + str(team[1]) + " times.")
        else:
            return None


def n_plus(teams: dict, num_wins: int) -> None:
    '''
    Outputs the list of teams which have won the rose bowl n
    or more times. To help with this, it assumes the dictionary
    not sorted, and sorts it using the sort_by_wins function.
    It them iterates through the dictionary until a lower number
    of wins team is found, and exits.
    This function has a special case where n is 0, whereupon it
    outputs all teams, sorted by wins.
    \n
    Input: teams - An unsorted dictionary containing all teams that
    have won mapped to the number of times they've won.
    Input: n - The number of wins above which to display teams.
    '''
    # Initial output - check to see what the bar is
    if num_wins < 1:
        # Output all teams
        print("All teams which have won the Rose Bowl:")
    else:
        print("Teams which have won four or more times: ")
    # Sort the dictionary
    sorted_teams = sort_by_wins(teams)
    # Iterate through the list
    for team in sorted_teams.items():
        if team[1] > num_wins - 1:
            # Cut the newline character from the end
            print(str(team[0]) + " has won " + str(team[1]) + " times.")
        else:
            return None


# Do some test outputs
# This is essentially the main function
# Generate the text file
f = attempt_get_file("RoseBowl.txt")
# Make sure the file was generated sucessfully
if f is not None:
    # Generate the winners
    d = generate_winners_list(f)
    # Output all four time winners
    four_plus(d)
    # Clear lines between outputs
    print()
    # Show that the n_times function works
    n_plus(d, 4)
    print()
    # Output all winners
    n_plus(d, 0)


#
# Thoughts:
# Firstly, I mainly regret that Python has no hashmaps. This program
# was made using dictionaries instead of hashmaps, and some features
# of hashmaps would have been incredibly helpful in this program.
# Additionally, the sort_by_wins function (as part of the creative element)
# could have likely been more effecient. Currently, I am utilizing
# (essentially) insertion sort, while bubble or merge would in theory
# be better. However, these are more difficult to implement when
# the indeces are names, instead of integers of increasing value.
# In theory, it would be possible to have an array of teams and their
# corresponding indeces, but that would likely be more complicated
# and end up taking longer/being less effecient than pure insertion
# as I implemented.
#
