"""
Mocked design for project.
"""
import time

HORIZONTAL_LINE: str = "-" * 80  # constant for horizontal line


def main():
    """
    Main function.
    """
    playing = True
    while playing:
        score = 0
        questions = [["What is the tallest building in the world?\n"
                      "A. Sky Tower\nB. Empire State Building\nC. McDonalds\nD. Burj Khalifa", "d"],
                     ["What's 9+10?\n"
                      "A. 19\nB. 21\nC. 24\nD. 67", "a"]]
        print("Hey there!\n")
        name = input("What is your name?\n").capitalize()  # This to ask the end users name.
        print("Hey" + " " + name + "!\n")  # Prints hey and the users name.
        time.sleep(1)

        capitalized_string = name.capitalize()  # Converts first character to uppercase and others to lowercase
        print(
            "Welcome to my Zero Hunger Quiz" + " " + capitalized_string + "!\n")  # Welcomes the user and prints
        # their name.
        time.sleep(1)
        capitalized_string = name.capitalize()  # Converts first character to uppercase and others to lowercase
        print(HORIZONTAL_LINE)

        for question in questions:  # for each question in the list, instead of repeating the code for each question
            print(question[0])  # print the question
            user_answer = input("Your answer: ").lower().strip()  # ask the user for their answer
            if user_answer == question[1]:  # if the user answer matches the one in the list
                print("Correct!")
                score += 1  # add to the score
            else:
                print("Wrong answer! The correct answer was " + question[1])  # if wrong, show the answer
            print(HORIZONTAL_LINE)
        print("Your score is " + str(score) + " out of " + str(len(questions)))  # print score out of total
        print(HORIZONTAL_LINE)
        print("Would you like to play again?\n")  # play again logic
        play_again_check = True
        while play_again_check:
            play_again = input("(yes/no)\n").lower().strip()
            if play_again == "yes":
                playing = True
                play_again_check = False
            elif play_again == "no":
                playing = False
                play_again_check = False
            else:
                print("Please enter a valid answer.")


if __name__ == "__main__":
    main()
