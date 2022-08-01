"""
Mocked design for project.
"""
import time
import random

HORIZONTAL_LINE: str = "-" * 80  # constant for horizontal line



def replay_game():
    while True:
        play_again = input("(yes/no)\n").lower().strip()
        if play_again == "yes":
            return True
        elif play_again == "no":
            return False
        else:
            print("Please enter a valid answer.")


def answer_logic(correct_answer):
    user_answer = input("Your answer: ").lower().strip()  # ask the user for their answer
    if user_answer in correct_answer:  # if the user answer matches the one in the list
        print("Correct!")
        return True
    else:
        print("Wrong answer! The correct answer was", ", ".join(correct_answer))  # if wrong, show the answer
        return False


def game(quiz):
    score = 0
    for question in quiz:  # for each question in the list, instead of repeating the code for each question
        print(question[0], f"\n{', '.join(question[1])}")  # print the question
        if answer_logic(question[-1]):
            score += 1  # add to the score
        print(HORIZONTAL_LINE)
    print("Quiz complete!\nYour score was", score, "out of", len(quiz))  # print score out of total


def load_questions_from_file(file_name):
    """
    Load questions from a file.
    """
    with open(file_name, 'r', encoding = "utf8") as file:
        for line in file:
            entry = line.split(' ! ')
            if entry[-1].endswith('\n'):
                entry[-1] = entry[-1][:-1]
            if entry[-1].endswith('\r'):
                entry[-1] = entry[-1][:-1]
            options = entry[1].split(", ")
            answers = entry[2].split(", ")
            try:
                elements.append([entry[0], options, answers])
            except (NameError, UnboundLocalError):
                elements: list = [[entry[0], options, answers]]
    return elements


def list_shuffler(list_to_shuffle):
    """
    Randomise the questions on replay.
    """
    random.shuffle(list_to_shuffle)
    return list_to_shuffle



def main():
    """
    Main function.
    """
    quiz_questions = load_questions_from_file("questions.txt")
    playing = True
    while playing:
        print("Hey there!\n")
        name = input("What is your name?\n").capitalize()  # This to ask the end users name.
        print("Hey " + name + "!\n")  # Prints hey and the users name.
        time.sleep(1)
        print(
            "Welcome to my Zero Hunger Quiz" + " " + name + "!\n")  # Welcomes the user and prints
        # their name.
        time.sleep(1)
        game(quiz_questions)  # Starts the quiz.
        print(HORIZONTAL_LINE)
        print("Would you like to play again?\n")  # play again logic
        if replay_game():
            print("Coming right up!")
            list_shuffler(quiz_questions)
        else:
            print("Thanks for playing!")
            exit()


if __name__ == "__main__":
    main()
