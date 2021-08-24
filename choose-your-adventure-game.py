name = input("Type your name: ")
print("Welcome", name, "to your adventure")


answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right")

if answer =="left":
    answer = input("You come across a river and can walk around to swin across? Type walk to walk around or swim to swim around")

    if answer =="swim":
        print("")
    elif answer =="walk":
        print("")

    else:
        print("not a valid option. your quest has ended")
        
    
elif answer =="right":
    print()

else:
    print("Not a valid option. Your quest has ended")
