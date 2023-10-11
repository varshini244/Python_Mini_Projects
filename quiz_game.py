print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay! let's play :)")
score=0

answer=input("what does CPU stands for? ").lower()
if answer == "central processing unit":
    print("correct!")
    score+=1
else:
    print("sorry,you're wrong!")

answer=input("what does GPU stands for? ").lower()
if answer == "graphics processing unit":
    print("correct!")
    score+=1
else:
    print("sorry,you're wrong!")

answer=input("what does RAM stands for? ").lower()
if answer == "random access memory":
    print("correct!")
    score+=1
else:
    print("sorry,you're wrong!")

answer=input("what does PSU stands for? ").lower()
if answer == "power supply":
    print("correct!")
    score+=1
else:
    print("sorry,you're wrong!")

print("you got",score,"questions correct")
print("you got",(score/4)*100,"%")

