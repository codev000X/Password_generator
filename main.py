from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


FONT=("Cursive",12,"bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list  += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    print(f"Your password is: {password}")
    p_input.insert(0 , password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():

    web_hold=w_input.get()
    try:
        with open("data.json","r") as file:
            data=json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Oooops",message=" Given website does not exist\nPlease recheck the entered website name.")
    finally:
        with open("data.json", "r") as file:
            data = json.load(file)
        if web_hold in data:
            messagebox.showinfo(message=f"Email : {data[web_hold]["email"]}\nPassword : {data[web_hold]["password"]}",
                                title=web_hold)
        else:
            messagebox.showinfo(title="File not Found",message="you dont save any data with this name")
def add_info():
    web_hold=w_input.get()
    email_hold=e_input.get()
    password_hold=p_input.get()
    new_file={
        web_hold:{"email" : email_hold,
                "password" : password_hold,
                  }
    }
    if len(web_hold)==0 or len(password_hold)==0:
        messagebox.showwarning(title="Fill All Fields",message="Please don't leave any of the fields empty.")
    else:
        try:
            with open("data.json","r") as file:
                data=json.load(file)
                data.update(new_file)

        except (FileNotFoundError,json.decoder.JSONDecodeError):
            with open("data.json" , "w") as file:
                json.dump(new_file,file,indent=4)

        else:

            with open("data.json","w") as file:
                json.dump(data,file,indent=4)

        finally:
            w_input.delete(0,END)
            p_input.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=70,pady=50)

canvas=Canvas()
image=PhotoImage(file="logo.png")
canvas.create_image(200,189,image=image)
canvas.grid(row=0,column=1)

# labels
web=Label(text="Website :",font=FONT)
web.grid(column=0 , row=1)
email=Label(text="Email/Username :",font=FONT)
email.grid(column=0 , row=2)
p_word=Label(text="Password :",font=FONT)
p_word.grid(column=0 , row=3)

# entry
w_input=Entry(width=63)
w_input.focus()
w_input.grid(column=1 , row=1 )
e_input=Entry(width=82)
e_input.insert(0 , "shahzaibkhalid1101@gmail.com")
e_input.grid(column=1 , row=2 , columnspan=2)
p_input=Entry(width=63)
p_input.grid(column=1 , row=3 )

# button
p_button=Button(text="Generate Password",width=14 , height=1 , command=generate)
p_button.grid(column=2 , row=3)
add_button=Button(text="Add" , width=69 , command=add_info)
add_button.grid(column=1 , row=4 , columnspan=2)
s_button=Button(text="Search",width=14,height=1,command=find_password)
s_button.grid(column=2,row=1)




window.mainloop()