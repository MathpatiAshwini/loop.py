n=int(input("enter the number:"))
i=0
k=ord("A")
while i<=n:
    j=0
    while j<=i:
        if i%2==0:
            print(chr(k),end=" ")
            j+=1
            k=k+1
        print()
        i=i+1