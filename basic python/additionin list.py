n=int(input("enter the elements in a list"))
p=[]
l=[]
for i in range(1,n+1):
    a=int(input("enter"))
    p.append(a)
    x=sum(p)
    l.append(x)
print(l)
