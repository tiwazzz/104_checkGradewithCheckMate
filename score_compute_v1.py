scoreList = []

def gradeCompute(score):
    if score >= 90:
        graded = "A+"
    elif score >= 85:
        graded = "A"
    elif score >= 80:
        graded = "A-"
    elif score >= 77:
        graded = "B+"
    elif score >= 73:
        graded = "B"
    elif score >= 70:
        graded = "B-"
    elif score >= 65:
        graded = "C+"
    elif score >= 60:
        graded = "C"
    elif score >= 55:
        graded = "C-"
    elif score >= 50:
        graded = "D"
    else:
        graded = "F"
    return graded

try:
    while True:
        scoreInput = int(input("Enter your score (press CTRL+C for stop input keyboard): "))
        scoreList.append(scoreInput)
except KeyboardInterrupt:
    for score in scoreList:
        if score >= 80:
            print(f"Congratulation!, You got {gradeCompute(score)} grade, This is your score: {score}.")
        elif score >= 50:
            print(f"Good Job!, You got {gradeCompute(score)} grade, This is your score: {score}.")
        else:
            print(f"Be good next time :(, You got {gradeCompute(score)} grade, This is your score: {score}.")
except TypeError:
    print("Error!, Please check your list:")
    print("This is your score list", scoreList)