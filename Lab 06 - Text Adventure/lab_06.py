# Define the class
class Room:
    def __init__(self):
        self.description = ""
        self.north = 0
        self.east = 0
        self.south = 0
        self.west = 0


def main():
    done = False
    current_room = 0
    room_list = []

    # Foyer
    room = Room()
    room.description = "You are in a dark and spacious foyer.\nA passage leads south."
    room.north = None
    room.east = None
    room.south = 1
    room.west = None
    room_list.append(room)

    # North hallway
    room = Room()
    room.description = "You are in a candle-lit hallway.\nThe hallway continues south."
    room.north = 0
    room.east = None
    room.south = 2
    room.west = None
    room_list.append(room)

    # South hallway
    room = Room()
    room.description = "You are in the south hallway.\nThere is a bedroom to the east and a kitchen to the west.\nThere is also a staircase to your south."
    room.north = 1
    room.east = 5
    room.south = 7
    room.west = 3
    room_list.append(room)

    # Kitchen
    room = Room()
    room.description = "You are in the kitchen.\nThere is a living room to the north and a hallway to the east."
    room.north = 4
    room.east = 2
    room.south = None
    room.west = None
    room_list.append(room)

    # Living room
    room = Room()
    room.description = "You are in the living room.\nThe kitchen is to the south."
    room.north = None
    room.east = None
    room.south = 3
    room.west = None
    room_list.append(room)

    # Bedroom
    room = Room()
    room.description = "You have entered the bedroom.\nThere is a storage room to the north and a hallway to the west."
    room.north = 6
    room.east = None
    room.south = None
    room.west = 2
    room_list.append(room)

    # Storage room
    room = Room()
    room.description = "You are in the storage room.\nThere is a bedroom to the south."
    room.north = None
    room.east = None
    room.south = 5
    room.west = None
    room_list.append(room)

    # Upstairs hallway
    room = Room()
    room.description = "You have gone up the stairs and found yourself in an upstairs hallway.\nThe stairs to the north lead to the downstairs hallway.\nThere a door to the south."
    room.north = 2
    room.east = None
    room.south = 8
    room.west = None
    room_list.append(room)

    # Master bedroom
    room = Room()
    room.description = "You have entered the master bedroom.\nThe master bath is to the west.\nThere is also a game room to the east."
    room.north = 7
    room.east = 10
    room.south = None
    room.west = 9
    room_list.append(room)

    # Master bathroom
    room = Room()
    room.description = "You have entered the master bathroom. It is incredibly spacious.\nThe door that leads back to the master bedroom is to the east."
    room.north = None
    room.east = 8
    room.south = None
    room.west = None
    room_list.append(room)

    # Game room
    room = Room()
    room.description = "You have entered the game room. There is a huge projector screen and a new PS5 game console.\nThe door that leads back to the master bedroom is to the west.\nThere is also a staircase to your south."
    room.north = None
    room.east = None
    room.south = 11
    room.west = 8
    room_list.append(room)

    # Attic
    room = Room()
    room.description = "You have made your way up the second floor stairs and find yourself in an attic. It is dark and dusty.\nThe stairs to the north lead back to the game room."
    room.north = 10
    room.east = None
    room.south = None
    room.west = None
    room_list.append(room)

    while not done:
        print()
        print(room_list[current_room].description)
        user_input = input("What direction? ")

        # Move north
        if user_input.upper() == "N" or user_input.upper() == "NORTH":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # Move east
        elif user_input.upper() == "E" or user_input.upper() == "EAST":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # Move south
        elif user_input.upper() == "S" or user_input.upper() == "SOUTH":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # Move west
        elif user_input.upper() == "W" or user_input.upper() == "WEST":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # Quit the game
        elif user_input.upper() == "Q" or user_input.upper() == "QUIT":
            print()
            print("You have quit the game.")
            done = True

        # Program doesn't understand what user typed
        else:
            print()
            print("The program does not understand what you entered. Please try again.")


main()
