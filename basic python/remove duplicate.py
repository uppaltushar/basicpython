n=int(input("enter"))
d={}
for i in range(1,n+1):
    d[i]=int(input("enter"))
d1={}
for i,j in d.items():
    if j not in d1.values():
        d1[i]=j
print(d1)
