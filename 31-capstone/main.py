from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

# UI Setup
window = Tk()
window.title("Learn french")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=525, background=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
rigt_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
front_canvas = PhotoImage(file="images/card_front.png")
back_canvas = PhotoImage(file="images/card_back.png")

canvas.create_image(400, 260, image=back_canvas)
canvas.create_image(400, 260, image=front_canvas)
title_text = canvas.create_text(400, 150 , text="Title", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 260 , text="Word", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
right_button = Button(image=rigt_img)
wrong_button = Button(image=wrong_img)

right_button.grid(column=1, row=2)
wrong_button.grid(column=0, row=2)



window.mainloop()
