n=int(input("enter the number:"))
i=0
while i<=n:
    i=i+1
    if i%2==0:
        print(i**2,end="-")
    else:
        print(i**2,end="+")