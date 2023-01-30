from tkinter import *
from random import choice
import pandas as pd
from time import sleep


BACKGROUND_COLOR = "#B1DDC6"

# Set global variables
words = {}
word = {}
# Read saved or new file
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    words = data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")

def next_word():
    global word, timer
    window.after_cancel(timer)
    word = choice(words)
    fr = word["French"]
    canvas.itemconfig(canvas_image, image = front_canvas)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=fr, fill="black")
    timer = window.after(3000, display_word)

def display_word():
    en = word["English"]
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=en, fill="white")
    canvas.itemconfig(canvas_image, image = back_canvas)

def is_known():
    words.remove(word)
    data = pd.DataFrame(words)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()

# UI Setup
window = Tk()
window.title("Learn french")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, display_word)

canvas = Canvas(width=800, height=525, background=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
rigt_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
front_canvas = PhotoImage(file="images/card_front.png")
back_canvas = PhotoImage(file="images/card_back.png")


canvas_image = canvas.create_image(400, 260, image=front_canvas)
title_text = canvas.create_text(400, 150 , text="Welcome!", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 260 , text="Learn some french.", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
right_button = Button(image=rigt_img, command=is_known)
wrong_button = Button(image=wrong_img, command=next_word)

right_button.grid(column=1, row=2)
wrong_button.grid(column=0, row=2)


next_word()

window.mainloop()
