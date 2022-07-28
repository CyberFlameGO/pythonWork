"""
Mocked design for project.
"""
import time

HORIZONTAL_LINE: str = "-" * 80  # constant for horizontal line


def play_again_checking():
    while play_again:
        play_again = input("(yes/no)\n").lower().strip()
        if play_again == "yes":
            playing = True
            play_again = False
        elif play_again == "no":
            playing = False
            play_again = False
        else:
            print("Please enter a valid answer.")


def replay_game():
    while True:
        play_again = input("(yes/no)\n").lower().strip()
        if play_again == "yes":
            return True
        elif play_again == "no":
            return False
        else:
            print("Please enter a valid answer.")


def game(quiz):
    score = 0
    for question in quiz:  # for each question in the list, instead of repeating the code for each question
        print(question[0])  # print the question
        user_answer = input("Your answer: ").lower().strip()  # ask the user for their answer
        if user_answer == question[1]:  # if the user answer matches the one in the list
            print("Correct!")
            score += 1  # add to the score
        else:
            print("Wrong answer! The correct answer was " + question[1])  # if wrong, show the answer
        print(HORIZONTAL_LINE)
    print("Quiz complete!\nYour score was", score, "out of", len(quiz))  # print score out of total


def load_questions_from_file(file_name):
    """
    Load questions from a file.
    """
    with open(file_name, "r") as file:
        questions = file.readlines()
    print(questions)

load_questions_from_file("questions.txt")

def main():
    """
    Main function.
    """
    playing = True
    while playing:
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
        print("Would you like to play again?\n")  # play again logic
        replay_game()


if __name__ == "__main__":
    main()
