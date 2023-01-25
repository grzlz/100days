from tkinter import * 

def button_click():
    km = int(input.get()) * 1.6
    km_output.config(text=km)

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Inital label
my_label = Label(text="Miles to km converter", font=("Arial", 18, "bold"))
my_label.grid(column=0, row=0)
# Entry
input = Entry(width=10)
input.grid(column=3, row=2)
# Miles label
miles_label = Label(text="miles", font=("Arial", 10))
miles_label.grid(column=4, row=2)
# Km space
km_output = Label(text="0", font=("Arial", 10))
km_output.grid(column=3, row=3)
# Km label
km_label = Label(text="km", font=("Arial", 10))
km_label.grid(column=4, row=3)
# Button
button = Button(text="Convert", command=button_click)
button.grid(column=3, row=4)

# Create miles to km converter

# Create initial label
# Create  






























window.mainloop()