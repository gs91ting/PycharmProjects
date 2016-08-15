import heapq
from headdata import data

heapq.heapify(data)
print(data)
#heap데이터 접근하기 heappop()을 이용하면 가장작은 값을 리턴한다.
'''
b=[]
for n in range(5):
    a=heapq.heappop(data)
    b.append(a)

print(b)
'''
#힙데이터 수정 heapreplace()

heapq.heapreplace(data,30) #min 값을 3으로 변경
heapq.heapreplace(data,15)
print(data)

for n in range(1,60):
    heapq.heapreplace(data,n)

print(data)

#힙의 최대값 최소값 구하기: nlargest(),nsmallest()

print(heapq.nlargest(2,data)) #2개의 최대값을 가져와라
print(heapq.nsmallest(3,data))

