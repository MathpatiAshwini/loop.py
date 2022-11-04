c=4
r=7
i=1
while i<=r:
    j=1
    while j<=c:
        if (j==1) or (i==1) or (i==4) or (i==7):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()

# c=4
# r=7
# i=1
# while i<=r:
#     j=1
#     while j<=c:
#         if (j==1) or (i==1) or (i==4) :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         j=j+1
#     i=i+1
#     print()

        