""" BMX program """
# Luke Dempsey
# September 2022
# Version 1 - input, calculation and output working
# Version 2 - adding functions and a mainloop
# Version 3 - adding a search, invalid entries -  no try and except
# Version 4 - invalid entries, with try and except
# Version 5 - sorting the outputs in order of highest to lowest tallied points
# Version 6 - removing reduntant code, cleaning up outputs
#           - general refactoring


# Setting the amount of riders in a team- currently 6
NUM_RIDERS = 3

# Setting the amount of races- currently 4
NUM_RACES = 3


def input_func():
    """ "
    Function for the input
    then adding the input into the dictionary
    """

    # Declaring riders dictionary an empty dictionary
    rider_dict = {}

    print("\nTEAM INPUT")
    for rider in range(NUM_RIDERS):
        # Declaring placing list as an empty list
        placing = []
        print(f"\nRIDER {rider + 1}")
        while True:
            name = input("Name: ").lower().strip()
            if not name:
                print("Please enter your name")
            else:
                break
        print("\nPLACINGS")
        print("If you did not race enter 0")

        for race in range(NUM_RACES):
            while True:
                try:
                    place = int(input(f"Race {race + 1}: "))
                    if place < 0 or place > 50:
                        print("Please enter a number between 0 and 50")
                    else:
                        if place == 0:
                            place = "N/A"
                        placing.append(place)
                        rider_dict[name] = placing
                        break
                except ValueError:
                    print("Please enter a number")
    return rider_dict


def points_calc(rider_dict):
    """Function to calculate riders total points"""

    for rider in rider_dict:
        total = sum(
            7 - (2 * place) for place in rider_dict[rider] if place in range(1, 4)
        )
        rider_dict[rider].append(total)


def output_func(rider_dict):
    """ "Function to sort and print the outputs"""

    # Putting the values and keys into tuples in a list
    dict_items = list(rider_dict.items())

    # Sorting the tuples by the riders total points - last index position
    for i in range(len(dict_items)):
        for j in range(i + 1, len(dict_items)):
            if dict_items[i][1][-1] < dict_items[j][1][-1]:
                dict_items[i], dict_items[j] = dict_items[j], dict_items[i]

    # Output
    print("\n\nTEAM RESULTS:")
    for rider in dict_items:
        print(f"\n{rider[0].title()}'s results:")
        print("Placings:")
        for race in range(NUM_RACES):
            print(f"Race {race + 1}: {rider[1][race]}")
        print(f"Tally for {NUM_RACES} races: {rider[1][-1]} points")
    print("\n")


def search_func(rider_dict):
    """ "Searching for a rider function"""

    while True:
        search_option = (
                input("Do you want to search for a rider? (Y or N): ").upper().strip() + " "
        )

        if search_option[0] not in ["Y", "N"]:
            print("Please enter Y or N")
        elif search_option[0] == "N":
            break
        else:
            search_name = input("Enter name of rider: ").lower().strip()

            if search_name not in rider_dict:
                print("Your name was not in our list.")
            else:
                # Printing output for searched rider
                print(f"\n{search_name.title()}'s Results:")
                print("Placings:")
                for race in range(NUM_RACES):
                    print(f"Race {race + 1}: {rider_dict[search_name][race]}")
                print(
                    f"Tally for {NUM_RACES} races: {rider_dict[search_name][-1]} points\n"
                )


def loop_prog():
    """ "Function to ask if user wants to repeat the program"""

    while True:
        choice = (
                input("Do you want to input another team? (Y or N): ").upper().strip() + " "
        )

        if choice[0] == "Y":
            return True
        if choice[0] == "N":
            return False
        print("Please enter Y or N")


def main():
    """ "Running all the functions"""

    repeat_program = True
    while repeat_program:
        rider_dict = input_func()
        points_calc(rider_dict)
        output_func(rider_dict)
        search_func(rider_dict)
        repeat_program = loop_prog()


if __name__ == "__main__":
    main()
