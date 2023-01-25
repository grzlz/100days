from tkinter import * 

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label!", font=("Arial", 18, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)
# Button
button = Button(text="Click me!")
button.grid(column=1, row=1)

# New button
new_button = Button(text="I'm the new button!")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)
































window.mainloop()