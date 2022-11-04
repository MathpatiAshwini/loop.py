r=6
c=5
i=0 
while i<r:
    j=0
    while j<c:
        if (i==0 and j!=0 and j!=4) or (j==0 and i!=0) or (j==4 and i!=0) or (i==3 and j>0 and j<5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()
    