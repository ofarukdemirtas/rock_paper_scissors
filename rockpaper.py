import random
computerscore = 0
playerscore = 0

list=["rock", "paper" , "scissors"]

while 1:
    playerchoice =input("Choose one Rock Paper or Scissors\n") 
    computer= random.choice(list)
    print(computer)
    if playerchoice==computer:
        print("that's a draw")
        
    elif (playerchoice=="rock" and computer=="scissors" ) or (playerchoice=="paper" and computer =="rock") or (playerchoice=="scissors" and computer=="paper"):
        playerscore+=1
        print("score={}-{}".format(computerscore,playerscore))
        print("you good bro ")
        
        if(playerscore==3):
            print("You won man congratsss")
            break

    elif (computer=="rock" and playerchoice=="scissors" ) or (computer=="paper" and playerchoice =="rock") or (computer=="scissors" and playerchoice=="paper"):
        computerscore+=1
        print("score={}-{}".format(computerscore,playerscore))
        print("you are losing man ")

        if(computerscore==3):
            print("You lost bro sorry  ")
            break
    else :
        print("please rock paper or scissors")
