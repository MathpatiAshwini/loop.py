
# n=int(input("enter the number:"))
# row=0
# while row<n:
#     space=n-row-1
#     while space>0:
#         print(end=" ")
#         space=space-1
#     star=row+1
#     while star>0:
#         print("*",end=" ")
#         star=star-1
#     row=row+1
#     print()

a=int(input("eneter the number:-"))
i=a
len=(str(a))
sum=0
while a>0:
    d=a%10
    sum+=d**len
    a//=10
if i==sum:
    print(i,"is armstrong number:-")
else:
    print(i,"is not armstrong number")