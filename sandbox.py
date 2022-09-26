# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
import sqlite3


class Database(object):
    """
    Database class for SQLite3.
    TODO: Potentially make a variable for table creation query
    """

    def __init__(self, db_name: str) -> None:
        """
        Database initialization logic
        :param db_name:
        """
        try:
            # Initialize the database (if it doesn't exist, a new file is created)
            self.connection = sqlite3.connect(db_name)
            # Set the cursor variable
            self.cursor = self.connection.cursor()
            # create a db table if it doesn't exist.
            # I'm aware that the autoincrement is redundant, as with having an 'id' column at all as
            # there's a built-in rowid which the id column just aliases to (unless using 'WITHOUT ROWID', which i'm not
            # doing right now as it's not worth the effort), but I've set it up this way on purpose.
            # Switching to no rowid is something I may do if I ever come back to working on this after submitting it.
            # todo: when i update these comments for this project, explain why i'm using real as opposed to
            #  double/float (the reason is that i don't need double precision decimals)
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS quiz (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    username TEXT NOT NULL,
                    score REAL NOT NULL,
                    attempt_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP UNIQUE NOT NULL 
                );""")
        except sqlite3.Error as e:
            print(e)

    def read_db(self, query, params: tuple = (None,)) -> tuple:
        """
        Runs a query then fetches and returns output of the query.
        :param query:
        :param params:
        :return:
        """
        if params[0] is None and len(params) == 1:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        return tuple(self.cursor.fetchall())

    def insert_row(self, name, score_percent: float):
        """
        Inserts a new row for an attempt
        :param length:
        """
        self.cursor.execute("INSERT INTO quiz (username, score) VALUES (?,?);", (name, score_percent))
        self.connection.commit()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# QuizBot Version 3
# Multi Choice with percentage score, while loops, play_again feautre, tells user the answer to a question if they
# got incorrect + others
# Mahdi Mousavi 29/07/2022
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Function 1, main function to carry out the quiz
def main_quiz():
    question_number = 1
    user_correct_guesses = 0
    inputs = []
    line()
    user_name = input("enter a name: ")
    for question in multi_choice_questions:
        line()
        print(question)
        for answer in ques_answers[question_number - 1]:
            print(answer)
        input_checking = True
        while input_checking:
            choices = input("Please type (A, B, C, D) ")
            choices = choices.upper()
            if choices in ['A', 'B', 'C', 'D']:
                input_checking = False
            else:
                print("Invalid input!")
        inputs.append(choices)
        user_correct_guesses += check_answer(multi_choice_questions.get(question), choices)
        question_number += 1
    db = Database("quiz.db")
    db.insert_row(user_name, ((user_correct_guesses / len(multi_choice_questions)) * 100))
    db.connection.close()
    user_score(user_correct_guesses, inputs)

def leaderboard():
    db = Database("quiz.db")
    print("leaderboard")
    for row in db.read_db("SELECT username, score, attempt_timestamp FROM quiz ORDER BY score;"):
        print(row)
    db.connection.close()

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Function 2, responds with correct or incorrect depending on the input the user enters
def check_answer(answer, choices):
    if answer == choices:
        print("That's Correct!")
        return 1
    else:
        print(f"That's Incorrect, the correct answer is: {answer}")
        return 0


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Function 3, display's the users score in a percentage, and what their inputs were
def user_score(user_correct_guesses, inputs):
    line()
    print("Your Results!")
    print("what your inputs were: ", end = "")
    for answer in inputs:
        print(answer, end = " ")
    print()

    score = int((user_correct_guesses / len(multi_choice_questions)) * 100)
    print("your score is: " + str(score) + "%")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def menu():
    input_check = True
    while input_check:
        user_menu = input("1. View Leaderboard, 2. Play Again, 3. End")
        user_menu = user_menu.strip().lower()
        if user_menu in ["1", "2", "3"]:
            input_check = False
        else:
            print('Invalid input!')
    if user_menu == "1":
        leaderboard()
    if user_menu == "2":
        return True
    if user_menu == "3":
        print("Thank you for playing all versions of the QuizBot! Hope you enjoyed our current version!")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Function 5, Add's '━━━━' after each question for an aesthetic appeal
def line():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A dictionary of questions that'll be asked to the user
multi_choice_questions = {

    "What is the name of the tallest mountain in the world:": "A",
    "Which country has the largest population in the world: ": "B",
    "What is the name of the longest river in Africa: ": "C",
    "What U.S. state is home to no documented poisonous snakes: ": "B",
    "What American city is the Golden Gate Bridge located in: ": "D",
    "What is the name of the largest country in the world": "C",
    "Which continent is Cambodia located in": "D",
    "In what ocean is the Bermuda Triangle located:": "A",
    "What is the name of the smallest US state:": "C",
}
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A list that'd be presented to the user, they would need to pick one to resume the code
ques_answers = [["A. Mount Everest", "B. Kangchenjunga", "C. Godwin Austen", "D. Lhotse"],
                ["A. India", "B. China", "C. United States", "D. Indonesia"],
                ["A. Congo ", "B. Zambezi", "C. The Nile River", "D. Kasai"],
                ["A. Texas", "B. Alaska", "C. Ohio", "D. Iowa"],
                ["A. Washington", "B. New York", "C. Illinois", "D. San Francisco"],
                ["A. New Zealand", "B. America", "C. Russia", "D. China"],
                ["A. Africa", "B. South America", "C. North America", "D. Asia"],
                ["A. Atlantic Ocean", "B. Pacific Ocean", "C. Indian Ocean", "D. Arctic Ocean"],
                ["A. Hawaii", "B. Delaware", "C. Rhode Island", "D. New Jersey"]]
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Function 1 allows the code to be carried out and once at the end of the game, function 4 goes into effect,
# this'll allow the user to either quit the code or play again, if no, function 6 prints out farewell message,
# if yes while loop carries out function 1
main_quiz()
while menu():
    main_quiz()
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
