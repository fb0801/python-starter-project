master_pwd =input("What is the master password? ")


def view():
    pass

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        #create a file and add data to it
        f.write(name + "|" + pwd)



while True:
    mode = input("add new pwd or view exisitn ones (view or addd)").lower()

    if mode =="view":
        view()

    elif mode=="add":
        add()
    elif mode=="q":
        break

    else:
        print("Invalid option")
