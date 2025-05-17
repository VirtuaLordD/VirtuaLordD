import random
R1=R2=0
while True:
    Ba=int(input("Enter batting no.-"))
    Bo=random.randint(1,6)
    print("Ball=",Bo)
    if Ba==Bo:
        break
    else:
        print("+",Ba,"runs",end="=")
        R1+=Ba
        print(R1)
print("Opponent needs",R1+1,"runs to win")
while R1>=R2:
    Ba=random.randint(1,6)
    Bo=int(input("Enter balling no.-"))
    print("Bat=",Ba)
    if Ba==Bo:
        if R1>R2:
            print("Player won by",R1-R2,"runs")
        else:
            print("Draw!")
        break
    else:
        print("+",Ba,"runs",end="=")
        R2+=Ba
        print(R2)
else:
    print("Opponent won by",R2-R1,"runs")