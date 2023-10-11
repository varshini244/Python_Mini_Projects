name=input("Type your name: ")
print("Welcome",name,"to this adventure")

answer=input("You are on a dirt road,it comes to an end and you can go left or right. Which way would you like to go? ").lower()

if answer=="left":
    answer=input("you come to river, you can walk around it or swim across (walk/swim)").lower()
    if answer=="swim":
       print("you swam across and were eaten by allegator")
    elif answer=="walk":
       print("you walked for many miles, ran out of water and you lose!")
    else:
       print("not a valid option,you lose")

elif answer=="right":
    answer=input("you come to a bridge,it looks wobbly, do you want to cross it or head back (cross/back)?").lower()
    if answer=="back":
       print("you go back to the main road and lose ")
    elif answer=="cross":
       answer=input("you cross the bridge and meet a stranger. Do you want to talk to them (yes/no)?").lower()
       if answer=="yes":
          print("you talk to the stranger and they gave you gold and you win!")
       elif answer=="no":
          print("you said no and you lose!")
       else:
          print("not a valid option,you lose")
    else:
       print("not a valid option,you lose")
    
else:
    print("not a valid option,you lose")

print("Thank you for trying!",name)