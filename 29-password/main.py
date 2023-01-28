from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    with open("data.txt", "a") as file:
        file.write(f"{website}-{username}-{password}\n")



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
generate_password_button = Button(text="Generate password") 
generate_password_button.grid(column=2, row=3, sticky=EW)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan = 2, sticky=EW)

window.mainloop()