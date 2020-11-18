# Exceptions
# Exception Handling
# Divide by zero
"""
try:
    x = 5 / 0
except:
    print("Error dividing by zero")
"""

# Handling number conversion errors
# Invalid number conversion
"""
try:
    x = int("fred")
except:
    print("Error converting fred to a number")
"""

# Better handling of number conversion errors
"""
number_entered = False
while not number_entered:
    number_string = input("Enter an integer: ")
    try:
        n = int(number_string)
        number_entered = True
    except:
        print("Error, invalid integer")
"""

# Checking for an error when opening a file
# Error opening file
"""
try:
    my_file = open("myfile.txt")
except:
    print("Error opening file")
"""

# Handling different types of errors
# Multiple errors
"""
try:
    # Open the file
    filename = "myfile.txt"
    my_file = open(filename)

    # Read from the file and strip any trailing line feeds
    my_line = my_file.readline()
    my_line = my_line.strip()

    # Convert to a number
    my_int = int(my_line)

    # Do a calculation
    my_calculated_value = 101 / my_int

except FileNotFoundError:
    print(f"Could not find the file '{filename}'.")
except IOError:
    print(f"Input/Output error when accessing the file '{filename}'.")
except ValueError:
    print("Could not convert data to an integer.")
except ZeroDivisionError:
    print("Division by zero error.")
except:
    print("Unexpected error.")
"""

# Creating an exception
"""
try:
    x = 5 / 0
except ZeroDivisionError as e:
    print(e)
"""
# Generating exceptions
def get_input():
    user_input = input("Enter something: ")
    if len(user_input) == 0:
        raise IOError("User entered nothing")

get_input()
