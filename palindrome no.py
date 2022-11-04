a=int(input("enetr the number:"))
b=a
num=0
while a>0:
    num=num*10+a%10
    a//=10
if b==num:
    print(b,"number is palindrome")
else:
    print(b,"number is not palindrome")

# a=input("enetr the character:")
# c=[0,1,2,3,4,5,6,7,8,9]
# b=a
# num=0
# len=len(str(a))m
# while b==len:
#     print(b[c])
# if c==num:
#     print(b,"character  is palindrome")
# else:
    # print(b,"character is not palindrome")

# i=int(input("enter the number:"))
# num=0
# x=i
# while i>0:
#     dig=i%10
#     num=num*10+dig
#     i=i//10
# if (x==num):
#     print(x," is palindrome number")
# else:
    # print(x," is not palindrome number")




