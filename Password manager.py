from tkinter import *
from tkinter import messagebox
import random
import pyperclip

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.delete(0, END) 
    pass_entry.insert(0, password)
    pyperclip.copy(password)

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                             f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            clear()

def clear():
    website_entry.delete(0, END)
    pass_entry.delete(0, END)
    email_entry.delete(0, END)

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=1, column=2)

email_label = Label(text="Email / Username:")
email_label.grid(row=3, column=1, sticky="e")

email_entry = Entry(width=35)
email_entry.grid(row=3, column=2, sticky="w")

website_label = Label(text="Website:")
website_label.grid(row=4, column=1, sticky="e")

website_entry = Entry(width=35)
website_entry.grid(row=4, column=2, sticky="w")

password_label = Label(text="Password:")
password_label.grid(row=5, column=1, sticky="e")

pass_entry = Entry(width=35)
pass_entry.grid(row=5, column=2, sticky="w")

pass_button = Button(text="Generate Password", width=25, command=generate_password)
pass_button.grid(row=5, column=3)

add_button = Button(text="ADD DETAILS", width=36, command=save)
add_button.grid(row=7, column=2)

window.mainloop()
