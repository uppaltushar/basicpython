"""
#1
a=[]
for i in range(1,11):
    a.append(i**2)
print(a)

#2
a=[i*i for i in range(1,11)]
print(a)

#3
a=['tushar','venus','yugam']
a=[i[0] for i in a]
print(a)

#4
a='my name is tanu'
b=a.split(' ')
b=[[i.upper(),len(i)] for i in b]
print(b)


#5
prod=lambda a,b:a*b
print(prod(2,3))


#6
lar=lambda a,b:max(a,b)
print(lar(3,2))
"""
#7
lar=lambda a,b:a if a>b else b
print(lar(4,5))
