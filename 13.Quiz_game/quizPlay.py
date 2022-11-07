from quizQuestionAnswer import *

def quizPlay():

    questions = getQuizQuestions()
    answers = getQuizAnswers()

    print("Wellcome to quiz game !!")
    print('NOTE: if your spelling is incorrect then it is considered as wrong answer')

    score = 0
    for i in range (len(questions)):

        print(f"Question nº{i+1}: {questions[i]}")
        showMultipleAnswer(answers)
        user_ans = int(input("Answer: "))

        if (answers[user_ans] == answers[i]):
            score += 1
            print("Correct! You got 1 point")
        else:
            print(f"Incorrect!. The answer is: {answers[i]}")
        
    print(f"Number of questions: {len(questions)}")
    print(f"Your score is: {score}")

    try:
        percentaje = (score * 100) / len(questions)
    except ZeroDivisionError:
        print("0% questions are correct.")

    print(f"{percentaje}% questions a are correct.")