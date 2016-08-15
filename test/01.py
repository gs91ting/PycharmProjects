def remove_adjacent_dups(x):
    for a in x:
        while x.count(a)>1:
            x.pop(x.index(a))
    print(x)

remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9])
remove_adjacent_dups([])
remove_adjacent_dups(["a", "big", "big", "bite", "dog"])

def rotate(x,k):
    for i in range (0,k+1):
        a=x.pop(0)
        x.append(a)
    print(x)

rotate([1,2,3,4,5,6,7],3)
ll=[2,3,3,3,4]


def isomorphic(x,y):
    if len(x)==len(y)==3:
        li=[]
        for i in x:
            if x.count(i) == 2:
                li.append(1)
        for j in y:
            if y.count(j)== 2:
                li.append(1)

        if li.count(1)==4:
            print('These words are isomorphic')
        else:
            print('nah')
    else:
        print("input correct words")

def largest(x,k):
    for i in range(1,k+1):
        a=x.index(max(x))
        b=x.pop(a)
    print(b)

largest([3,2,1,5,6,4],1)


def fib(x):
    start=1
    start_1=1
    list=[]
    list.append(start)
    list.append(start_1)
    if x==1 or x==2:
        print(start)
    else:
        j=-1
        k=0
        for i in range(x-2):
            j+=1
            k+=1
            list.append(list[j]+list[k])
        print(max(list))

print("================")
def repeat(x,y):
    x.sort()
    for i in x:
        a=y-i
        x.pop(x.index(i))
        if a ==0:
            print(i)
        if a in x:
            print(i,a)

repeat([1,2,3,4,5,15,7,8],24)

a= [12,3,4,5,7,8]
print(a)
import math
def check(x):
    if x==2:
        return True
    j=0
    if x>2 and x%2!=0:
        for i in range(1,int(math.sqrt(x))+1):
            if x%i==0:
                j+=1
    if (j+1)==2:
        return True
    else:
        return False


print(check(17))


def prime(x):

    i=1
    j=1
    while j<x:
        i+=1
        if check(i) is True:
            j+=1
    print(i)

import time
start_time=time.time()

'''
def prime_num(x):
    j=0
    for i in range(0,x):
        if check(i) is True:
            j+=i
    print(j)

prime_num(2000000)'''
'''
def productk(x):
    li=[]
    b=x.split()
    c=[b[0:20],b[20:40],b[40:60],b[60:80],b[80:100],b[100:120],b[140:160],b[160:180],b[180:200],b[200:220],b[220:240],b[240:260],b[260:280],b[280:300],b[300:320],b[320:340],b[340:360],b[360:380],b[380:400],]
    for i in range(0,19):
        for j in range(0,16):
            d=int(c[i][j])*int(c[i][j+1])*int(c[i][j+2])*int(c[i][j+3])
            li.append(d)

    for i in range(0,16):
        for j in range(0,19):
            d=int(c[j][i])*int(c[j][i+1])*int(c[j][i+2])*int(c[j][i+3])
            li.append(d)

    for i in range(0,16):
        for j in range(0,16):
            d=int(c[j][i])*int(c[j+1][i+1])*int(c[j+2][i+2])*int(c[j+3][i+3])
            li.append(d)



    print(max(li))
'''
from itertools import chain, cycle, accumulate, count
import math
def factor(x):

    li=[1]

    for i in range(2,int(math.sqrt(x))+1):

        if x%i==0:
            li.append(i)

            if not x//i in li:
                li.append(x // i)


    return(len(li)+1)

'''
for j in accumulate(count(1)):
    if factor(j)>500:
        print(j)
        break'''

'''
problem 18

import random

def tree(x):

    li=[]
    while 1:
        b=random.randint(0,len(x)-3)
        c=random.randint(0,len(x)-3)

        k=0

        for i in range(3):
            if b<len(x)-3 and c<len(x)-3:
                k+=x[b][c]
                b+=1
                c+=1


            if k not in li:
                li.append(k)
        l=0
        for i in range(4):
            if b <= len(x) - 4 and c<= len(x)-4:
                l+=(x[b][c])
                b+=1
            if l not in li:
                li.append(l)
        if b <= len(x) - 4 and c<= len(x)-4:

            m=(x[b][c])+(x[b+1][c+1])+(x[b+2][c+2])+(x[b+3][c+2])

            f = (x[b][c]) + (x[b + 1][c+1]) + (x[b + 2][c+1]) + (x[b + 3][c + 2])

            e = (x[b][c]) + (x[b + 1][c + 1]) + (x[b + 2][c + 1]) + (x[b + 3][c + 1])

            q = (x[b][c]) + (x[b + 1][c]) + (x[b + 2][c + 1]) + (x[b + 3][c + 2])

            w = (x[b][c]) + (x[b + 1][c]) + (x[b + 2][c + 1]) + (x[b + 3][c + 1])

            o = (x[b][c]) + (x[b + 1][c]) + (x[b + 2][c]) + (x[b + 3][c + 1])
            if m not in li:
                li.append(m)
            if f not in li:
                li.append(f)
            if e not in li:
                li.append(e)
            if q not in li:
                li.append(q)
            if w not in li:
                li.append(w)
            if o not in li:
                li.append(o)

        if len(li)==8*max(list(accumulate(chain(range(1,len(x)-2))))):
            print(max(li))
            break


tree([[75],[95,64],[17,47,82],[18,35,87,10],[20,4,82,47,65]])
'''