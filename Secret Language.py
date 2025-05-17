while True:
    St=input("Enter a text-")
    for ch in St:
        if ch.isspace():
            print(" ",end="")
        else:
            print(chr(130000-ord(ch)),end="")
    print()