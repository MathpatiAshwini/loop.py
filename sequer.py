n=int(input("enter the number:"))
i=1
while i<=n:
    print(i,"=",i**2)
    i=i+1
    print()


n=int(input("enter the rows:"))
r=n
while r>0:
    k=ord("E")
    j=0
    while j<r:
        print(chr(k),end=" ")
        j=j+1
        k=k-1
    print()
    r=r-1