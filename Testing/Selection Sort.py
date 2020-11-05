# Swapping Values
"""
my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]

print(my_list)

# temp = my_list[0]
# my_list[0] = my_list[2]
# my_list[2] = temp

my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)
"""

# Selection Sort
# (scan/select smallest element)
"""
15, 57, 14, 33, 72, 79, 26, 56, 42, 40
# Replace 15 with smallest #, 14
14, 57, 15, 33, 72, 79, 26, 56, 42, 40
#
14, 15, 57, 33, 72, 79, 26, 56, 42, 40

14, 15, 26, 33, 72, 79, 57, 56, 42, 40

14, 15, 26, 33, 72, 79, 57, 56, 42, 40

14, 15, 26, 33, 40, 79, 57, 56, 42, 72

14, 15, 26, 33, 40, 42, 57, 56, 79, 72

14, 15, 26, 33, 40, 42, 56, 57, 79, 72

14, 15, 26, 33, 40, 42, 56, 57, 72, 79 """

# Code for Selection Sort


def selection_sort(my_list):
    """ Sort a list using the selection sort """
    # Loop through the entire array
    for cur_pos in range(len(my_list)):  # 10 times looped if have 10 items
        # Find the position that has the smallest number
        # Start with the current position
        min_pos = cur_pos

        # Scan left to right (end of the list)
        for scan_pos in range(cur_pos + 1, len(my_list)):  # will loop about half times per round, n/2
            # so 5 * 10 = run 50 times, or n * (n/2)

            # Is this position smallest?
            if my_list[scan_pos] < my_list[min_pos]:

                # It is, mark this position as the smallest
                min_pos = scan_pos

        # Swap the two values
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp


my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
selection_sort(my_list)
print(my_list)
