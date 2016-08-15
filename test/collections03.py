#namedtuple()
aa=('홍길동',24,'남')
bb=('강복녀',21,'여')

for n in [aa,bb]:
    print("%s은(는) %d 세에 %s성 입니다" %n)

import collections
Person = collections.namedtuple("Person",'이름 나이 성')
aa = Person(성='강길동',나이=25,이름='남')
bb = Person(이름='강복녀',나이=21,성='여')
for n in [aa,bb]:
    print("%s은(는) %d 세에 %s성 입니다" %n)

# OrderedDict: 자료의 순서를 기억하는 사전형 클래스

dic = {} #입력된 순서가 관계가 없다.
dic['a']='가'
dic['c']='다'
dic['b']='나'

for i,j in dic.items():
    print(i,j)

print('============================================================')
dic1 = collections.OrderedDict() #입력한 순서를 기억한다.
dic1['a']='가'
dic1['b']='나'
dic1['c']='다'

for i,j in dic1.items():
    print(i,j)


dic3={}
dic3['a']='가'
dic3['c']='다'
dic3['b']='나'

dic4=collections.OrderedDict()
dic4['b']='나'
dic4['c']='다'
dic4['a']='가'
print(dic3==dic4)
print(dic1==dic4) #orderedDict끼리는 값이 다르다
