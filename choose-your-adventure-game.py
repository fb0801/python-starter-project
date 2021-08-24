name = input("Type your name: ")
print("Welcome", name, "to your adventure")


answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right")

if answer =="left":
    answer = input("You come across a river and can walk around to swin across? Type walk to walk around or swim to swim around").lower()

    if answer =="swim":
        print("you swam across and were eaten by an alligator.")
    elif answer =="walk":
        print("you walked for many miles, ran out of food and water")

    else:
        print("not a valid option. your quest has ended")
        
    
elif answer =="right":
    answer = input("You stumble across a old bridge, you want to cross it or head back (cross/back)").lower()

    if answer =="cross":
        answer=input("you crossed the old bridge and on the other side see a stranger ")
    elif answer =="back":
        print("you head back in the direction you came from but end up getting lost")

    else:
        print("not a valid option. your quest has ended")
      

else:
    print("Not a valid option. Your quest has ended")
