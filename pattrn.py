n=int(input("enter the number:"))
for i in range(n):
    for j in range (n-i-1):
        print(" ",end=" ")
    for j in range(i,-1,-1):
        print(n-i,end=" ")
    print()