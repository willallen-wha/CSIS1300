'''
This program draws an american flag, utilizing the standard convention that it should
be 1.9 times as long as it is tall. The union dimensions are 7/13 of the height and 2/5
of the width. From this, only a height is required to construct the entire flag, which
is set by default to be 500 pixels wide.

CREATIVE ELEMENT: I decided to implement each individual component of the flag
(a single star, the star groups, a filled and unfilled rectangle, the stripes, etc.)
in their own function on their own. This made drawing the flag incredibly easy, as it
was a simple call to the subsequent functions.
'''

from turtle import Turtle
import time

# We have to define turtle up here to avoid a bunch of pylint errors
turtle = Turtle()


def draw_rect_no_fill(x: int, y: int, height: int, width: int, color="black") -> None:
    '''
    Draws a rectangle of the given height and width at the given x and y
    coordinate. Color may optionally be passed, otherwise, the pencil defaults
    to black.
    \n
    Input: x - The x coordinate for the rectanlge to start at as int
    Input: y - The y coordinate for the rectangle to start at as int
    Input: height - The height of the rectangle as an int
    Input: width - The width of the rectangle as an int
    Input: color - A string representing the color to draw
    '''
    # Begin with the tail up
    turtle.up()
    # Move to the x and y coordinate
    turtle.setx(x)
    turtle.sety(y)
    turtle.seth(0)
    # Begin the draw and fill
    turtle.pencolor(color)
    # Draw the rectangle
    turtle.down()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    # Lift the pen again
    turtle.up()


def draw_rect(x: int, y: int, height: int, width: int, color="black") -> None:
    '''
    Draws a rectangle of the given height and width at the given x and y
    coordinate. Color may optionally be passed, otherwise, the color fill
    defaults to black.
    \n
    Input: x - The x coordinate for the rectanlge to start at as int
    Input: y - The y coordinate for the rectangle to start at as int
    Input: height - The height of the rectangle as an int
    Input: width - The width of the rectangle as an int
    Input: color - The color to fill the rectangle
    '''
    # Begin with the tail up
    turtle.up()
    # Move to the x and y coordinate
    turtle.setx(x)
    turtle.sety(y)
    # Set the fill color
    turtle.fillcolor(color)
    turtle.begin_fill()
    # Call the no_fill method
    draw_rect_no_fill(x, y, height, width, color)
    # End the fill
    turtle.end_fill()


def draw_star(x: int, y: int, rad: int, color="black") -> None:
    '''
    Draws a star with side lengths of len with top left corner at (x, y)
    \n
    Input: x - An int representing the x coordinate of the star's top-left point
    Input: y - An int representing the y coordinate of the star's top-left point
    Input: len - The length of the star's sides
    Input: Color - an optional string with the color for the star to be
    '''
    # Begin with the tail up
    turtle.up()
    # Move to the x and y coordinate
    turtle.setx(x)
    turtle.sety(y)
    turtle.seth(0)
    # Begin the fill
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.down()
    # Loop to fill
    for i in range(5):
        turtle.forward(rad)
        turtle.right(144)
        # This line is necessary to avoid a pylint error
        i = i * 1
    # Finalize the item
    turtle.end_fill()
    turtle.up()


def draw_union(x: int, y: int, height: int = 360 * 7 / 13, width=360 * 1.9 * 2 / 5) -> None:
    '''
    Draws a union with top left location at (x, y), using height
    defaulting to 713, maintaining a ratio of 1:1.9
    \n
    Input: x - An int representing the union's top left corner's x coordinate
    Input: y - An int representing the unino's top left corner's y coordinate
    '''
    # Calculate the rows and columns
    cols = 12
    rows = 10
    col_size = width / cols
    row_size = height / rows
    # Draw the rectangle for the union
    draw_rect(x, y, height, width, "blue")
    # Draw the stars
    start_x = x + col_size / 2
    start_y = y - row_size * 3 / 4
    for i in range(6):
        for j in range(5):
            draw_star(start_x + 2 * i * col_size,
                      start_y - j * 2 * row_size,
                      height / 8.74, "white")
    # Now do the offset grid
    start_x += col_size
    start_y -= row_size
    for i in range(5):
        for j in range(4):
            draw_star(start_x + 2 * i * col_size,
                      start_y - j * 2 * row_size,
                      height / 8.74, "white")


def draw_stripes(x: int, y: int, height=360) -> None:
    '''
    Draws the stripes of the american flag with the top left located at (x, y),
    with provided height or a defualt height of 360.
    \n
    Input: x - An int representing the flag's top left corner's X coordinate
    Input: y - An int representing the flag's top left conrer's Y coordinate.
    '''
    # Get the desired width
    width = height * 1.9
    bar_height = height / 13
    # Draw rectangles of alternating colors
    for i in range(7):
        draw_rect(x, y - bar_height * 2 * i, bar_height, width, "red")


def draw_flag(x: int, y: int, height=360) -> None:
    '''
    Draws a flag at given (x, y) coordinate. Defaults to height of 360 pixels,
    but other non-standard heights may be set.
    \n
    Input: x - The x coordinate of the top left of the flag, an int.
    Input: y - The y coordinate of the top left of the flag, an int.
    Input: height - The height of the flag, an optional int.
    '''
    # Outline the flag
    draw_rect_no_fill(x, y, height, height * 1.9)
    # Draw the flag's stripes
    draw_stripes(x, y, height)
    # Draw the union
    draw_union(x, y, height * 7 / 13, height * 1.9 * 2 / 5)


# Make the turtle faster
turtle.speed(0)
# Create the turtle screen
draw_flag(-350, 300)
# Hide the turtle and admire for 10 seconds
turtle.hideturtle()
time.sleep(10)

# THOUGHTS:
# Overall, this project was a fun recap of Turtles. In a
# previous class, I had worked with turtles before. In that
# class, the turtle shapes were already defined, so recreating
# them function by function was fun. I very much appreciated that
# my creative element was putting each shape into its own function.
# I misunderstood the assignment initially, as I didn't realize that
# 25 w and 713 h meant that the union should be 2/5 of the width,
# and 7/13 of the height. However, since the union recieved its own
# function which sets most of the coordinates dynamically, it was an
# incredibly quick update of only two lines of code. I also recieve a pylint
# error suggesting that x and y do not conform to snake_case naming style,
# but renaming them to something like x_coord or y_coord would decrease
# readability, so I elected to keep them like that with the pylint error.
