from re import I


n=int(input("enter the number:"))
i=1
p=1
while i<=n:
    p=i*p
    print(p,end="+")
    i=i+1