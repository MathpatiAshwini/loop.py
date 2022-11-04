n=int(input("enetr the number:"))
i=1
while i<=n:
    k=1
    while k<=n-i:
        print("",end="")
        k+=1
        j=i
        while j>=1:
            print(j,end="")
            j+j+1
        m=2
        while m<=i:
            print(m,end="")
            m+=1
        i+=1
        print()