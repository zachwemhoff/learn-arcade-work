import random


def selection_sort(my_list):
    """ Sort a list using the selection sort """

    # Loop through the entire array
    # Count how many times looped
    outside_loop_count = 0
    inside_loop_count = 0
    for cur_pos in range(len(my_list)):
        # Find the position that has the smallest number
        # Start with the current position
        min_pos = cur_pos
        outside_loop_count += 1

        # Scan left to right (end of the list)
        for scan_pos in range(cur_pos + 1, len(my_list)):
            inside_loop_count += 1

            # Is this position smallest?
            if my_list[scan_pos] < my_list[min_pos]:
                # It is, mark this position as the smallest
                min_pos = scan_pos

        # Swap the two values
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp
    print("Outside loop of selection sort count: ", outside_loop_count)
    print("Inside loop of selection sort count: ", inside_loop_count)


def insertion_sort(my_list):
    """ Sort a list using the insertion sort """
    # Count the number of times looped
    outside_loop_count = 0
    inside_loop_count = 0
    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    for key_pos in range(1, len(my_list)):

        # Get the value of the element to insert
        key_value = my_list[key_pos]

        # Scan from right to the left (start of list)
        scan_pos = key_pos - 1
        outside_loop_count += 1
        # Loop each element, moving them up until
        # we reach the position the
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1
            inside_loop_count += 1

        # Everything's been moved out of the way, insert
        # the key into the correct location
        my_list[scan_pos + 1] = key_value

    # Print number of times looped
    print("Outside loop of insertion sort count: ", outside_loop_count)
    print("Inside loop of insertion sort count: ", inside_loop_count)


# This will point out a list
# For more information on the print formatting {:3}
# see the chapter on print formatting.
def print_list(my_list):
    for item in my_list:
        print(f"{item:3}", end="")
    print()


def main():
    # Create two lists of the same random numbers
    list_for_selection_sort = []
    list_for_insertion_sort = []
    list_size = 100
    for i in range(list_size):
        new_number = random.randrange(100)
        list_for_selection_sort.append(new_number)
        list_for_insertion_sort.append(new_number)

        # Print the original list
    print("Original List")
    print_list(list_for_selection_sort)

    # Use the selection sort and print the result
    print()
    print("Selection Sort")
    selection_sort(list_for_selection_sort)

    # Use the insertion sort and print the result
    print()
    print("Insertion Sort")
    insertion_sort(list_for_insertion_sort)


main()
