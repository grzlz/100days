from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="✓")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps 

    if reps % 4 == 0:
        current_time = LONG_BREAK_MIN
        label.config(text="Long break", fg=PINK)
    elif reps % 4 == 2:
        current_time = SHORT_BREAK_MIN
        label.config(text="Break", fg=RED)
    else:
        current_time = WORK_MIN
        label.config(text="Work", fg=GREEN)

    count_down(current_time * 60)

    check_marks.config(text=f"{'✓'*reps}")
    reps += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    time_remaining = f"{count_min}:{count_sec}"


    canvas.itemconfig(timer_text, text=time_remaining)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #¨
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightbackground=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130 , text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)


# Label
label = Label(text="Timer", foreground=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
label.grid(column=1, row=0)

# Buttons
start_button = Button(text="start", highlightbackground=YELLOW, command=start_timer)
reset_button = Button(text="reset", highlightbackground=YELLOW, command=reset_timer)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

# Checkmarks
check_marks = Label(text="", foreground=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=2)





 




window.mainloop()