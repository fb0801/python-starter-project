print("Welcome to my game")
playing = print("Do you want to play? ")

if playing != "yes":
    print("Leaving the game")
    quit()

print("Ok! lets play :)")

answer = str(input("What does CPU stand for? "))
if answer.lower() == "central processing unit": #convert the string to lowercase
    print("correct!")
    score+=1

else:
    print("Sorry that is incorrect")


answer = str(input("What does GPU stand for? "))
if answer.lower() == "graphics processing unit":
    print("correct!")
    score+=1
else:
    print("Sorry that is incorrect")


answer = str(input("What does RAM stand for? "))
if answer.lower() == "random access memory":
    print("correct!")
    score+=1
else:
    print("Sorry that is incorrect")


answer = str(input("What does PSU stand for? "))
if answer.lower() == "power supply unit":
    print("correct!")
    score+=1
else:
    print("Sorry that is incorrect")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score /4)* 100) +"%.")

