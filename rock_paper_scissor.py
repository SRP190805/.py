import random as rand

c = 0
p = 0
print("computer:\n" + " " + f"{c}\n" + "player:\n" + " " + f"{p}\n")
def main(n=0):
    list = ["ROCK", "PAPER","SCISSOR"]
    if not n:
        c = 0
        p = 0
    computer = rand.choice(list) 
    player = str(input("enter your choice rock-paper-scissor//Quit:\n")).upper()
    flag = 1
    while (flag):
        if (player == "ROCK"):
            if(computer == "SCISSOR"):
                print("you destroyed him!")
                p += 1
                print("computer:\n" + " " + f"{c}\n" + "player:\n" + " " + f"{p}\n")
                main(n)
            else:
                print("")
                c += 1
                print("computer:\n" + " " + f"{c}\n" + "player:\n" + " " + f"{p}\n")
                main(n)
        elif(player == "PAPER"):
            if(computer == "ROCK"):
                print("you wrapped him!")
                p += 1
                print("computer:\n" + " " + f"{c}\n" + "player:\n" + " " + f"{p}\n")
                main(n)
            else:
                print("computer juct cut you out!")
                c += 1
                print("computer:\n" + " " + f"{c}\n" + "player:\n" + " " + f"{p}")
                main(n)
        elif(player == "SCISSOR"):
            if(computer == "PAPER"):
                print("you just cut the computer!")
                p += 1
                print("computer:\n" + " " + f"{c}\n" + "player:\n" + " " + f"{p}\n")
                main(n)
            else:
                print("computer just destroyed you!")
                c += 1
                print("computer:\n" + " " + f"{c}\n" + "player:\n" + " " + f"{p}\n")
                main(n)
        else:
            print("you sure you want to quit!")
            i = str(input("true/false?:\n")).upper()
            if i:
               flag = 0
            #print("Scores:\n")
    #print("computer:\n" + f"{c}\n" + "player:\n" + f"{p}\n")        

def choice():
    n = input("enter 1 to continue the game:\n")
    main(n)

main()
choice()