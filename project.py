import random

computer = random.choice([1,-1,0])
Dics = {0:"Gun",1:"Snake",-1:"Water"}
print('Gun for g",Snake for s And Water for w')
youstr = input("Choice your input : ")
youDict = {"g":0,"s":1,"w":-1}

you = youDict[youstr]

print(f"computer choise is : {Dics[computer]} \nYour choise is :{Dics[you]}")

if(computer == you):
    print("Draw Match!\nTry Again ...")

else:
    if(computer == 0 and you == 1):
        print("You Lose!")
    elif(computer == 0 and you == -1):
        print("you won!")   
    elif(computer == 1 and you == -1):
        print("You Lose!") 
    elif(computer== 1 and you == 0):
        print("you won!") 
    elif(computer == -1 and you == 0):
        print("You Lose!")
    elif(computer == -1 and you == 1):
        print("you won!") 
    else:
        print("Somthing Wrong ...")


