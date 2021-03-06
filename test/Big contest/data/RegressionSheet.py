import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import pandas as pd
import statsmodels.formula.api as sm
from pandas.stats.api import ols
from collections import OrderedDict

Cust_data=pd.read_csv('BGCON_CUST_DATA.csv', encoding='utf-16')
data1=Cust_data[Cust_data['SIU_CUST_YN']=='Y']#학습용 사기자
data2=Cust_data[Cust_data['SIU_CUST_YN']=='N']#학습용 비사기자
Eval_data=Cust_data[Cust_data['DIVIDED_SET']==2]#평가용 데이터
#X=Cust_data[['AGE','CHLD_CNT']] ->필요한 데이터 추출방법
#y=Cust_data['SIU_CUST_YN']
x=Cust_data['AGE']
y=Cust_data['CHLD_CNT']
z=Cust_data['LTBN_CHLD_AGE']
'''


df = pd.DataFrame({'Age':x,"ChildCnt":y,'ChildAge':z})
result = sm.ols(formula="ChildCnt ~ Age + ChildAge", data=df).fit()
print(result.summary())

inter,slop = result.params
print(inter,slop)
fig,ax=plt.subplots()
ax.plot(x,inter+slop*x,color='red')
ax.scatter(x,y)
plt.show()
'''

def regression(dependent,*argv):
    li=[]
    dict=OrderedDict()
    str1=input("please enter your name of dependent variable")
    for i in range(len([*argv])):
        str=input("please enter your name of independent variable")
        li.append(str)#list of names of independent variable

    dict[str1] = dependent
    a=0
    for i in argv:
        dict[li[a]]=i
        a+=1

    df = pd.DataFrame(dict)
    a=list(dict.keys())
    result = sm.ols(formula="{}~%s".format(a[0]) %'+'.join(e for e in a[1:]), data=df).fit()
    print(result.summary())
regression(x,y,z)

