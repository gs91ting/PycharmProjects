# ***Deque : 양방향 큐 (데크)는 컨테이너 양쪽 (앞뒤)에 아이템을 넣거나
#            뺄 수 있다.
import collections

deq = collections.deque('Hello Python')
print(deq)
print(deq[0])
print(deq[-1])
deq.append(1)
deq.appendleft('k')
deq.extendleft('d')
deq.remove('o')
deq.insert(3,1)
print(deq)

deq1 = collections.deque()
deq1.extend('가나다라마바사')
print(deq1)
deq1.extendleft('요')
print(deq1)

#아이템 꺼내기
'''while True:
    try:
        print (deq1.pop(), end=' ') #오른쪽부터 꺼낸다
    except IndexError:
        break'''
print(" ")
print("왼쪽에서 꺼내오기")
while True:
    try:
        print (deq1.popleft(), end=' ') #오른쪽부터 꺼낸다
    except IndexError:
        break