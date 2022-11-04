n=int(input("enter the number:"))
sum=0
i=0
a=len(str(n))
while n>0:
    r=n%2
    b=r*10**i
    sum=sum+b
    i=i+1
    n=n//2
print(sum)


n=int(input("enter the number:"))
i=1
while i<=n:
    k=1
    while k<=n-i:
        print(" ",end=" ")
        k=k+1
    j=1
    while j>=1:
        print(j,end=" ")
        j=j-1
    m=2
    while m<=i:
        print(i,end=" ")
        m=m+1
    i=i+1
    print()
        