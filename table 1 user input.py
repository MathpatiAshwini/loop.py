# a=int(input("enter the number:-"))
# i=1
# while i<=a:
#     j=1
#     while j<=10:
#         print(i,"*",j,"=",i*j)
#         j=j+1
#     i=i+1
#     print()

# a=int(input("enter the number:-"))
# i=1
# while a>0:
#     j=1
#     while j<=a:
#         print(i,end=" ")
#         j=j+1
#     a-=1
#     i=i+1
#     print()

# a=int(input("enter the number:-"))
# p=5
# i=1
# k=0
# while i<=a:
#     k=0
#     while k<=a:
#         if p-i+1:
#             print(" ",end=" ")
#             k=k-1
#         i=i+1
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
# #     print()
# a=int(input("enter the number:-"))
# i=a
# while i>0:
#     j=0
#     while j<=a-1:
#         print(" ",end=" ")
#         j=j+1
#     k=1
#     while k<=a:
#         print(k,end="")
#         k=k+i
#     i=i+1
#     print()

# a= int(input("enter the number:"))


# k=1
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(k,end=" ")
#         k=k+1
#         j=j+1
#     i=i+1
#     print()


i=1
while i<=5:
    j=1
    k=0
    a=0
    while j<=i:
        print(i+k,end=" ")
        j=j+1
        a=a+1
        k=k+5-a
    i=i+1
    print()

