import abstra.workflows as aw

# Use Scripts to run Python code after any workflow Stage

# You can store data in the current thread,
# so it will be available in the next stages
aw.set_data("script_output", "Some data from the script!")
import pickle
import os
from PIL import Image
from tabulate import tabulate
image = Image.open(r"C:\Users\farfa_sxd1r1j\Documents\FADIL'S FOLDER\Fadil Programs\Player management system\711.vresize.350.350.medium.70.webp")

def add():
    with open(r"C:\Users\farfa_sxd1r1j\Documents\FADIL'S FOLDER\Fadil Programs\Player management system\players.dat", 'ab') as fob:
            stats=[]
            stats.append(input('Player name: '))
            stats.append(input('Enter position in 2 letters: ').upper())
            if stats[1]== 'GK':
                stats.append(int(input('Saves: ')))
                stats.append(int(input('Clean sheets: ')))
            else:
                stats.append(int(input('Goals scored: ')))
                stats.append(int(input('Assists scored: ')))
            stats.append(input('Nationality: '))
            stats.append(input('Club: '))
            pickle.dump(stats, fob)
            print(f"{' PLAYER ADDED ':=^75}")

def create():
    n = int(input('No. of players you want in your team: '))
    for i in range(n):
        print("-"*74)
        add()
    print(f"{n,'PLAYERS ADDED':^74}")
            
def remove():
    fob=open(r"C:\Users\farfa_sxd1r1j\Documents\FADIL'S FOLDER\Fadil Programs\Player management system\players.dat", 'rb')
    fob2=open(r"C:\Users\farfa_sxd1r1j\Documents\FADIL'S FOLDER\Fadil Programs\Player management system\newplayers.dat", 'wb')
    p=input("Enter a Player name to remove:")
    flag=True
    try:
        while True:
            rec=pickle.load(fob)
            if rec[0]!=p:
                pickle.dump(rec,fob2)
            else:
                flag=False
    except EOFError:
        pass
    fob.close()
    fob2.close()
    os.remove(r"C:\Users\farfa_sxd1r1j\Documents\FADIL'S FOLDER\Fadil Programs\Player management system\players.dat")
    os.rename(r"C:\Users\farfa_sxd1r1j\Documents\FADIL'S FOLDER\Fadil Programs\Player management system\newplayers.dat",r"C:\Users\farfa_sxd1r1j\Documents\FADIL'S FOLDER\Fadil Programs\Player management system\players.dat")
    if flag:
        print("Player not found")
    else:
        print(f"{' PLAYER REMOVED ':=^75}")

def leaderboard():
    with open(r"C:\Users\farfa_sxd1r1j\Documents\FADIL'S FOLDER\Fadil Programs\Player management system\players.dat", 'rb') as fob:
        top={}
        GA=0
        try:
            while True:
                rec=pickle.load(fob)
                if rec[1]!='GK':
                    top[rec[2]]=rec
        except EOFError:
            pass
        tops=list(top.keys())
        tops.sort(reverse=True)
        print(tops)
        table = [[f"{'Name':^20s}",f"{'Pos':^5s}",f"{'Goals':^7s}",f"{'Assists':^9s}",f"{'Nationality':^13s}",f"{'Club':^15s}"]]
        for i in tops:
            table.append([f"{(top[i][0]):^20s}",f"{str(top[i][1]):^5s}",f"{top[i][2]}",f"{top[i][3]:^9d}",f"{(top[i][4]):^13s}",f"{(top[i][5]):^15s}"])
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    fob.close()
    
def search():
    with open(r"C:\Users\farfa_sxd1r1j\Documents\FADIL'S FOLDER\Fadil Programs\Player management system\players.dat", 'rb') as fob:
        p=input("Enter Player name:")
        try:
            while True:
                rec=pickle.load(fob)
                if rec[0]==p:
                    print("="*75)
                    print(f"{'Name':^20s}{'|'}{'Pos':^5s}{'|'}{'Goals':^7s}{'|'}{'Assists':^9s}{'|'}{'Nationality':^13s}{'|'}{'Club':^15s}{'|'}")
                    print("-"*74)
                    print(f"{rec[0]:^20s}{'|'}{rec[1]:^5s}{'|'}{rec[2]:^7d}{'|'}{rec[3]:^9d}{'|'}{rec[4]:^13s}{'|'}{rec[5]:^15s}{'|'}")
                    print("="*75)
                    break
            else:
                print("Player does not exist")
        except EOFError:
            pass
    fob.close()
    
