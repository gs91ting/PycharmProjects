#bisect 모듈 : 정렬된 상태로 아이템을 추가할 수 있는 모듈
#              데이터가 많은 경우 heapq보다 성능이 좋다.
import random


random.seed() #같은 랜덤한 결과를 나오게하는경우

for i in range(5):
    print('%.4f'%random.random(),end=' ')


print('new index list')
print('=== ===== ====')
import bisect
li=[]
random.seed(1)
for i in range (1,15):
    num=random.randint(1,100)
    pos = bisect.bisect(li,num) #인덱스값 리턴
    bisect.insort(li,num) #리스트를 정렬상태로 유지 insort_left(),insort_right()
    print("%3d %3d" %(num,pos),li)