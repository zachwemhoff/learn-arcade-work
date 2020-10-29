import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "my_dictionary"
    my_dictionary = open("dictionary.txt")

    # Create an empty list to store our names
    dictionary_list = []

    # Loop through each line in the file like a list
    for line in my_dictionary:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # Add the name to the list
        dictionary_list.append(line)

    my_dictionary.close()

    print("--- Linear Search ---")
    my_file = open("AliceInWonderLand200.txt")

    # Start a for loop to iterate through each line
    current_line = 0
    for line in my_file:
        word_list = split_line(line)
        current_line += 1
        for word in word_list:

            # --- Linear search
            key = word.upper()

            # Start at the beginning of the list
            current_word_list = 0

            # Loop until you reach the end of the list, or the value at the
            # current position is equal to the key
            while current_word_list < len(dictionary_list) and dictionary_list[current_word_list] != key:
                # Advance to the next item in the list
                current_word_list += 1
            if current_word_list == len(dictionary_list):
                print("Line", current_line, "possible misspelled word: ", word)
    my_file.close()

    # Binary Search
    print("---Binary Search")
    my_dictionary = open("dictionary.txt")

    # Create an empty list to store our names
    dictionary_list = []

    # Loop through each line in the file like a list
    for line in my_dictionary:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # Add the name to the list
        dictionary_list.append(line)

    my_dictionary.close()

    my_file = open("AliceInWonderLand200.txt")

    # Binary search code
    current_line = 0
    for line in my_file:
        word_list = split_line(line)
        current_line += 1
        for word in word_list:
            key = word.upper()
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False

            # Loop until we find the item, or our upper/lower bounds meet
            while lower_bound <= upper_bound and not found:

                # Find the middle position
                middle_pos = (lower_bound + upper_bound) // 2

                # Figure out if we:
                # move up the lower bound, or
                # move down the upper bound, or
                # we found what we are looking for
                if dictionary_list[middle_pos] < key:
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > key:
                    upper_bound = middle_pos - 1
                else:
                    found = True

            if not found:
                print("Line", current_line, "possible misspelled word:", word)
    my_file.close()


main()
