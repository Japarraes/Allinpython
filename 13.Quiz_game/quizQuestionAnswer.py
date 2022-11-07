quiz = {
        "what does CPU stand for?": "central processing unit",
        "what does GPU stand for?": "graphics processing unit",
        "what does RAM stand for?": "random access memory",
        "what does PSU stand for?": "power supply unit",
        "what does ROM stand for?": "read only memory"
    }

def getQuizQuestions():
    
    questions = []
    for item in quiz.keys():
        questions.append(item)

    return questions

def getQuizAnswers():
    answers = []
    for item in quiz.values():
        answers.append(item)
        
    return answers

def showMultipleAnswer(list):
    for i in range (len(list)):
        print(f"{i}. {list[i]}")