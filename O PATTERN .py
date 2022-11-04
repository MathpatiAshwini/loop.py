r=7
c=5
i=1
while i<=r:
    j=1
    while j<=r:
        if (j==1 and i>2 and i<=5 ) or (j==5 and i>2 and i<=5) or (j==1 and i!=1 and i!=7)  or (j==5 and i!=1 and i!=7):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()