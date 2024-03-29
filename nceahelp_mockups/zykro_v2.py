"""
Mocked design for project.
"""
from typing import Any


def quiz_runner(quiz_set: dict) -> int:
    """
    Start the quiz.
    The quiz set MUST be a dictionary with the following structure:
    "dict[int, tuple[str, tuple[Any, ...], set[Any, ...], Any]]"
    The first element of the tuple is the question, the second is the answers, the third is the possible user inputs
    (lowercase), and the fourth is the correct answer (lowercase).
    The code does not account for floats/integers as quiz answers (without being strings), though if it does require
    those, it's easy to add a TypeError check (or just let the answers come back as strings).
    :param quiz_set:
    :rtype: int
    :return
    """
    score: int = 0
    for question_number, question_data in quiz_set.items():
        question_check: bool = True
        while question_check:
            print(question_data[0])
            for option in question_data[1]:
                print(option)
            user_input = str(input("Your answer: ").lower().strip())
            result, code = answer_checking(question_number, quiz_set, user_input)
            if result:
                print("Correct!")
                score += 1
                question_check = False
            else:  # A match-case would've worked better but Python 3.10 isn't widely used yet.
                if code == 1:
                    print(f"Wrong answer! The correct answer was {question_data[3]}")
                    question_check = False
                elif code == 2:
                    print(f"Wrong input, try again entering one of {question_data[2]}")
        print("Current score:", score)
    return score


def answer_checking(question: int, quiz_set: dict, user_input: str) -> tuple[bool, int]:
    """
    Check if the user input is correct.
    """
    if user_input in quiz_set[question][2]:
        if user_input == quiz_set[question][3]:
            return True, 0
        else:
            return False, 1
    else:
        return False, 2


# noinspection DuplicatedCode
def file2dict(filename):
    """
    Reads a file and returns a dictionary with the following structure:
    Question | Possible Options (separated by commas, lowercase) | Possible Answers (separated by commas,
    lowercase) | Answer (in the possible answers section, lowercase)
    The pipes must have a space leading and trailing the pipe character, and the comma must have a trailing space.
    Example:
    What is water's molecular structure? | A. H2O, B. H, C. O, D. K | a, b, c, d | a
    :param filename:
    :return:
    """
    with open(filename, 'r', encoding = "utf8") as file:
        for line in file:
            row = line.split(' | ')
            if row[-1].endswith('\n'):
                row[-1] = row[-1][:-1]
            if row[-1].endswith('\r'):
                row[-1] = row[-1][:-1]
            separated_str_tuple = tuple(row[1].split(", "))
            separated_str_set = set(row[2].split(", "))
            try:
                processed_data[len(processed_data) + 1] = (row[0], separated_str_tuple, separated_str_set, row[3])
            except (NameError, UnboundLocalError):
                processed_data: dict[int, tuple[str, tuple[Any, ...], set[Any, ...], Any]] = {
                    1: (row[0], separated_str_tuple, separated_str_set, row[3])
                }
    print("Questions loaded successfully!")
    return processed_data


def play_again() -> bool:
    """
    Asks the user if they want to play again.
    :return:
    """
    while True:
        quiz_again = str(input("Would you like to play again? (yes/no)\n").lower().strip())
        if quiz_again == "no":
            print("Thanks for playing!")
            return False
        elif quiz_again == "yes":
            print("Let's go again!")
            return True
        else:
            print("I'm sorry, I didn't understand that. Please try again.")


# noinspection DuplicatedCode
def main():
    """
    Main function
    """
    questions: dict = file2dict("questions.txt")
    quizzing: bool = True
    while quizzing:
        player_name = str(input("What is your first name?\n").strip())
        print(f"Hey, {player_name}, welcome to my Disney/Pixar themed Quiz!")  # Welcomes the user and prints their
        # name.
        print("Let's start the quiz!\nHere's your first question:")  # Prints a message to the user.
        player_score = quiz_runner(questions)  # Starts the quiz.
        print(f"{player_name}, you scored {player_score} out of {len(questions)}!")  # Prints the user's score. If they
        # got 100% correct, printing a different message is very do-able.

        # Asks the user if they want to play again.
        if play_again():
            print("New quiz coming up!")
        else:
            quizzing = False
    exit()


if __name__ == "__main__":
    main()
