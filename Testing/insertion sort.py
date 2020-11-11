# Insertion Sort
"""
15, 57, 14, 33, 72, 79, 26, 56, 42, 40
# Look at 15 and 57, first two, they are in correct position
15, 57, 14, 33, 72, 79, 26, 56, 42, 40
# 14, third number, slides to front, rest fall into place
14, 15, 57, 33, 72, 79, 26, 56, 42, 40
# fourth number, 33 and so on
14, 15, 33, 57, 72, 79, 26, 56, 42, 40
14, 15, 33, 57, 72, 79, 26, 56, 42, 40
# 26 slides up
14, 15, 26, 33, 57, 72, 79, 56, 42, 40
14, 15, 26, 33, 56, 57, 72, 79, 42, 40
14, 15, 26, 33, 42, 56, 57, 72, 79, 40
14, 15, 26, 33, 40, 42, 56, 57, 72, 79

"""

# Code for Insertion Sort
def insertion_sort(my_list):
    """ Sort a list using the insertion sort """

    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    for key_pos in range(1, len(my_list)):  # n

        # Get the value of the element to insert
        key_value = my_list[key_pos]

        # Scan from right to the left (start of list)
        scan_pos = key_pos - 1

        # Loop each element, moving them up until
        # we reach the position the
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):  # n/4, total of n squared / 4
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1

        # Everything's been moved out of the way, insert
        # the key into the correct location
        my_list[scan_pos + 1] = key_value


my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
insertion_sort(my_list)
print(my_list)
