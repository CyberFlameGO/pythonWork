question_dic = {}  # Variables for main components of code
import time  # Import for time when using time.sleep
import random
from unicodedata import name  # Import for random when using random questions

c = []  # List to used for the question file split
valid = ["A", "B", "C", "D", "a", "b", "c", "d"]  # List of answers the user can enter
retry_ans = ["YES", "NO"]  # List for retry answers

with open('realques.txt') as f:  # Splits the question file into the separate questions in a dictionary
    lines = list(f)
    while len(
            question_dic) < 15:  # This part of code splits the question file into parts so it can ask the user the
        # questions
        question = random.choice(lines).strip()
        a, b = question.split(";")
        c = b.split("|")
        question_dic[a] = c


def intro():
    name = ""
    print("====****Introduction****=======")
    print("Hey there!\n")
    while len(name) < 1 or len(
            name) > 10:  # Asks the user for their name and limits inputs to no less than 1 and no more than 10
        name = input(
            "Please enter a name with no more than 10 characters to continue: ")  # This will ask for the end users name
    print("Hey!" + name + "!\n")
    print(
        "Welcome to my Lack of Education Quiz" + "\n")  # Welcoming the end user, and intoduction to the quiz and gives the user a rundown of the quiz
    time.sleep(1)  # Stops time for 1 second
    print("In this quiz you will be quizzed on 20 random questions about education around the world")
    time.sleep(1)
    print("You will receive your results and final score at the end.")
    time.sleep(1)
    print("Enjoy the quiz!")
    print("")
    return name  # Returns name


def questions(a):  # Definition for main part of code which is the questions
    count = 1  # Variables for count, score, and retry
    score = 0
    retry = ""
    for key, value in question_dic.items():  # prints the questions out to the user and asks for an input
        print(count, ".", key)
        for items in range(4):
            print(value[items])
        count = count + 1
        ans = ""  # Variable for answer
        while ans not in valid:  # checks if the answer is valid
            ans = input("-----Please enter A, B, C, D to answer-----\nWhat is your answer? ")
            print("")
        if ans.upper() == value[4] or value[5]:  # checks if the answer is correct and prints this statement
            print("Congrats, you are correct!")
            score = score + 1
            print("Your score is", score)
            print("")
        else:  # checks if the answer is incorrect and prints this statement
            print("Sorry, your answer was incorrect!")
            print("Your score is", score)
            print("")
    print("Congrats,", a, "you completed the Education quiz!")  # Prints if user gets 5 or bellow
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

    while retry not in retry_ans:  # Asks the user if they want to try again
        retry = input(
            "Would you like to try the quiz again to get a better score?\nPlease enter yes or no: ")  # Input for retry
        print("")
        retry = retry.upper()  # Makes the retry answer uppercase
    return score, retry  # Returns score and retry


def writing_to_file(a, b):  # definition used to write back the data to the file for the users final score
    with open('Score.txt', 'a') as writing:
        writing.write(a + ":" + str(b) + "\n")


def main():  # Definition for the main part of the code
    final_score = 0  # Variable for users final score
    name = intro()  # runs intro def and returns name
    score, retry = questions(name)  # runs questions def and returns score and retry
    if final_score <= score:
        final_score = score
    while retry == "YES":  # Asks the user if they want to retry the quiz and if they do it restarts it
        retry = ""

        question_dic = {}
        with open('realques.txt') as f:  # Splits the question file into the separate questions in a dictionary
            lines = list(f)
            while len(
                    question_dic) < 15:  # This part of code splits the question file into parts so it can ask the
                # user the questions
                question = random.choice(lines).strip()
                a, b = question.split(";")
                c = b.split("|")
                question_dic[a] = c

        score, retry = questions(name)
        if final_score <= score:
            final_score = score
    if retry == "NO":  # If the user does not want to retry the quiz it ends the quiz
        writing_to_file(name, final_score)  # Runs the definition for write to file
        print("Congrats,", name, "your final score was", final_score, "!")  # Final statement
        print("Thanks for playing the Education quiz")
        print("Goodbye...")
        exit()


if __name__ == "__main__":  # Uses main function to run the entire program
    main()
