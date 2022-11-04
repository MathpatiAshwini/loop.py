r=7
c=5
i=1
while i<=r:
    j=1
    while j<=c:
        if (j==1) or (j==5) or (i==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()