n=int(input("enter the rows:"))
r=0
while r<=n:
    j=0
    k=ord("A")
    while j<=r:
        print(chr(k),end=" ")
        j=j+1
        k=k+1
    print()
    r=r+1

n=int(input("enter the rows:"))
for i in range(n):
    k=ord("A")
    for j in range(i+1):
        print(chr(k),end=" ")
        k=k+1
    print()




