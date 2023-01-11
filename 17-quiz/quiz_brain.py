class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        if self.question_number >= len(self.question_list):
            return False
        return True

    def next_question(self):
        self.question_number += 1
        current_question = self.question_list[self.question_number]

        self.user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ")
