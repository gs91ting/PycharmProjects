import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import statsmodels.api as sm
import pandas as pd

Cust_data=pd.read_csv('BGCON_CUST_DATA.csv', encoding='utf-16')
data1=Cust_data[Cust_data['SIU_CUST_YN']=='Y']#학습용 사기자
data2=Cust_data[Cust_data['SIU_CUST_YN']=='N']#학습용 비사기자
Eval_data=Cust_data[Cust_data['DIVIDED_SET']==2]#평가용 데이터
#X=Cust_data[['AGE','CHLD_CNT']] ->필요한 데이터 추출방법
#y=Cust_data['SIU_CUST_YN']

print(Eval_data)