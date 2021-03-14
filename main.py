from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# The new password will be displayed after "Generate" button is clicked:
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
               'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Specifying numbers of characters for each category:
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Creating a list of password characters out of three lists:
    password_letters = [random.choice(letters) for l in range(nr_letters)]
    password_symbols = [random.choice(symbols) for s in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for n in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)  # Shuffling characters for a stronger password:
    password = "".join(password_list)  # Saving password as a string:
    password_display.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# Function that will save all entry and new password to a text file and empty the fields:
def save_to_file():
    # Saving the entries as variables, to be used later
    website = website_entry.get()
    email = email_entry.get()
    password = password_display.get()

    # Checking if any field is left empty - a pop up will warn the user:
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        # Creating a pop-up for the user to verify the entered information.
        is_ok = messagebox.askokcancel(title=website, message=
        f"Here are the details entered:\nEmail: {email}, Password: {password}\n Is it OK to save?")

        # When user clicks "OK" on the pop-up, the data will be appended to the text file and the fields will clear:
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_display.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()  # main window
window.title("Password Manager".center(20))
window.config(padx=50, pady=50)
canvas = Canvas(width=220, height=220)  # canvas for the logo image file
logo = PhotoImage(file="logo.png")
canvas.create_image(110, 110, image=logo)
canvas.grid(column=1, row=0)  # placing the image centrally
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()  # Focuses cursor on the start of the field
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "p_gerasimenko@yahoo.com")  # starting value (common email)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_display = Entry(width=37)
password_display.grid(column=1, row=3)
generate_password_button = Button(text="Generate", font="bold", width=7, fg="red",
                                  relief="raised", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(width=33, text="Add", font="bold", command=save_to_file,
                    fg="red", relief="raised")
add_button.grid(column=1, row=4, columnspan=2)
add_button.config(pady=1)



window.mainloop()