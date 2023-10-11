import random

top_of_range=int(input("Type a number: "))

if top_of_range <=0:
    print("pls type a number greater than 0")
    quit()

random_number= random.randint(0,top_of_range)
guesses=0

while True:
    guesses+=1
    user_guess=int(input("make a guess:"))
    if user_guess == random_number:
        print("you got it!")
        break
    elif user_guess > random_number:
        print("you are above that number")
    else:
        print("you are below that number")

print("you got it in",guesses,"guesses")
