r=6
c=5
i=1
while i<r:
    j=1
    while j<c:
        if (j==1) or (i==1 and j!=1 and j!=4) or (i==5 and j!=4) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()