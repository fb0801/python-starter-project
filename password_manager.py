pwd =input("What is the master password? ")


def view():
    pass

def add():
    pass



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
