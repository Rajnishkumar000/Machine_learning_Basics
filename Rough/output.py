d=dict()
for i in range(5):
    d[i]=i*i
print(max(d))

D={1:2,2:3,3:4,4:5}
print(sum(D))

tuple1=(5,1,7,6,2)
# tuple1.pop(2)
print(tuple1)

import copy
a=[10,20,30,[40,50]]
b=copy.copy(a)
b[3][1]=80
c=copy.deepcopy(a)
c[3][0]=60
print(b,c)

def fun(n):
    if n>100:
        return n-5
    return fun(fun(n+11))
print(fun(45))

lst=[i for i in range(10)]
new_lst=list(filter(lambda x:x%2!=0,lst))
print(new_lst)

a=[1,2,3,4]
b=[sum(a[0:x+1]) for x in range(0,len(a))]
print(b)

lst=[10,20,30,10,30,40]
x=list(set(lst))
print(len(x))
