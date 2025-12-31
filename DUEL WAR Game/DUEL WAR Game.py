while True:
    print("_"*64)
    print('''1: Throw stones🪨: Spend 5 power to inflict 10 damage on a roll of 2-6.
2: Punch opponent🤜: Spend 10 power to inflict 20 damage on a roll of 3-6. 
3: Club opponent with tail💢: Spend 15 power to inflict 30 damage on a roll of 4-6.
4: Claw opponent🐾: Spend 20 power to inflict 40 damage on a roll of 5-6.
5: Bite opponent🦷: Spend 25 power to inflict 50 damage on a roll of 6.''')
    print("_"*64)
    Player=input("Enter player name-")
    Mode=input('''Enter 'M' for Multiplayer
Enter 'S' for Singleplayer-''')
    if Mode=="M":
        Player2=input("Enter player 2 name-")
    else:
        Player2="Enemy"
    import random
    PowerA=PowerB=100
    HealthA=HealthB=100
    a={'5':[25,50,"bit",'🦷'],'4':[20,40,"clawed",'🐾'],'3':[15,30,"clubed","with tail 💢"],'2':[10,20,"punched",'🤜'],'1':[5,10,"threw stones at",'🪨']}
    c=random.randint(-1,1)
    C={-1:[PowerA,HealthA,Player],1:[PowerB,HealthB,Player2]}
    print(" Power of",Player+"-",PowerA,"| Power of",Player2+"-",PowerB,"\n","Health of",Player+"-",HealthA,"| Health of",Player2+"-",HealthB)
    print("_"*(27+len(Player)+len(Player2)))
    while C[-1][0]>0 and C[1][0]>0 and C[-1][1]>0 and C[1][1]>0:
        if Mode!="M"and c==1:
            for k in a.keys():
                if C[1][0]>a[k][0]:
                    X=str(random.randint(1,int(k)))
                    break
            if C[1][0]==5:
                X='1'
            print("Attack of",Player2+"-",X)
        else:
            X=input("Enter attack of "+C[c][2]+"-")
        x=random.randint(1,6)
        if X in a.keys():
            if C[c][0]<a[X][0]:
                print("Insufficient power\a")
            else:
                if x>int(X):
                    C[c][0]-=a[X][0]
                    C[c*-1][1]-=a[X][1]
                    print(x,":",C[c][2],a[X][2],C[c*-1][2],a[X][3],'\a')
                else:
                    C[c][0]-=a[X][0]
                    print(x)
                c*=-1
        else:
            print("Invalid Attack")
        print(" Power of",Player+"-",C[-1][0],"| Power of",Player2+"-",C[1][0],"\n","Health of",Player+"-",C[-1][1],"| Health of",Player2+"-",C[1][1])
        print("_"*(27+len(Player)+len(Player2)))
    else:
        log=open(r"C:\Users\farfa_sxd1r1j\Documents\FADIL'S FOLDER\Fadil Programs\DUEL WAR Game\War Log.txt","a+")
    #top=open(r"C:\Users\farfa_sxd1r1j\Documents\FADIL'S FOLDER\Fadil Programs\DUEL WAR Game\Leaderboard.txt","a+")
        if C[-1][0]==0 and C[1][1]<=0 or C[1][0]==0 and C[-1][1]<=0:
            print(" "*((21+len(Player)+len(Player2))//2),"DRAW!\a")
            log.writelines("\n"+Player+" drew "+Player2)
        elif C[-1][0]==0 or C[-1][1]<=0:
            print("  "*((16+len(Player)+len(Player2))//2),Player2,"WON!\a")
            log.writelines("\n"+Player2+" defeated "+Player)
        elif C[1][0]==0 or C[1][1]<=0:
            print("  "*((16+len(Player)+len(Player2))//2),Player,"WON!\a")
            log.writelines("\n"+Player+" defeated "+Player2)
        log.close()
'''Players=[]
for line in log.readlines():
    W=line[0]
    if player in top.readlines():'''

