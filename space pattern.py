# n=int(input("enter the number:"))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i,-1,-1):
#         print(j+1,end=" ")
#     print()

# n=int(input("enter the number:"))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i,-1,-1):
#         print(i+1,end=" ")
#     print()

a=int(input("enter the number:"))
i=a
while a>=0:
    s=0
    while s==s-a:
        print(" ",end=" ")
        s=s-1
    j=i
    while j<=i:
        print(j,end=" ")
        j=j-1
    i=i-1
    print()


