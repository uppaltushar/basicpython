n=int(input("enter"))
d={}
for x in range(n):
    i=input()
    j=input()
    d[i]=j
for i in sorted(d):
    print(i,d[i])
