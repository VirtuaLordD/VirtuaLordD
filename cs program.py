def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return n,"is not prime"
    else:
        return n,"is prime"
def palindrome(n):
    temp=n
    r=0
    while n!=0:
        r=r*10+n%10
        n=n//10
    if temp==r:
        return temp, "is palindrome"
    else:
        return temp, "is not palindrome"
n=int(input("Enter-"))
print(prime(n),palindrome(n))