import random
import time  # Import for time when using time.sleep


valid = ["A", "B", "C", "D", "a", "b", "c", "d"]  # List of answers the user can enter


def file_to_list(file_name):
    """
    Load questions from a file.
    """
    with open(file_name, 'r', encoding = "utf8") as file:
        for line in file:
            data = line.split(';')
            if data[-1].endswith('\n'):
                data[-1] = data[-1][:-1]
            if data[-1].endswith('\r'):
                data[-1] = data[-1][:-1]
            options = data[1].split("|")
            correct_answers = data[2].split("|")
            try:
                list_from_file.append([data[0], options, correct_answers])
            except (NameError, UnboundLocalError):
                list_from_file: list = [[data[0], options, correct_answers]]
    return list_from_file


# noinspection DuplicatedCode
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


def score_logic(score_num):
    print("You got a score of", score_num, "/ 15")
    if score_num <= 5:  # The program determines how well the user did and prints their name and score out to them
        print("Better luck next time!")
    elif score_num <= 10:
        print("Good job you did well!")
    elif score_num < 15:
        print("Great work you actually did really well!")
    elif score_num == 15:
        print("You got a perfect score!\nExcellent work!")


# noinspection DuplicatedCode
def questions(player_name, question_list):  # Definition for main part of code which is the questions
    count = 1  # Variables for count, score, and retry
    score = 0
    for sublist in question_list:  # prints the questions out to the user and asks for an input
        print(f"Question {count}: {sublist[0]}\nOptions: {', '.join(sublist[1])}\n")
        count += 1
        ans = ""  # Variable for answer
        while ans not in valid:  # checks if the answer is valid
            ans = input("What is your answer? ")
            print("")
        if ans.upper() in sublist[2]:  # checks if the answer is correct and prints this statement
            print("Congrats, you are correct!")
            score += 1
            print("Your score is", score)
            print("")
        else:  # checks if the answer is incorrect and prints this statement
            print("Sorry, your answer was incorrect!")
            print("Your score is", score)
            print("")
    print("Congrats,", player_name, "you completed the Education quiz!")  # Prints if user gets 5 or bellow
    score_logic(score)
    play_again_check = input("Would you like to retry the quiz? (YES/NO) ")
    while play_again_check not in ['yes', 'no']:  # Asks the user if they want to try again
        play_again_check = input(
            "Sorry, your input was not recognised. Please enter either 'yes' or 'no'.\nWould you like to try the quiz "
            "again to get a better score?\nPlease enter 'yes' or 'no' here: ").lower().strip()  #
        # Input
        # for retry
        print("")
    return score, play_again_check  # Returns score and retry


# noinspection DuplicatedCode
def writing_to_file(a, b):  # definition used to write back the data to the file for the users final score
    with open('Score.txt', 'a') as writing:
        writing.write(a + ":" + str(b) + "\n")


# noinspection DuplicatedCode
def main():  # Definition for the main part of the code

    quiz = file_to_list("realques.txt")

    final_score = 0  # Variable for users final score
    player = intro()  # runs intro def and returns name
    score, retry = questions(player, quiz)  # runs questions def and returns score and retry
    final_score += score  # adds the score to the final score

    if retry == "no":  # If the user does not want to retry the quiz it ends the quiz
        writing_to_file(player, final_score)  # Runs the definition for write to file
        print(f"Congrats, {player}, your final score was {final_score}!")  # Final statement
        print("Thanks for playing the Education quiz")
        print("Goodbye...")
        exit()


if __name__ == "__main__":  # Uses main function to run the entire program
    main()
