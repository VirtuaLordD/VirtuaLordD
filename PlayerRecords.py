import os
s = ' '
d = '|'
def cls():
   os.system('cls')
def view():
    print(f"{'Name':^12s}{'Age':^5s}{'Gender':^8s}{'Positions':^9s}{s}{'Club':^11s}{s}{'Preferred Foot':^14s}{s}{'Pace':^4s}{s}{'Shot':^4s}{s}{'Pass':^4s}{s}{'Vision':^6s}")
    PR=[]
    with open("PlayerRecords.txt","r") as r:
        for i in r.readlines():
            PR.append(i)
    for j in PR:
        n = j.split(',')[0].strip()
        a = j.split(',')[1].strip()
        g = j.split(',')[2].strip()
        p = j.split(',')[3].strip()
        c = j.split(',')[4].strip()
        f = j.split(',')[5].strip()
        pace,shot,pss,vison = j.split(',')[6].strip(),j.split(',')[7].strip(),j.split(',')[8].strip(),j.split(',')[9].strip()
        r = f"{n:^12s}{d}{a:^2s}{d}{g:^8s}{d}{p:^9s}{d}{c:^11s}{d}{f:^14s}{d}{pace:^4s}{d}{shot:^4s}{d}{pss:^4s}{d}{vison:^6s}"
        print('-'*len(r))
        print(r)
#def add():
    
while True:
    print('''PLAYER MANAGEMENT SYSTEM''')
    print("1: View Player Records")
    print("2: Add New Player")
    ch=input("Enter Choice - ")
    if ch=="1":
        view()
        print("\n")
    c=input("Do You Want to Contiue : ")
    if c.lower()=="no":
        break