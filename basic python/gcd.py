c=0
a=int(input("enter no"))
b=int(input("enter no"))
if(a>b):
    while(b!=0):
        c=b
        b=a%b

else:
    while(a!=0):
        c=a
        a=b%a
print(c)
