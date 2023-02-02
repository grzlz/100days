from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk() 
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.canvas = Canvas(width=300, height=250, background="white", highlightbackground="white")
        self.question_text = self.canvas.create_text(150, 125, width= 280, text="New quiz GUI", fill = THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=(50,50))


        self.score_label = Label(text="Score: ", bg=THEME_COLOR, fg="white", font=("Arial", 13))
        self.score_label.grid(column=1, row=0)
        
        # Create buttons
        self.true_button = Button(image=true_img, command=self.clicked_true)
        self.false_button = Button(image=false_img, command=self.clicked_false)

        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)
        
        self.get_next_question()
        
        self.window.mainloop()

    def clicked_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def clicked_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():    
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text="No more questions.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)