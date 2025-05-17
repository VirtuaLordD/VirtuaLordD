def compute(n):
    print(n,end=" ")
    if n==1:
        return 1
    else:
        return compute(n-1)
print("\nAnswer ",compute(5))