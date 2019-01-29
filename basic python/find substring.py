q=[]
p=[]
n=int(input("enter"))
for i in range(n):
    a=input("enter the string")
    p.append(a)

m=int(input("enter"))
for i in range(m):
    b=input("enter the substring")
    q.append(b)
    z=q.split(" ")
for i in q:
    for j in p:
        if i in j:
            print(p.index(j))
    print(" ")
            
