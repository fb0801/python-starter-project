import random


user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]

while True:
    user_input =input("Type Rock/Paper/Scissors or Q to qit:").lower()
    if user_input =="q":
        break #end the program

    if user_input not in options:
        continue


    random_number = random.randint(0,2)
    # rock0, paper: 1, sci: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick)


    if user_input =="rock" and computer_pick =="scissors":
        print("you won!")
        user_wins+=1
        
    elif user_input =="paper" and computer_pick =="rock":
        print("you won!")
        user_wins+=1
        
    elif user_input =="rock" and computer_pick =="paper":
        print("you won!")
        user_wins+=1
        
    else:
        print("You lost I win human")
        computer_wins +=1
    


print("you won", user_wins, "times")
print("The computer wins", computer_wins, "times")
print("This is the end \n This is the end \n Beautiful friend \n This is the end \n My only friend, the end")
