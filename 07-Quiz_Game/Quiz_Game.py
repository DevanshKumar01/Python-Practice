Questions = ("What does CPU stand for?: ",
             "Who created Python?: ",
             "What is the extension of a Python file?: ",
             "Which data type is used to store True or False values?: ")

Options = (("A:Central Processing Unit", "B:Computer Personal Unit", "C:Central Program Utility", "D:Control Processing Unit"),
           ("A:Elon Musk", "B:Guido van Rossum", "C:Bill Gates", "D:Dennis Ritchie"),
           ("A:.py", "B:.python", "C:.pt", "D:.pyt"),
           ("A:Integer", "B:String", "C:Boolean", "D:Float"))

Answers = ("a", "b", "a", "c")

Score = 0

for index, Question in enumerate(Questions):
    print("--------------------------")
    print(Question)

    for Option in Options[index]:
        print(Option)

    guess = input("Enter your guess: A, B, C, D : ").lower()

    if guess == Answers[index]:
        Score += 1
    else:
        print("Wrong Answer")

print("--------------------------")
print("Quiz Finished!")
print(f"Your score is {Score}/{len(Questions)}")
