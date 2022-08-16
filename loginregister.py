from tkinter import *


def click():
    username = usernamee.get()
    password = passwordd.get()
    with open("user.txt",'r') as file:
        file = file.read()
        file = file.split()
        if username in file:
            index = file.index(username) + 2
            passw = file[index]
            if passw == password:
                Label(window,text= f"welcome back {username}",font="none 12 bold").grid(row=1, column=3, sticky=W)
            else:
                Label(window,text="password wrong, try again!!", font="none 12 bold", fg='red',bg="white").grid(row=1, column=3, sticky=W)
        else:
            Label(window,text="error in password or username!", font="none 12 bold", fg='red',).grid(row=1, column=3, sticky=W) 
def click2():
    username = usernamee0.get()
    password = passwordd0.get()
    password1 = passwordd1.get()
    file = open("user.txt",'r')
    file = file.read()
    file = file.split()
    if username in file:
        Label(window,text= "username already taken.",font="none 12 bold").grid(row=13, column=3, sticky=W)
    elif username not in file:
        if password != password1:
            Label(window,text= "password not match",font="none 12 bold").grid(row=13, column=3, sticky=W)
        else:
            with open("user.txt", "a+") as file:
                test = (f"username: {username} password: {password}\n")
                file.write(test)
                file.close()
                Label(window,text= "congratulation, now you have an account",font="none 12 bold").grid(row=13, column=3, sticky=W)
window = Tk()
window.title("Co2App")
window.minsize(width=600,height=200)

Label(window,text="username:",font="none 12 bold").grid(row=1, column=1, sticky=W)
usernamee = Entry(window, width=25)
usernamee.grid(row=1, column=2)
Label(window,text="password:",font="none 12 bold").grid(row=3, column=1, sticky=W)
passwordd = Entry(window, width=25)
passwordd.grid(row=3, column=2)
Button(window,text="login",width=6,command=click).grid(row=4, column=2)
Label(window,text="username:",font="none 12 bold").grid(row=6, column=1, sticky=W)
usernamee0 = Entry(window, width=25)
usernamee0.grid(row=6, column=2)
Label(window,text="password:",font="none 12 bold").grid(row=9, column=1, sticky=W)
passwordd0 = Entry(window, width=25)
passwordd0.grid(row=9, column=2)
Label(window,text="rewrite password:",font="none 12 bold").grid(row=10, column=1, sticky=W)
passwordd1 = Entry(window, width=25)
passwordd1.grid(row=10, column=2)
Button(window,text="register",width=6,command=click2).grid(row=11, column=2)


window.mainloop()