def modify():
    fob=open(r"C:\Users\farfa_sxd1r1j\Documents\FADIL'S FOLDER\Fadil Programs\Player management system\players.dat", 'rb')
    fob2=open(r"C:\Users\farfa_sxd1r1j\Documents\FADIL'S FOLDER\Fadil Programs\Player management system\newplayers.dat", 'wb')
    p=input("Enter a Player name to modify:")
    flag=True
    try:
        while True:
            rec=pickle.load(fob)
            if rec[0]==p:
                rec[1] = input('Enter position in 2 letters: ').upper()
                if rec[1] == 'GK':
                    rec[2]= int(input('Saves: '))
                    rec[3]= int(input('Clean sheets: '))
                else:
                    rec[2]= int(input('Goals scored: '))
                    rec[3]= int(input('Assists scored: '))
                rec[5]= input('Club: ')
                pickle.dump(rec, fob2)
                flag=False
            else:
                pickle.dump(rec, fob2)
    except EOFError:
        pass
    fob.close()
    fob2.close()
    os.remove(r"C:\Users\farfa_sxd1r1j\Documents\FADIL'S FOLDER\Fadil Programs\Player management system\players.dat")
    os.rename(r"C:\Users\farfa_sxd1r1j\Documents\FADIL'S FOLDER\Fadil Programs\Player management system\newplayers.dat",r"C:\Users\farfa_sxd1r1j\Documents\FADIL'S FOLDER\Fadil Programs\Player management system\players.dat")
    if flag:
        print("Player not found")

print('''
1-create() – Inputting players
2-add() – Adding players with all details
3-remove() – Deleting a player from the file
4-leaderboard() – Arranging players
5-search() – Search a player to find the details
6-modify()''')
while True:
    ch=int(input('Enter Choice=>'))
    if ch==1:
        create()
    elif ch==2:
        add()
    elif ch==3:
        remove()
    elif ch==4:
        leaderboard()
    elif ch==5:
        search()
    elif ch==6:
        modify()
    else:
        print("Nigguh enter a choice which is available!")
        print(image.show())
        print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡀⣀⣠⣤⣤⣄⣤⣀⢀⠀⠀⢀⣤⣀⣄⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣴⣶⣟⢻⣿⣿⣿⣿⣷⣿⣿⣿⣿⣶⣿⣷⣶⣼⣿⣿⣶⣿⣿⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⣺⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢑⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠎⣾⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⢿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠙⠛⠉⠉⠁⠀⠀⠀⠀⠉⠙⠋⠙⢿⠙⢟⡽⣿⠻⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡰⡟⠁⠛⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠒⠛⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⠁⠀⢠⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢫⠁⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣼⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⣿⣿⣿⢻⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣌⠀⠐⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡫⣿⣗⡦⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠠⣿⡜⢻⠇⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠧⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢁⡎⡠⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣶⣶⣦⣤⣀⠀⠄⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⠿⣿⣿⣿⣿⣿⣈⠁⠐⠈⡁⠀⠌⠁⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣧⡟⣿⣿⢼⣯⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⡿⠁⠤⠒⠛⢿⣿⣿⣷⣄⠠⠀⢀⠀⠒⠛⣿⣿⣿⣿⣿⣾⣷⣶⣶⣶⣶⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣽⡿⣕⣿⣿⣿⣽⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡅⢀⣠⣞⣛⡛⢛⢻⡿⣿⡆⠀⠀⠀⠁⠀⠀⠭⣉⣻⣿⣿⣿⣿⡟⠛⠻⠿⠿⢿⣿⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣿⢻⣼⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⣟⣿⣿⣿⣿⠻⢷⠶⣽⠃⠀⠀⠀⠀⠀⢀⢴⣿⣿⣿⣿⣿⣿⣿⣷⡦⣤⣀⠀⠠⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⣿⣿⣿⢿⣿⣿⡟⣿⣿⣿⣿⡿⠿⠿⠿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠋⢺⣿⣿⣭⣿⣻⠃⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⢿⣿⣟⣻⡿⠿⠾⢽⣲⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣼⢿⡟⠀⣡⡼⠛⠁⣀⡠⠴⣖⢻⡃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠹⢿⡿⠿⢹⠇⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⢸⣿⡿⢶⣾⣁⣀⠀⠀⠀⠉⠹⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣷⠏⢀⡿⠁⠀⢀⣾⠉⠀⠀⢿⣇⢱⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠈⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠒⠀⠈⠉⠒⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡟⠋⠐⢉⡠⣄⣴⣿⡿⠀⣨⣁⠘⣿⣇⢧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⢟⠛⠟⠃⠀⠸⣇⠀⢸⣿⠸⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣸⡅⠀⠀⠀⠀⣿⣶⣀⠀⠀⠀⠹⡄⢸⡇⢸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⢀⣿⣼⠀⠀⠀⢱⣄⣿⣿⣿⣷⠀⠀⠁⣿⡾⠅⡼⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⠀⠀⠀⢺⣄⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⡆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⠀⠀⠀⠀⣰⣾⣿⡷⠀⠀⠀⠀⣿⡿⠉⡉⢻⣷⣤⢢⢏⡟⢠⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣦⢀⣄⠠⠝⣿⣿⢿⣦⣤⣤⣶⣶⣶⣦⣄⣠⣴⠇⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⢠⣴⣿⣿⣿⡇⠀⠀⠀⢠⣿⠋⣀⠄⣸⣿⡷⢋⣾⠃⡞⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡫⠅⠀⠀⠈⠙⢻⣿⣯⣭⣭⡭⣙⣿⡿⠛⠁⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠀⣾⣿⣿⣿⣷⣿⢧⠀⠀⠀⠿⠥⠞⠁⠈⠉⢉⣴⡿⠁⡜⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡄⠀⠈⠀⣀⣴⣿⣿⣿⣽⣷⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⢠⣧⠞⣿⣿⣿⡟⣿⣷⠀⢳⣿⣶⣦⣤⠤⠲⠞⠛⠛⢁⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⡈⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣧⢼⣿⣟⣯⣿⣟⣿⣿⣿⢳⣾⣿⡌⠛⠐⠀⠀⠀⢀⠔⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣷⣿⣿⣿⣿⣿⣿⡛⣛⣛⣿⣟⡿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣰⣀⣻⣿⣾⣿⣾⣿⡿⣿⣿⣿⣿⣴⣧⣿⣿⣦⣀⣀⣴⠖⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣭⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣤⣬⣿⣿⣿⢿⣿⣿⣿⣿⣿⣧⡿⣿⣿⣿⠂⣙⣿⣿⠟⠃⠀⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡟⢊⣻⣈⠉⠉⠉⠉⠁⠈⠉⠚⠉⠉⠘⣿⣿⣿⣿⣿⡆⠀⢀⢀⣾⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣽⣻⣿⣿⣽⡿⠤⠁⠙⠁⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⢴⠄⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣷⣀⣤⣶⣿⣦⣭⣬⣍⣀⠂⠀⠀⠀⠀⠈⢿⣿⣿⣿⣟⣷⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡮⡼⢿⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣯⠘⢿⣿⣿⣿⣿⣿⢿⣞⠀⠀⢀⡀⢠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣾⣿⠀⠀⠀⠀⠀⠀⠀⢸⣜⢳⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠛⠁⠀⢠⠀⢀⣀⣤⡀⢠⣿⣿⣿⣿⣿⣧⠎⢸⣿⣿⣿⣿⡿⠌⠀⠄⠁⠄⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠠⠁⠀⠀⠀⠀⠀⢸⠀⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡏⢳⡀⠀⢀⢸⡼⠗⠻⠋⠁⠀⡾⣿⣿⣿⣿⣿⣿⣿⣮⣿⣟⣿⣏⣁⣦⣀⡀⣀⢲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⢀⠂⠀⠀⠀⠀⠀⠀⡿⠀⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠣⣌⠙⠛⠛⢉⣉⡹⢄⡟⠒⢺⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⢹⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣩⣴⣒⡾⠋⡹⣄⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡃⣸⣿⠿⢿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠉⢹⡏⠀⠀⢱⣿⡾⠏⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⣿⡿⢷⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢒⣩⣥⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⢸⢻⣧⣿⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⡿⣟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠋⠀⠀⠀⠂⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⢠⠇⠠⣾⢿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣻⢫⠝⣦⢩⣷⣌⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣟⡻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⣸⣿⢿⣾⣟⣿⣿⣿⣞⣿⣿⣿⣯⣝⢦⡀⠀
