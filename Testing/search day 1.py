
def read_in_file(file_name):
    # --- Read in a file of names and put in a list
    name_list = []

    # Open a file for reading
    my_file = open("super_villains.txt")

    for line in my_file:
        line = line.strip()
        # print(line)
        name_list.append(line)

    my_file.close()

    return name_list


def linear_search(key, name_list):
    current_list_position = 0
    while current_list_position < len(name_list) and name_list[current_list_position] != key:
        current_list_position += 1

    return current_list_position


def main():

    name_list = read_in_file("super_villains.txt")

    # --- Search a list
    # LINEAR SEARCH
    key = "Morgiana the Shrew"
    name_list = read_in_file("super_villains.txt")
    list_position = linear_search(key, name_list)
    # Am I at the end of the list?
    # Is this item equal to the key

    if list_position < len(name_list):
        print("Found it !!!! It is in position", list_position + 1)
    else:
        print("Not in list.")


main()
