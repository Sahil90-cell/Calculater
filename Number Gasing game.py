print("This is a number guessing Game")
n=0
while(n<=9):
    n1=int(input("Guess between 1 to 100: \n"))
    if n1>18:
        print("You enter too high")
        n=n+1
        print(9-n,"Gases left")

    elif n1<18:
        print("You enter too Low")
        n=n+1
        print(9-n,"Gases left")

    else:
        print("You win")
        print(n,"Number of guess to finish")
        print(9-n,"Gases left")
        break

    if (n>9):
     print("Game Over")
