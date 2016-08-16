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
data1=[] #사기자 age
data2=[] #비사기자 age
for i in range(1,len(matrix)):
    if 'Y' in matrix[i][2]:
        data1.append(int(matrix[i][4]))
    if 'N'  in matrix[i][2]:
        data2.append(int(matrix[i][4]))

#사기자 나이 범위
data1_0_10=[]
data1_11_20=[]
data1_21_30=[]
data1_31_40=[]
data1_41_50=[]
data1_51_60=[]
data1_61_70=[]
data1_71_80=[]
for i in data1:
    if i<11:
        data1_0_10.append(i)
    if 10<i<21:
        data1_11_20.append(i)
    if 20<i<31:
        data1_21_30.append(i)
    if 30<i<41:
        data1_31_40.append(i)
    if 40<i<51:
        data1_41_50.append(i)
    if 50<i<61:
        data1_51_60.append(i)
    if 60<i<71:
        data1_61_70.append(i)
    if 70<i<81:
        data1_71_80.append(i)



import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='gs91ting', api_key='87cmy6musf')



data1_box=[go.Bar(
                x=['0~10세','11~20세','21~30세','31~40세','41~50세','51~60세','61~70세','71~80세'],
                y=[len(data1_0_10),len(data1_11_20),len(data1_21_30),len(data1_31_40),len(data1_41_50),len(data1_51_60),len(data1_61_70),len(data1_71_80)])]

py.plot(data1_box, filename="사기자 연령")

#비사기자 나이 범위
data2_0_10=[]
data2_11_20=[]
data2_21_30=[]
data2_31_40=[]
data2_41_50=[]
data2_51_60=[]
data2_61_70=[]
data2_71_80=[]
data2_81_90=[]
for i in data2:
    if i<11:
        data2_0_10.append(i)
    if 10<i<21:
        data2_11_20.append(i)
    if 20<i<31:
        data2_21_30.append(i)
    if 30<i<41:
        data2_31_40.append(i)
    if 40<i<51:
        data2_41_50.append(i)
    if 50<i<61:
        data2_51_60.append(i)
    if 60<i<71:
        data2_61_70.append(i)
    if 70<i<81:
        data2_71_80.append(i)
    if 80<i<91:
        data2_81_90.append(i)

data2_box=[go.Bar(
                x=['0~10세','11~20세','21~30세','31~40세','41~50세','51~60세','61~70세','71~80세','81~90세'],
                y=[len(data2_0_10),len(data2_11_20),len(data2_21_30),len(data2_31_40),len(data2_41_50),len(data2_51_60),len(data2_61_70),len(data2_71_80),len(data2_81_90)])]

py.plot(data2_box, filename="비사기자 연령")


