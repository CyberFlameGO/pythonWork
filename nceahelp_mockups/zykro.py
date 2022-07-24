"""
Mocked design for project.
"""
from typing import Any


class Quiz(object):
    """
    Quiz logic class.
    The quiz set MUST be a dictionary with the following structure:
    "dict[int, tuple[str, tuple[Any, ...], set[Any, ...], Any]]"
    The first element of the tuple is the question, the second is the answers, the third is the possible user inputs
    (lowercase), and the fourth is the correct answer (lowercase).
    The code does not account for floats/integers as quiz answers (without being strings), though if it does require
    those, it's easy to add a TypeError check (or just let the answers come back as strings).
    """
    def __init__(self, name, quiz_set: dict):
        self.name = name
        self.quiz_set = quiz_set
        self.score: int = 0  # Declares the score variable, set to zero

    def quiz_runner(self):
        """
        Start the quiz.
        """
        for question_number, question_data in self.quiz_set.items():
            question_check = True
            while question_check:
                print(question_data[0])
                for answer in question_data[1]:
                    print(answer)
                user_input = str(input("Your answer: ").lower().strip())
                result, code = self.answer_checking(question_number, user_input)
                if result:
                    print("Correct!")
                    self.score += 1
                    question_check = False
                else:  # A match-case would've worked better but Python 3.10 isn't widely used yet.
                    if code == 1:
                        print(f"Wrong answer! The correct answer was {question_data[3]}")
                        question_check = False
                    elif code == 2:
                        print("Wrong input, try again!")
        return self.name, self.score

    def answer_checking(self, question: int, user_input: str) -> tuple[bool, int]:
        """
        Check if the user input is correct.
        """
        if user_input in self.quiz_set[question][2]:
            if user_input == self.quiz_set[question][3]:
                return True, 0
            else:
                return False, 1
        else:
            return False, 2


def main():
    """
    Main function
    """

    # We use a dictionary here for key-value pairing of question number to question.
    questions: dict[int, tuple[str, tuple[Any, ...], set[Any, ...], Any]] = {
        1: ("What is the capital of France?",
            ("A - Paris",
             "B - Berlin",
             "C - London",
             "D - Madrid"), {"a", "b", "c", "d"}, "a"),
        2: ("The symbol for the element Gold is Au.",
            ("True", "False"),
            {"true", "false"}, "true")
    }

    print("Hey there!\n")
    quiz = Quiz(input("What is your first name?\n").strip(), questions)  # This to ask the end users name.
    print(f"Hey, {quiz.name}, welcome to my Disney/Pixar themed Quiz!")  # Welcomes the user and prints their
    # name.
    print("Let's start the quiz!\nHere's your first question:")  # Prints a message to the user.
    player_name, player_score = quiz.quiz_runner()  # Starts the quiz.
    print(f"{player_name}, you scored {player_score} out of {len(questions)}!")  # Prints the user's score.


if __name__ == "__main__":
    main()
