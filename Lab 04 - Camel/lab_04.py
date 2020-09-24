import random


def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi dessert.")
    print("The natives want their camel back and are chasing you down! Survive your\ndesert trek and out run the natives.")

    print()

    # Variables
    done = False
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_traveled = -20
    drinks_in_canteen = 3
    oasis = -1

    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")

        user_choice = input("What is your choice? ")
        print()

        # If the user wants to quit
        if user_choice.upper() == "Q":
            print("You quit the game.")
            done = True

        # Status Check
        elif user_choice.upper() == "E":
            print("Miles traveled:", miles_traveled)
            print("Drinks in canteen:", drinks_in_canteen)
            print("The natives are", miles_traveled - natives_traveled, "miles behind you.")
            print()

        # Stop for the night
        elif user_choice.upper() == "D":
            print("You stop for the night.")
            print("The camel is happy.")
            camel_tiredness = 0
            natives_traveled += random.randrange(7, 16)
            print("The natives are", miles_traveled - natives_traveled, "miles behind you.")
            print()

        # Full Speed Ahead
        elif user_choice.upper() == "C":
            miles = random.randrange(10, 19)
            miles_traveled += miles
            thirst += 1
            camel_tiredness += random.randrange(1, 4)
            natives_traveled += random.randrange(7, 16)
            if oasis == 10:
                print("You found an oasis!")
                drinks_in_canteen = 3
                thirst = 0
                camel_tiredness = 0
            else:
                print("You traveled:", miles, "miles")
                print()

        # Moderate speed ahead
        elif user_choice.upper() == "B":
            miles = random.randrange(5, 12)
            miles_traveled += miles
            thirst += 1
            camel_tiredness += 1
            natives_traveled += random.randrange(7, 16)
            if oasis == 10:
                print("You found an oasis!")
                drinks_in_canteen = 3
                thirst = 0
                camel_tiredness = 0
            else:
                print("You traveled", miles, "miles.")
                print()

        # Drink from your canteen
        elif user_choice.upper() == "A":
            if drinks_in_canteen > 0:
                drinks_in_canteen -= 1
                thirst = 0
                print("You take a drink from your canteen")
                print("You have", drinks_in_canteen, "drinks left.")
                print()
            else:
                print("Your canteen is empty. You have no drinks left.")

        # Status updates/calculations

        # Win
        if miles_traveled >= 200:
            print("You have traveled the entire desert.")
            print("You won!")
            print()
            done = True

        # Thirst
        if thirst > 6:
            print("You died of thirst!")
            print("Game over.")
            print()
            done = True
        elif not done and thirst > 4:
            print("You are thirsty.")
            print()

        # Camel tiredness
        if camel_tiredness > 8:
            print("Your camel died of exhaustion.")
            print("The natives catch up to you and kill you.")
            print("Game over.")
            print()
            done = True
        elif not done and camel_tiredness > 5:
            print("Your camel is getting tired.")
            print()

        # Natives proximity to player
        if miles_traveled - natives_traveled <= 0:
            print("The natives have caught up to you!")
            print("They kill you and take back their camel.")
            print("Game over.")
            print()
            done = True
        elif not done and miles_traveled - natives_traveled < 15:
            print("The natives are getting close!")
            print()


main()