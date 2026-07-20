# 🧠 Quiz Game

A simple command-line quiz game built in Python that tests your basic programming knowledge through multiple-choice questions.

## 📋 Description

This project presents the user with a series of multiple-choice questions related to programming fundamentals. For each question, the user selects an option (A, B, C, or D), and the program checks the answer, keeps track of the score, and displays the final result at the end.

## ✨ Features

- Multiple-choice questions with 4 options each
- Case-insensitive answer input (accepts both uppercase and lowercase)
- Instant feedback on wrong answers
- Final score summary at the end of the quiz
- Clean and simple console-based interface

## 🛠️ How It Works

1. The program stores questions, their respective options, and correct answers using tuples.
2. It loops through each question using `enumerate()` to track the question index.
3. For every question, all available options are displayed to the user.
4. The user enters their guess (A/B/C/D), which is converted to lowercase for comparison.
5. If the guess matches the correct answer, the score increases by 1.
6. If the guess is wrong, "Wrong Answer" is displayed.
7. After all questions are answered, the final score is displayed in the format `Score/Total Questions`.

## 🚀 How to Run

1. Make sure Python is installed on your system.
2. Clone this repository or navigate to this folder.
3. Run the script using:

```bash
python Quiz_Game.py
```

4. Follow the on-screen instructions and enter your answers (A, B, C, or D) when prompted.

## 📝 Sample Output

```
--------------------------
What does CPU stand for?: 
A:Central Processing Unit
B:Computer Personal Unit
C:Central Program Utility
D:Control Processing Unit
Enter your guess: A, B, C, D : a
--------------------------
...
Quiz Finished!
Your score is 3/4
```

## 📂 Project Structure

```
07-Quiz_Game/
├── Quiz_Game.py
└── README.md
```

## 💡 Possible Improvements

- Add a timer for each question
- Randomize the order of questions
- Add support for more categories/topics
- Store high scores in a file

## 🧑‍💻 Author

Part of my Python learning journey — daily practice, beginner projects, and problem solving.
