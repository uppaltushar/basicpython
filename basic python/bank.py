n=int(input("enter"))
b=p=o=0
for i in range(1,n+1):
    a=(input("enter"))
    
    t,f=a.split(" ")
    if(t=='d'):
        p=p+int(f)
    else:
        o=o+int(f)
b=p-o
print(b)
    
