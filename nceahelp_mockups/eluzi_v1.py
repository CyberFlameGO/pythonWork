import random
import sqlite3
import time  # Import for time when using time.sleep

DB_FILE: str = r"questions.db"

c = []  # List to used for the question file split
valid = ["A", "B", "C", "D", "a", "b", "c", "d"]  # List of answers the user can enter


class Database(object):
    """
    Database class for SQLite3.
    """

    def __init__(self, db_name: str, query_file: str = r"query.sql") -> None:
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
            self.cursor.execute(
                '''CREATE TABLE IF NOT EXISTS Questions (
                'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                'question' TEXT NOT NULL, 
                'a' TEXT NOT NULL,
                'b' TEXT NOT NULL,
                'c' TEXT NOT NULL,
                'd' TEXT NOT NULL,
                'answer' TEXT NOT NULL 
                );
            '''
            )
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


def intro():
    """
    This function is used to introduce the user to the game
    :return:
    """
    print("====****Introduction****=======")
    print("Hey there!\n")
    name: str = input(
        "Please enter a name with no more than 10 characters to continue: ").strip()
    while len(name) < 1 or len(
            name) > 10:  # Asks the user for their name and limits inputs to no less than 1 and no more than 10
        name = input(
            "\nUnfortunately, you've entered a name too long (or not entered a name) for this program to read.\nPlease "
            "enter a name with no more than 10 characters to continue: ").strip()  # This
        # will ask for the end
        # users name
    print("Hey,", name + "!")
    print("Welcome to my Lack of Education Quiz" + "\n")  # Welcoming the end user, and intoduction to the quiz and
    # gives the user a rundown of the quiz
    time.sleep(1)  # Stops time for 1 second
    print("In this quiz you will be quizzed on 20 random questions about education around the world")
    time.sleep(1)
    print("You will receive your results and final score at the end.")
    time.sleep(1)
    print("Enjoy the quiz!")
    print()
    return name  # Returns name


def questions(player_name):  # Definition for main part of code which is the questions
    count = 1  # Variables for count, score, and retry
    score = 0
    for key, value in question_dic.items():  # prints the questions out to the user and asks for an input
        print(count, ".", key)
        for items in range(4):
            print(value[items])
        count += 1
        ans = ""  # Variable for answer
        while ans not in valid:  # checks if the answer is valid
            ans = input("-----Please enter A, B, C, D to answer-----\nWhat is your answer? ")
            print("")
        if ans.upper() == value[4] or value[5]:  # checks if the answer is correct and prints this statement
            print("Congrats, you are correct!")
            score += 1
            print("Your score is", score)
            print("")
        else:  # checks if the answer is incorrect and prints this statement
            print("Sorry, your answer was incorrect!")
            print("Your score is", score)
            print("")
    print("Congrats,", player_name, "you completed the Education quiz!")  # Prints if user gets 5 or bellow
    print("You got a score of", score, "/ 15")
    if score <= 5:  # The program determines how well the user did and prints their name and score out to them
        print("Better luck next time!")
    elif score <= 10:
        print("Good job you did well!")
    elif score < 15:
        print("Great work you actually did really well!")
    elif score == 15:
        print("You got a perfect score!\nExcellent work!")
    print("")

    play_again_check = input("Would you like to retry the quiz? (YES/NO) ")
    while play_again_check != "yes" or play_again_check != "no":  # Asks the user if they want to try again
        play_again_check = input(
            "Sorry, your input was not recognised. Please enter either 'yes' or 'no'.\nWould you like to try the quiz "
            "again to get a better score?\nPlease enter 'yes' or 'no' here: ").lower().strip()  #
        # Input
        # for retry
        print("")
    return score, play_again_check  # Returns score and retry


def writing_to_file(a, b):  # definition used to write back the data to the file for the users final score
    with open('Score.txt', 'a') as writing:
        writing.write(a + ":" + str(b) + "\n")


def main():  # Definition for the main part of the code
    db = Database(DB_FILE)  # Initializes the database


    quiz_data = db.read_db("SELECT question, a, b, c, d, answer FROM Questions")  # Reads the database


    with open('realques.txt') as f:  # Splits the question file into the separate questions in a dictionary
        lines = list(f)
        while len(question_dic) < 15:  # This part of code splits the question file into parts so it can ask the
            # user the questions
            question = random.choice(lines).strip()
            a, b = question.split(";")
            c = b.split("|")
            question_dic[a] = c

    final_score = 0  # Variable for users final score
    player = intro()  # runs intro def and returns name
    score, retry = questions(player)  # runs questions def and returns score and retry
    final_score += score  # adds the score to the final score

    if retry == "no":  # If the user does not want to retry the quiz it ends the quiz
        writing_to_file(player, final_score)  # Runs the definition for write to file
        print(f"Congrats, {player}, your final score was {final_score}!")  # Final statement
        print("Thanks for playing the Education quiz")
        print("Goodbye...")
        exit()


if __name__ == "__main__":  # Uses main function to run the entire program
    main()
