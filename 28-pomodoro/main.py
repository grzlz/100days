from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #¨
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightbackground=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
canvas.create_text(103, 130 , text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

# Label
label = Label(text="Timer", foreground=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
label.grid(column=1, row=0)

# Buttons
start_button = Button(text="start", highlightbackground=YELLOW)
reset_button = Button(text="reset", highlightbackground=YELLOW)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

# Checkmarks
check_marks = Label(text="✓", foreground=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=2)





 




window.mainloop()