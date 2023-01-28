from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

lower_case_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

constants = {
    "capital_letters": [letter.upper() for letter in lower_case_letters],
    "lower_case_letters": lower_case_letters,
    "symbols": ["!", "#", "$", "%", "&", "/", "(", ")", "=", "?", "¡"]
}

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    upper_case_characters = [choice(constants.get("capital_letters")) for i in range(4)]
    lower_case_characters = [choice(constants.get("lower_case_letters")) for i in range(4)]
    symbol_characters = [choice(constants.get("symbols")) for i in range(4)]
    password = upper_case_characters + lower_case_characters + symbol_characters
    shuffle(password)

    return "".join(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    messagebox.askokcancel(title=website, message=f"These are the details entered:\nusername: {username}\npassword: {password}\nIs it okay to save?")

    with open("data.txt", "a") as file:
        file.write(f"{website} | {username} | {password}\n")

    website_input.delete(0, END)
    username_input.delete(0, END)
    password_input.delete(0, END)

    website_input.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Inputs
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky=EW)
website_input.focus()

username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2, sticky=EW)

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky=EW)

# Buttons
generate_password_button = Button(text="Generate password", command=generate_password) 
generate_password_button.grid(column=2, row=3, sticky=EW)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan = 2, sticky=EW)

window.mainloop()