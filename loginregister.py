#welcome to my login system project (co2)


def start():
    print("welcome to Co2 App \n if you wanna login write 1 \n if you want to register write 2 \n if wanna quit write 3")
    user_want = input()
    if user_want == '1':
        login()
    elif user_want == '2':
        register()
    elif user_want == "3":
        quit()
    else:
        print("something went wrong try again")
        return start()

def login():
    username = str(input('whats your username: '))
    password = str(input('whats your password: '))
    with open("user.txt",'r') as file:
        file = file.read()
        file = file.split()
        if username in file:
            index = file.index(username) + 2
            passw = file[index]
            if passw == password:
                print(f'welcome back {username}')
                return quit()
            else:
                print("error in password")
                return login()
        else:
            print("error in password or username")
            return start()

def register():
    username = str(input('username: '))
    password = str(input('password: '))
    password1 = str(input('enter password again: '))
    file = open("user.txt",'r')
    file = file.read()
    file = file.split()
    if username in file:
        print('username already taken')
        return register()
    elif username not in file:
        if password != password1:
            print('password error')
            return register()
        else:
            with open("user.txt", "a+") as file:
                test = (f"username: {username} password: {password}\n")
                file.write(test)
                file.close()
                print("congratulation you now have an account, go login")
                return login()

start()