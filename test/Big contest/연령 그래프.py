class People:
    cnt=0
    def __init__(self,name1,name2):

        self.name1=name1
        self.name2=name2
        print("%s님 %s님 빅콘테스트 참여를 진심으로 축하드립니다." %(self.name1,self.name2))
        People.cnt+=2
        print("현재 {}명의 참가자가 있습니다".format(People.cnt))

Person1=People('장윤제','김동영')

import csv

matrix = []
matrix_1 = []

with open('사기 비사기 data.csv', 'r') as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        for i in row:
            a=i.split(',')
            matrix.append(a)
