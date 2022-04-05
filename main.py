from random import randint,choice,shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def passwordGenerator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols=[choice(symbols) for _ in range(randint(2,4))]
    password_number=[choice(numbers)for _ in range(randint(2,4))]

    password_list=password_letters+password_symbols+password_number
    shuffle(password_list)
    
    password="".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)

    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def saveFile():
    web_input_data=web_input.get()
    username_data=username_input.get()
    password_data=password_input.get()
    new_data={
        web_input_data:{
        "email":username_data,
        "password":password_data
         }
    }

    if len(web_input_data) | len(password_data) == 0:
        messagebox.showwarning(title="WARNING",message="Please enter all the fields")
    else:
        is_ok=messagebox.showinfo(title="title",message=f"These are the details enterd :\nEmail: {username_data}\nPassword: {password_data}")
        if(is_ok):
            try:
                with open("data.json","r") as data_file:
                    #Reading data
                    data=json.load(data_file)

            except FileNotFoundError:
                with open("data.json","w") as data_file:
                    json.dump(new_data,data_file,indent=4)

            else:
                #updatae data
                data.update(new_data)
                with open("data.json","w") as data_file:
                    json.dump(data,data_file,indent=4)

            finally:
                web_input.delete(0,END)
                password_input.delete(0,END)

#----------------------------FIND PASSWORD-----------------------------#
def search():
    website=web_input.get()
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error",message="No data Files Found")
    else:
         if website in data:
            email=data[website]["email"]
            passwrd=data[website]["password"]
            messagebox.showinfo(title=website,message=f"email: {email}\npassword: {passwrd}")

         else:
             messagebox.showinfo(title="Error",message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.minsize(width=500,height=400)
window.title("Password Manager by BK")
window.config(padx=50,pady=50)


canvas=Canvas(width=200,height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

#names
web=Label(text="Website :").grid(row=1,column=0)
username=Label(text="email/Username :").grid(row=2,column=0)
password=Label(text="Password :").grid(row=3,column=0)

#Entry

web_input=Entry(width=24)
web_input.focus()
web_input.grid(row=1,column=1)

username_input=Entry(width=36)
username_input.insert(END,"@gmail.com")
username_input.grid(row=2,column=1,columnspan=2)

password_input=Entry(width=24)
password_input.grid(row=3,column=1)

#button
search=Button(text="Search",command=search).grid(row=1,column=2)

generate_psswd=Button(text="generate Password",command=passwordGenerator).grid(row=3,column=2)

add_button=Button(text="Add",command=saveFile,width=36).grid(row=4,column=1,columnspan=2)


window.mainloop()
