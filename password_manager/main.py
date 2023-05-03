from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT_NAME = "Franklin Gothic"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)
    messagebox.showinfo(message="Password copied to clipboard!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # grabbing user input
    # Istead of using the website name as primary key it is better to use a unique
    # Identifier to take care of case when the user has two credentials for the same
    # Website. (Implement this after search).
    website_name = website_name_entry.get()
    user_name_or_email = email_username_entry.get()
    password_generated = password_entry.get()

    # Check for empty fields
    if len(website_name) == 0 or len(password_generated) == 0:
        messagebox.showerror(title="Error!", message="Please don't leave any fields empty!")
    else:
        # writing to file
        data = {
            website_name: {
                "user_name": user_name_or_email,
                "password": password_generated
            }
        }
        try:
            with open('data.json', 'r+') as file:
                prev_data = json.load(file)
                prev_data.update(data)
                file.seek(0)
                json.dump(prev_data, file, indent=4)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        website_name_entry.delete(0, END)
        email_username_entry.delete(0, END)
        email_username_entry.insert(END, "nithishkr62@gmail.com")
        password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_name = website_name_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="File Not Found",
                             message="No Data File Found")
    else:
        if website_name in data:
            messagebox.showinfo(title=website_name, message=f"Email/Username: {data[website_name]['user_name']}\n"
                                                            f"Password: {data[website_name]['password']}")
        else:
            messagebox.showerror(title="Website Not Found",
                                 message="No Details for the website exists")


if __name__ == "__main__":
    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)

    canvas = Canvas(width=200, height=200)

    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(column=1, row=0)

    # Labels:
    # Website
    website_label = Label(text="Website:", font=(FONT_NAME, 10))
    website_label.grid(column=0, row=1)

    # Email/Username
    email_label = Label(text="Email/Username:", font=(FONT_NAME, 10))
    email_label.grid(column=0, row=2)

    # Password:
    password_label = Label(text="Password:", font=(FONT_NAME, 10))
    password_label.grid(column=0, row=3)

    # Text box:
    # Entry for Website
    website_name_entry = Entry(width=34)
    website_name_entry.grid(column=1, row=1, sticky='w')
    website_name_entry.focus()  # To get the cursor on the first textbox the user needs to type.

    # Entry for Email/Username
    email_username_entry = Entry(width=53)
    email_username_entry.grid(column=1, row=2, columnspan=2)
    email_username_entry.insert(END, "nithishkr62@gmail.com")

    # Entry for Password:
    password_entry = Entry(width=34)
    password_entry.grid(column=1, row=3, sticky="w")

    # Buttons:
    # Button to Generate Password

    password_button = Button(text="Generate Password", command=generate_password)
    password_button.grid(column=2, row=3, columnspan=2)

    # Button to "Add"
    add_button = Button(text="Add", width=45, command=save)
    add_button.grid(column=1, row=4, columnspan=3)

    # Search button
    search_button = Button(text="Search", justify="center", width=14, command=find_password)
    search_button.grid(column=2, row=1, columnspan=2)

    window.mainloop()
