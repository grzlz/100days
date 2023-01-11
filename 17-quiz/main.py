# Create quiz game
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


# Create question bank
question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

q = QuizBrain(question_bank)
q.next_question()

print(q.current_question.answer)
