# Recursion
"""
A child couldn't sleep, so her mother told her a story about a little frog,
  who couldn't sleep, so the frog's mother told her a story about a little bear,
    who couldn't sleep, so the bear's mother told her a story about a little weasel...
      who fell asleep.
    ...and the little bear fell asleep;
  ...and the little frog fell asleep;
...and the child fell asleep.
"""

# Functions calling other functions
"""
def f():
    g()
    print("f")

def g():
    print("g")

f()
"""

# Recursion
"""
def f():
    print("Hello")
    f()

f()
"""

# Controlling recursion levels
"""
def f(level):
    # Print the level we are at
    print("Recursion call, level", level)
    # If we haven't reached level ten...
    if level < 10:
        # Call this function again
        # and add one to the level
        f(level+1)

# Start the recursive calls at level 1
f(1)
"""

# Non-recursive factorial
# This program calculates a factorial
# WITHOUT using recursion
"""
def factorial_nonrecursive(n):
    answer = 1
    for i in range(2, n + 1):
        answer = answer * i
    return answer
"""
# Recursive factorial
# This program calculates a factorial
# Doesn't do anything by itself
# WITH recursion
"""
def factorial_recursive(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * factorial_recursive(n - 1)
"""


# Trying out recursive functions
# This program calculates a factorial
# WITHOUT using recursion
"""
def factorial_nonrecursive(n):
    answer = 1
    for i in range(2, n + 1):
        print(i, "*", answer, "=", i * answer)
        answer = answer * i
    return answer

print("I can calculate a factorial!")
user_input = input("Enter a number:")
n = int(user_input)
answer = factorial_nonrecursive(n)
print(answer)
"""

"""
# This program calculates a factorial
# WITH recursion

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        x = factorial_recursive(n - 1)
        print( n, "*", x, "=", n * x )
        return n * x

print("I can calculate a factorial!")
user_input = input("Enter a number:")
n = int(user_input)
answer = factorial_recursive(n)
print(answer)
"""

# Recursive Expressions
"""
def f(n):
    if n == 1:
        return 6
    elif n > 1:
        return (1 / 2) * f(n - 1) + 4


def main():
    result = f(10)
    print(result)


main()
"""

# Recursive Rectangles
"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500


def draw_rectangle(x, y, width, height):
    # Recursively draw a rectangle, each one a percentage smaller 

    # Draw it
    arcade.draw_rectangle_outline(x, y, width, height, arcade.color.BLACK)

    # As long as we have a width bigger than 1, recursively call this function with a smaller rectangle
    if width > 1:
        # Draw the rectangle 90% of our current size
        draw_rectangle(x, y, width * .9, height * .9)


class MyWindow(arcade.Window):
    # Main application class.

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        # Render the screen.
        arcade.start_render()

        # Find the center of our screen
        center_x = SCREEN_WIDTH / 2
        center_y = SCREEN_HEIGHT / 2

        # Start our recursive calls
        draw_rectangle(center_x, center_y, SCREEN_WIDTH, SCREEN_HEIGHT)


def main():

    MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
"""

# Recursive H's
"""
Recursive H's
"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

RECURSION_DEPTH = 0


def draw_h(x, y, width, height, count):
    """ Recursively draw an H, each one a half as big """

    # Draw the H
    # Draw cross-bar
    arcade.draw_line(x + width * .25, height / 2 + y,
                     x + width * .75, height / 2 + y, arcade.color.BLACK)
    # Draw left side
    arcade.draw_line(x + width * .25, height * .5 / 2 + y,
                     x + width * .25, height * 1.5 / 2 + y, arcade.color.BLACK)
    # Draw right side
    arcade.draw_line(x + width * .75, height * .5 / 2 + y,
                     x + width * .75, height * 1.5 / 2 + y, arcade.color.BLACK)

    # As long as we have a width bigger than 1, recursively call this function with a smaller rectangle
    if count > 0:
        count -= 1
        # Draw the rectangle 90% of our current size
        # Draw lower left
        draw_h(x, y, width / 2, height / 2, count)
        # Draw lower right
        draw_h(x + width / 2, y, width / 2, height / 2, count)
        # Draw upper left
        draw_h(x, y + height / 2, width / 2, height / 2, count)
        # Draw upper right
        draw_h(x + width / 2, y + height / 2, width / 2, height / 2, count)


class MyWindow(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        # Start our recursive calls
        draw_h(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, RECURSION_DEPTH)


def main():
    MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()