import streamlit as st
import pandas as pd
import numpy as np



coDf=pd.read_csv('covid_19_clean_complete.csv') #파일불러오기
coDf['DT']=pd.to_datetime(coDf['Date'])         #Date의 변수형을 datetime으로 변경하여 DT생성


#국가별합계
st.title('전세게 코로나 데이터 분석')
latestDf = coDf[coDf['DT'] == max(coDf['DT'])]  #최신형날짜만 선택
latestDf_cntr_sum=latestDf.groupby('Country/Region')['Confirmed','Deaths','Recovered'].sum().reset_index()
latestDf_cntr_sum=latestDf_cntr_sum.sort_values(by='Confirmed',ascending=False).reset_index(drop=True)
st.dataframe(data=latestDf_cntr_sum)

#날짜별합계
st.write("## 시간에 따른 확진자, 사망자, 회복자 시각화")
coDf_st=coDf.groupby(by='DT')['Confirmed','Deaths','Recovered'].sum()
coDf_st.sort_index()
st.line_chart(data=coDf_st)



