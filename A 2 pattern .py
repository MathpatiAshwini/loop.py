# n=int(input("enter the rows:"))
# r=0
# while r<=n:
#     j=0
#     while j<=r:
#         k=ord("A")
#         print(chr(k),end=" ")
#         j=j+1
#     print()
#     k=k+1
#     r=r+1
    
    
n=int(input("enter the rows:"))
k=ord("A")
for i in range(n):
    for j in range(i+1):
        print(chr(k),end=" ")
        k=k+1
    print()

# n=int(input("enter the rows:"))
# r=1
# while r<=n:
#     i=1
#     while i==n-r:
#         print(" ",end=" ")
#         i=i+1
#     j=0
#     while j<=r:
#         k=ord("A")
#         print(chr(k),end=" ")
#         j=j+1
#     print()
#     k=k+1
#     r=r+1
