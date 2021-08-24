from cryptography.fernet import Fernet




'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file =open("key.key", "rb")
    key=file.read()
    file.close()
    return key





master_pwd =input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
     with open("passwords.txt", "r") as f:
        #read a file
        for line in r.readlines():
            #print(line.rstrip()) #right strip the \n
            data = line.rstrip()
            user, passsw = data.split("|")
            print("User:", user, "Password:", fer.decrypt(passw.encode()))

            
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        #create a file and add data to it
        f.write(name + "|" + fer.encrypt(pwd.encode()) + "\n")



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
