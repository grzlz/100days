# Create quiz game
from question_model import Question
from data import question_data

# Create question bank
question_bank = []
for i in question_data:
    question_bank.append(Question(i["text"], i["answer"]))

