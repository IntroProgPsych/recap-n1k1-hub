question1 = "What is 1 + 1?(a= 1, b=2 or c=3)"
answer1 = "b"

questions = [{"text": "What is 1 + 1?(a= 1, b=2 or c=3)",
              "correct" : "b"},
              {"text": "What is 2 + 2?(a= 2, b=0 or c=4)",
               "correct" : "c"},
               ]

def run_rest():
    score = 0

    for question in questions:
        print(question["text"])

        answer = input("Your answer should be a, b or c")
        if answer == question["correct"]:
            print("Correct")
        else:
            print("Wrong")

    return score

def interpetscore(score):
    print("Your total score is:" , score)
    if score > 1 :
        print("You passed")
    else:
        print("You failed")


finalscore = run_rest()
print(finalscore)