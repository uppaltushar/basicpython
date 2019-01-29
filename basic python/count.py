a=int(input("enter a no"))
i=j=k=0
while a!=-1:
    if a>0:
        i=i+1
    elif a<0:
        j=j+1
    else:
        k=k+1
    a=int(input('enter a no'))
print('+ve no ',i)
print('-ve ni is',j)
print('0s=',k)
