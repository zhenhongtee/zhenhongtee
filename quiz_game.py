# -----------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_number = 1
    for key in questions:
        print("-----------------------")
        print(key)
        for i in options[question_number-1]:
            print(i)
        guess = input("A, B, C or D?:").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        question_number += 1
    display_score(correct_guesses, guesses)

# -----------------------
def check_answer(answer,guess):
    print("-----------------------")
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

# -----------------------
def display_score(correct_guesses, guesses):
    print("-----------------------")
    print("RESULTS")
    print("-----------------------")
    print("Answers", end = " ")
    for i in questions:
        print(questions.get(i), end = " ")
    print()

    print("Guesses", end = " ")
    for i in guesses:
        print(i, end = " ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is " + str(score) + "%")

# -----------------------
def play_again():
    response = input("Play again (yes/no)?:").upper()
    if response == "YES":
        return True
    else:
        return False

questions = {
"1. 1+1":"A",
"2. 2+2":"B",
"3. 3+3":"C",
"4. 4+4":"D"
}

options = [["A.2","B.4","C.6","D.8"],["A.2","B.4","C.6","D.8"],["A.2","B.4","C.6","D.8"],["A.2","B.4","C.6","D.8"]]

new_game()

while play_again():
    new_game()

print("Bye!")