⠀⠘⣿⣿⣿⣿⣿⣷⣯⠭⣤⢧⣼⣹⠾⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣝⡿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣱⢦⠙⠁⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⢰⣿⣿⣽⣿⣿⣿⣿⡇⠽⡳⢋⡽⣿⣿⣿⣯⡀
⠀⢰⣿⣿⣿⣿⣿⣿⣷⣼⣳⣿⣴⣶⣾⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣟⠛⠿⣿⣿⣿⣿⣽⣾⣋⠔⠂⠄⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠈⠀⠀⠀⡸⠁⢠⢿⣿⣿⣿⣿⣿⣿⡿⣵⠁⢶⠁⠇⡈⡛⢷⢻⠁
⠀⠐⣿⣿⣿⣿⣟⣻⣿⡿⣿⣿⣿⡟⣿⢻⢿⣻⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣮⣌⣉⠻⠿⢮⣉⡉⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠃⢀⣞⡿⢋⣻⣿⣿⣿⣟⣙⠭⡍⣃⠬⣅⠐⡀⢂⢟⠀
⠀⠠⣿⣿⡿⠷⠿⣯⡿⣿⣿⡿⣿⣿⣾⣿⣿⣿⡿⣾⠿⢿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣌⡉⠲⣄⡀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⣰⠃⢀⡼⣿⣻⣼⣿⣿⣿⣻⣰⣶⡆⠲⠤⠖⠛⠐⠊⠀⠀⠀
⠀⠀⠙⠛⠂⠈⠐⠚⠛⠛⠓⠛⠚⠛⠛⠓⠛⠛⠒⠛⠒⠁⠐⠈⠘⠛⠛⣿⢿⣿⠿⠿⠟⠿⠿⠿⠿⣿⠿⣿⣿⣿⣿⣻⣷⡦⠹⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠏⠠⠞⠻⠿⠿⠿⠟⠛⠓⠁⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⢉⡉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
