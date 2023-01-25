from tkinter import * 

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label!", font=("Arial", 24, "bold"))
my_label.pack(expand=True)


def button_click():
    my_label.config(text=input.get())


# Create button
button = Button(text="Click me!", command=button_click)
button.pack()

# Entry
input = Entry(width=10)
input.pack()






































window.mainloop()