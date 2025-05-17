log=open(r"C:\Users\farfa_sxd1r1j\Documents\FADIL'S FOLDER\Fadil Programs\DUEL WAR Game\War Log.txt","r")
C=0
while True:
    st=log.readline()
    if st=="":
        break
    if st[0]=="E":
        C+=1
print(C)
log.close()