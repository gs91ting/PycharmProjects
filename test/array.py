# pprint(pretty print): 자료형 구조를 보기좋게 출력하는 모듈
data=[(1,{"a":'가','b':'라'}),3,4,5,6,
      (2,{'e':'바','ㄹ':1})]
print(data)
from pprint import *
pprint(data)

#array: 시퀀스 자료구조를 정의하는데,list와의 차이점은 모든 자료형이 동일하다.
import array
str = 'abcdefg'
arr = array.array('u',str) #array(타입코드, 값)
print(arr)
print(array.typecodes)

arr1 = array.array('i',range(5))
print(arr1)
arr1.extend(range(5))
print(arr1[3:6])

print(list(enumerate(arr1)))


