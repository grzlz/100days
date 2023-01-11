# Create quiz game
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
from os import system


# Create question bank
question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

q = QuizBrain(question_bank)

while q.still_has_questions():
    q.next_question()

system("clear")
print(f"Game over! Your final score was {q.score}/{q.question_number}")
