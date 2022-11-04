i=0
r=7
c=4
while i<r:
    j=0
    while j<c:
        if (j==0) or (i==0 and j>0 and j<3) or(i==3 and j>0 and j<3) or (i==6 and j>0 and j<3) or (j==3 and i!=0 and i!=3 and i!=6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()

