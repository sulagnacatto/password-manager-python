from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save(): 
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="OOPS!",message="please dont the fields empty")

    else:


        response = messagebox.askokcancel(title=website, message=f"The email: {email}\nThe password: {password} for {website}\nWould you like to proceed? If not, click Cancel.")
        if response:
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            password_entry.delete(0,END) 


    try:
        with open("data.txt", "a") as password_data:
            password_data.write(f"{website}|{email}|{password}\n")
    except Exception as e:
        print("An error occurred while writing to the file:", e)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
sexy_image = PhotoImage(file="logo_pass.png")
canvas.create_image(100, 100, image=sexy_image)
canvas.grid(row=0, column=0, columnspan=3)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus() 
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=35) 
password_entry.grid(row=3, column=1)  # Adjusted column span to 1

#generate_password = Button(text="Generate Password")
#generate_password.grid(row=3, column=2) 
add_button = Button(text="Add", width=36,command=save) 
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop() 
