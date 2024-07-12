import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty Fields", message="Do not leave any fields empty")
    else:
        try:
            with open("passwords.json", "r") as file:
                # reading old data
                data = json.load(file)
        except FileNotFoundError:
            print("Let's just make a new \"passwords.json\"")
            with open("passwords.json", "w") as file:
                # saving
                json.dump(new_data, file, indent=4)
        else:
            # updating with new data
            data.update(new_data)

            with open("passwords.json", "w") as file:
                # saving
                json.dump(new_data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- find password ------------------------------- #
def find_password():
    user_search = website_entry.get()
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            if user_search in data:
                messagebox.showinfo(title="database search...", message=f"\"{user_search}\" is in our website database"
                                                                        f"\nand here is the information:"
                                                                        f"\n{data[user_search]}")
            else:
                messagebox.showerror(title="database search...", message=f"\"{user_search}\" is NOT a website in our "
                                                                         f"database\nspelling and \".com\" specifics matter")
    except FileNotFoundError:
        print(FileNotFoundError)
        print("no json file to load from OR the file is named wrong")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

canvas = Canvas(window, width=200, height=200)
canvas.grid(column=1, row=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "cameronpool2019@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
password_button = Button(width=15, text="Generate Password:", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
